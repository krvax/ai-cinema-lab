import re
import os
import subprocess
import sys

def parse_formatting(text):
    # Code spans
    text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
    # Bold and italic combined
    text = re.sub(r'\*\*\*([^*]+)\*\*\*', r'<strong><em>\1</em></strong>', text)
    # Bold
    text = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', text)
    # Italic
    text = re.sub(r'\*([^*]+)\*', r'<em>\1</em>', text)
    # Links: [text](url)
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', text)
    return text

def md_to_html(md_text):
    html_out = []
    lines = md_text.splitlines()
    
    list_stack = [] # Stack of (indent_level, tag)
    in_table = False
    table_header_done = False
    
    for line in lines:
        stripped = line.strip()
        
        # Handle empty line
        if not stripped:
            if in_table:
                html_out.append("</table>")
                in_table = False
                table_header_done = False
            continue
            
        # Handle table rows
        if stripped.startswith("|") and stripped.endswith("|"):
            # Close lists if any
            while list_stack:
                _, t = list_stack.pop()
                html_out.append(f"</li></{t}>")
                
            # Parse row cells
            cells = [c.strip() for c in stripped.split("|")[1:-1]]
            
            # Check if this is a separator line (e.g., | --- | --- |)
            if all(re.match(r'^:?-+:?$', c) for c in cells):
                table_header_done = True
                continue
                
            if not in_table:
                html_out.append("<table>")
                in_table = True
                table_header_done = False
                
            is_total_row = "Total" in stripped
            row_class = " class='total-row'" if is_total_row else ""
            
            if not table_header_done:
                html_out.append("<tr>" + "".join(f"<th>{parse_formatting(c)}</th>" for c in cells) + "</tr>")
            else:
                html_out.append(f"<tr{row_class}>" + "".join(f"<td>{parse_formatting(c)}</td>" for c in cells) + "</tr>")
            continue
            
        # If we get a non-table line but were in a table, close it
        if in_table:
            html_out.append("</table>")
            in_table = False
            table_header_done = False
            
        # Handle horizontal rule
        if stripped == "---":
            while list_stack:
                indent, tag = list_stack.pop()
                html_out.append(f"</{tag}>")
            html_out.append("<hr>")
            continue
            
        # Determine indentation level
        indent_level = len(line) - len(line.lstrip(' '))
        
        # Headers
        h_match = re.match(r'^(#{1,6})\s+(.*)$', stripped)
        if h_match:
            while list_stack:
                indent, tag = list_stack.pop()
                html_out.append(f"</{tag}>")
            level = len(h_match.group(1))
            content = parse_formatting(h_match.group(2))
            html_out.append(f"<h{level}>{content}</h{level}>")
            continue
            
        # Blockquotes
        if stripped.startswith(">"):
            while list_stack:
                indent, tag = list_stack.pop()
                html_out.append(f"</{tag}>")
            content = parse_formatting(stripped[1:].strip())
            html_out.append(f"<blockquote><p>{content}</p></blockquote>")
            continue
            
        # List items (Unordered and Ordered)
        ul_match = re.match(r'^([\*\-\+])\s+(.*)$', stripped)
        ol_match = re.match(r'^(\d+)\.\s+(.*)$', stripped)
        
        if ul_match or ol_match:
            tag = "ul" if ul_match else "ol"
            content = ul_match.group(2) if ul_match else ol_match.group(2)
            content = parse_formatting(content)
            
            if not list_stack:
                html_out.append(f"<{tag}>")
                list_stack.append((indent_level, tag))
                html_out.append(f"<li>{content}")
            else:
                curr_indent, curr_tag = list_stack[-1]
                if indent_level > curr_indent:
                    html_out.append(f"<{tag}>")
                    list_stack.append((indent_level, tag))
                    html_out.append(f"<li>{content}")
                elif indent_level < curr_indent:
                    while list_stack and list_stack[-1][0] > indent_level:
                        _, t = list_stack.pop()
                        html_out.append(f"</li></{t}>")
                    if not list_stack or list_stack[-1][1] != tag:
                        html_out.append(f"<{tag}>")
                        list_stack.append((indent_level, tag))
                    else:
                        html_out.append("</li>")
                    html_out.append(f"<li>{content}")
                else:
                    if curr_tag != tag:
                        list_stack.pop()
                        html_out.append(f"</li></{curr_tag}><{tag}>")
                        list_stack.append((indent_level, tag))
                    else:
                        html_out.append("</li>")
                    html_out.append(f"<li>{content}")
            continue
            
        # Regular paragraph
        while list_stack:
            _, t = list_stack.pop()
            html_out.append(f"</li></{t}>")
            
        content = parse_formatting(stripped)
        html_out.append(f"<p>{content}</p>")
        
    while list_stack:
        _, t = list_stack.pop()
        html_out.append(f"</li></{t}>")
        
    if in_table:
        html_out.append("</table>")
        
    return "\n".join(html_out)

def highlight_costs(html):
    # Highlight USD $X.XX or USD $X.XX / segundo
    html = re.sub(
        r'USD\s+\$([0-9.]+)(?:\s*/\s*segundo)?',
        lambda m: f'<span class="cost-highlight">USD ${m.group(1)}{" / segundo" if "segundo" in m.group(0) else ""}</span>',
        html
    )
    # Highlight "Dentro de presupuesto."
    html = html.replace(
        '<strong>Dentro de presupuesto.</strong>',
        '<span class="status-good">Dentro de presupuesto.</span>'
    )
    return html

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    source_path = os.path.join(script_dir, "resumen_ejecutivo.md")
    html_path = os.path.join(script_dir, "resumen_ejecutivo.html")
    pdf_path = os.path.join(script_dir, "resumen_ejecutivo.pdf")

    if not os.path.exists(source_path):
        print(f"Error: {source_path} not found.")
        sys.exit(1)

    with open(source_path, "r", encoding="utf-8") as f:
        md_content = f.read()

    # Parse markdown to HTML body
    html_body = md_to_html(md_content)
    
    # Apply cost highlight styling
    html_body = highlight_costs(html_body)

    # HTML document template with styling
    html_template = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Resumen Ejecutivo - AI Cinema & Comercial</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=Inter:wght@300;400;500;600;700&family=Fira+Code:wght@400;500&display=swap');
        
        @page {
            size: A4;
            margin: 20mm;
        }
        
        body {
            font-family: 'Inter', sans-serif;
            color: #1e293b;
            background-color: #ffffff;
            line-height: 1.6;
            font-size: 10pt;
            -webkit-print-color-adjust: exact;
            print-color-adjust: exact;
            margin: 0;
            padding: 0;
        }
        
        .container {
            max-width: 800px;
            margin: 0 auto;
        }
        
        /* Document Title */
        h1 {
            font-family: 'Outfit', sans-serif;
            font-size: 22pt;
            font-weight: 800;
            color: #0f172a;
            line-height: 1.25;
            margin-top: 0;
            margin-bottom: 5px;
            letter-spacing: -0.025em;
            border-bottom: 2px solid #e2e8f0;
            padding-bottom: 15px;
        }
        
        /* Section Headings */
        h2 {
            font-family: 'Outfit', sans-serif;
            font-size: 13pt;
            font-weight: 700;
            color: #1e3a8a; /* Deep blue */
            margin-top: 25px;
            margin-bottom: 12px;
            border-left: 4px solid #3b82f6; /* Accent blue */
            padding-left: 12px;
            page-break-after: avoid;
        }
        
        h3 {
            font-family: 'Outfit', sans-serif;
            font-size: 11pt;
            font-weight: 600;
            color: #0f172a;
            margin-top: 20px;
            margin-bottom: 10px;
            page-break-after: avoid;
        }
        
        /* Paragraphs & text */
        p {
            margin-top: 0;
            margin-bottom: 10px;
            text-align: justify;
        }
        
        strong {
            font-weight: 600;
            color: #0f172a;
        }
        
        em {
            font-style: italic;
        }
        
        /* Lists */
        ul, ol {
            margin-top: 0;
            margin-bottom: 12px;
            padding-left: 20px;
        }
        
        li {
            margin-bottom: 6px;
        }
        
        /* Nested list */
        li ul {
            margin-top: 4px;
            margin-bottom: 0;
            padding-left: 20px;
            list-style-type: circle;
        }
        
        /* Links */
        a {
            color: #2563eb;
            text-decoration: none;
            font-weight: 500;
        }
        
        /* Blockquotes / Alerts */
        blockquote {
            margin: 15px 0;
            padding: 12px 18px;
            background-color: #f0f9ff;
            border-left: 4px solid #0284c7;
            border-radius: 0 8px 8px 0;
            color: #0369a1;
        }
        
        blockquote p {
            margin: 0;
            font-style: italic;
        }
        
        /* Code blocks & inline code */
        code {
            font-family: 'Fira Code', 'Courier New', Courier, monospace;
            font-size: 8.5pt;
            background-color: #f1f5f9;
            color: #0f172a;
            padding: 2px 5px;
            border-radius: 4px;
            border: 1px solid #e2e8f0;
        }
        
        hr {
            border: 0;
            height: 1px;
            background: #e2e8f0;
            margin: 20px 0;
        }
        
        /* Cost highlight styles */
        .cost-highlight {
            font-weight: bold;
            color: #047857; /* Emerald green */
            background-color: #ecfdf5;
            padding: 2px 6px;
            border-radius: 4px;
            border: 1px solid #a7f3d0;
            font-size: 9pt;
            display: inline-block;
        }
        
        .status-good {
            color: #047857;
            background-color: #d1fae5;
            padding: 2px 8px;
            border-radius: 9999px;
            font-weight: 600;
            font-size: 9pt;
            border: 1px solid #a7f3d0;
            display: inline-block;
        }
        
        /* Table styles */
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 15px 0;
            font-size: 9.5pt;
        }
        
        th {
            background-color: #f8fafc;
            color: #0f172a;
            font-weight: 600;
            text-align: left;
            padding: 6px 10px;
            border-bottom: 2px solid #e2e8f0;
        }
        
        td {
            padding: 6px 10px;
            border-bottom: 1px solid #e2e8f0;
            color: #334155;
        }
        
        tr:nth-child(even) td {
            background-color: #f8fafc;
        }
        
        tr.total-row td {
            font-weight: 700;
            background-color: #ecfdf5;
            color: #047857;
            border-top: 2px solid #10b981;
            border-bottom: 2px solid #10b981;
        }
    </style>
</head>
<body>
    <div class="container">
        {content}
    </div>
</body>
</html>
"""

    # Inject parsed HTML using .replace instead of .format to avoid braces issues
    full_html = html_template.replace("{content}", html_body)

    with open(html_path, "w", encoding="utf-8") as f:
        f.write(full_html)
        
    print(f"HTML intermediate file generated at: {html_path}")

    # Invoke Microsoft Edge to convert HTML to PDF
    edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    
    if not os.path.exists(edge_path):
        print(f"Error: Microsoft Edge not found at {edge_path}")
        sys.exit(1)

    print("Running Microsoft Edge in headless mode to render PDF...")
    command = [
        edge_path,
        "--headless",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={pdf_path}",
        "--no-margins", 
        html_path
    ]
    
    try:
        subprocess.run(command, check=True)
        print(f"Success! Beautiful PDF generated at: {pdf_path}")
    except subprocess.CalledProcessError as e:
        print("Failed to run Edge command:", e)
        sys.exit(1)
    finally:
        # Clean up HTML intermediate file
        if os.path.exists(html_path):
            os.remove(html_path)

if __name__ == "__main__":
    main()
