# 🌌 AI Cinema Lab

*Hecho con amor y estilo por Miguel Ángel Carvajal & Antigravity (Google DeepMind) 🎬🖤*

AI Cinema Lab applies Platform Engineering, FinOps, and Generative AI principles to media production.

From creative brief to published commercial:

```mermaid
flowchart LR
    A[Creative Brief]
    B[Prompt Engineering]
    C[Asset Generation]
    D[Video Generation]
    E[Audio Production]
    F[Post Production]
    G[Distribution]

    A --> B
    B --> C
    C --> D
    D --> E
    E --> F
    F --> G
```

---

## 🎯 Vision

Treat media production as a software delivery pipeline.

Instead of manually creating every asset, AI Cinema Lab combines:

- Prompt Engineering
- Generative Video
- Automated Rendering
- FinOps Governance
- Platform Engineering

to produce commercial content at scale.

---

## 🏗 Reference Architecture

See:

- [AI Cinema Pipeline](./AI-CINEMA-PIPELINE.md)
- [Platform Architecture](./docs/architecture.md)
- [FinOps Governance](./docs/finops.md)
- [Roadmap](./docs/roadmap.md)

---

## 🎬 Production Workflow

```mermaid
flowchart TD
    A[Business Brief]
    B[Prompt Engineering]
    C[Storyboard]
    D[Image Generation]
    E[Video Generation]
    F[Audio Production]
    G[Rendering]
    H[Distribution]

    A --> B
    B --> C
    C --> D
    D --> E
    E --> F
    F --> G
    G --> H
```

---

## 📂 Repository Structure

```text
ai-cinema-lab/
├── README.md
├── AI-CINEMA-PIPELINE.md
├── docs/
│   ├── architecture.md
│   ├── finops.md
│   └── roadmap.md
├── campaigns/
├── assets/
├── render_movie.py
└── config.json
```

---

## 💰 FinOps

AI Cinema Lab incorporates cost governance into creative workflows.

Examples:

- Budget thresholds
- Asset reuse
- Controlled rendering
- Cost attribution
- Future cost dashboards

---

## 🚀 Long-Term Vision

Build an AI-native media production platform that applies:

- Platform Engineering
- DevOps
- FinOps
- Generative AI

to transform content creation into a scalable, observable, and repeatable production system.

---

## 🧪 Current Campaigns

### R&JC FundaCerveza

First commercial campaign developed within AI Cinema Lab.

---

## 🎓 Lessons Learned

Our first AI-generated commercial exceeded the initial rendering budget by **150%**.

What started as a simple product advertisement quickly became an unexpected FinOps exercise:

- Budget configured: **$10 USD**
- Actual cost: **$296.60 MXN**
- Root cause: aggressive experimentation with Vertex AI Veo video generation
- Mitigation: stop cloud rendering workloads and move post-production to local tooling using MoviePy

This incident became the foundation of the project's FinOps governance model and reinforced a key principle:

> Every AI pipeline eventually becomes a FinOps problem.

Or, stated differently:

> We accidentally spent almost 300 pesos teaching a silicone beer sleeve how to become a movie star. 🎬🍺

---

## 📜 License

This repository is intended for experimentation, learning, and AI-powered media production research.