# Context-Aware Role-Based Chatbot

This is a role-based AI chatbot built with **Streamlit**, **LangChain**, and **MongoDB**. It supports dynamic roles like Engineer and Doctor using YAML templates and maintains conversation history using MongoDB to provide contextual responses.

---

## Features

- Role-based prompt design (Engineer, Doctor, etc.)
- Prompts defined in `templates/prompts.yaml`
- Stores chat history in MongoDB
- Uses last 10 messages as context
- Integrates LangChain + deepseek-r1
- Web interface built with Streamlit

---

## Application Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/your-chatbot-project.git

### 2. Create virtual environment

```bash
python -m venv venv

### 1. Clone the repository

```bash
git clone https://github.com/your-username/your-chatbot-project.git
