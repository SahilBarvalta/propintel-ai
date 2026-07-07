<div align="center">

# 🏠 PropIntel AI

### AI-powered Property Intelligence Platform

Helping investors discover and evaluate Dubai real estate opportunities using AI-powered recommendations, Retrieval-Augmented Generation (RAG), and structured property intelligence.

> ⚠️ **Technology Preview**  
> This project uses **synthetically generated property data** for demonstration purposes only and is **not connected to live real estate listings**.

---

![Python](https://img.shields.io/badge/Python-3.14-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Web_App-red)
![Gemini](https://img.shields.io/badge/Google-Gemini_2.5_Flash-blue)
![RAG](https://img.shields.io/badge/RAG-Implemented-success)
![License](https://img.shields.io/badge/Status-Portfolio_Project-green)

</div>

---

# 🚀 Live Demo

**Application**

> _Add your Streamlit URL here_

```
https://YOUR-APP.streamlit.app
```

---

# 📖 Overview

PropIntel AI is an AI-powered property intelligence platform built to demonstrate how Large Language Models (LLMs), Retrieval-Augmented Generation (RAG), recommendation engines, and structured business logic can support real estate investment decisions.

Unlike traditional AI chatbots, PropIntel AI grounds every recommendation using a structured property database before generating AI insights, significantly reducing hallucinations and improving recommendation quality.

This project was built as an AI Product Management portfolio project to demonstrate end-to-end product thinking—from ideation and MVP development to deployment.

---

# ✨ Features

### 🤖 AI Investment Advisor

- Personalized investment recommendations
- Gemini 2.5 Flash integration
- Context-aware AI responses

### 🧠 Retrieval-Augmented Generation (RAG)

- CSV-based property retrieval
- Grounded AI responses
- No fabricated property recommendations

### 📊 Recommendation Engine

- Budget filtering
- Risk filtering
- Community filtering
- Property type filtering
- Investment scoring algorithm

### 🏘 Synthetic Property Dataset

- 2,000+ generated property listings
- 10 Dubai communities
- 20 developers
- ROI
- Rental Yield
- Expected Appreciation
- Investment Risk
- Developer Information

### 🎯 Product Management Focus

Designed as a real-world AI product rather than a chatbot prototype.

---

# 🏗 Architecture

```
Investor

        │

        ▼

 Streamlit Web UI

        │

        ▼

Investment Preferences

        │

        ▼

Property Retrieval (RAG)

        │

        ▼

Matching Property Dataset

        │

        ▼

Prompt Engineering

        │

        ▼

Gemini 2.5 Flash

        │

        ▼

Structured Recommendation

        │

        ▼

Interactive Dashboard
```

---

# ⚙ Technology Stack

| Category | Technology |
|-----------|------------|
| Language | Python |
| UI | Streamlit |
| AI Model | Gemini 2.5 Flash |
| AI SDK | google-genai |
| Knowledge Base | CSV Dataset |
| AI Technique | Retrieval-Augmented Generation (RAG) |
| Version Control | Git & GitHub |
| Deployment | Streamlit Community Cloud |

---

# 📂 Project Structure

```
propintel-ai/

│
├── app.py
├── config.py
├── requirements.txt
├── README.md
├── .env.example
│
├── services/
│   ├── gemini_service.py
│   ├── rag_service.py
│   └── prompt_service.py
│
├── prompts/
│   └── advisor.txt
│
├── scripts/
│   ├── generate_dataset.py
│   ├── dataset_config.py
│   └── name_generator.py
│
├── data/
│   ├── properties.csv
│   ├── communities.csv
│   ├── developers.csv
│   └── investment_terms.csv
```

---

# 🧠 AI Workflow

1. User enters investment preferences.
2. The recommendation engine filters the property dataset.
3. Matching properties are ranked using an Investment Score.
4. Retrieved properties are injected into the AI prompt.
5. Gemini generates grounded recommendations.
6. Results are displayed in the dashboard.

---

# 📈 Investment Score

Each property is ranked using deterministic business rules before AI reasoning.

Current scoring factors include:

- ROI
- Rental Yield
- Expected Appreciation
- Investment Risk

This separates business logic from AI reasoning and improves recommendation consistency.

---

# 🛡 Prompt Engineering

PropIntel AI uses a structured system prompt that instructs the AI to:

- Act as a Dubai property investment advisor
- Recommend only retrieved properties
- Avoid hallucinations
- Never guarantee investment returns
- Explain risks
- Provide transparent reasoning

---

# 🔒 Security

Sensitive information is never committed to GitHub.

The application uses:

- `.env` for local development
- `.env.example` as a template
- Streamlit Secrets for cloud deployment

---

# 🚀 Running Locally

Clone the repository

```bash
git clone https://github.com/SahilBarvalta/propintel-ai.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create `.env`

```
GEMINI_API_KEY=YOUR_API_KEY
```

Run

```bash
streamlit run app.py
```

---

# 🛣 Roadmap

### ✅ Version 0.7

- Gemini Integration
- Streamlit Dashboard
- RAG
- Recommendation Engine
- Synthetic Dataset Generator
- Deployment
- GitHub

### 🚧 Version 0.8

- Community Comparison
- Analytics Dashboard
- Interactive Charts

### 🚧 Version 0.9

- PDF Investment Report
- Mortgage Calculator
- Market Insights

### 🚧 Version 1.0

- Database Integration
- Authentication
- Vector Search
- Embeddings
- Production APIs

---

# 📚 Key AI Concepts Demonstrated

- Large Language Models (LLMs)
- Prompt Engineering
- Retrieval-Augmented Generation (RAG)
- Recommendation Systems
- Structured AI Outputs
- Synthetic Data Generation
- Grounded AI Responses

---

# 👨‍💻 About

**Sahil Barvalta**

Senior Product Manager | AI | PropTech | Growth

PropIntel AI was built as a portfolio project to demonstrate AI product strategy, recommendation systems, LLM integration, and modern AI application development.

---

## ⭐ If you found this project interesting

Consider giving it a ⭐ on GitHub.
