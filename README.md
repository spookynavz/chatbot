# Context-Aware Role-Based Chatbot

This is a role-based AI chatbot built with **Streamlit**, **LangChain**, and **MongoDB**. It supports dynamic roles like Engineer and Doctor using YAML templates and maintains conversation history in MongoDB to provide contextual responses using LangChain and LLMs.

---

## Features

- Role-based character chat (Engineer, Doctor, etc.)
- Prompts defined using `templates/prompts.yaml`
- Uses MongoDB to store last 10 chat messages per session
- Automatically passes conversation history as context
- Built using Streamlit for a web interface
- Integrated with LangChain + deepseek-r1
---

## Application Installation

| Step | Command |
|------|---------|
| Clone the repository | `git clone https://github.com/your-username/your-chatbot-project.git` |
| Navigate to project directory | `cd your-chatbot-project` |
| Create virtual environment | `python -m venv venv` |
| Activate environment (Windows) | `venv\Scripts\activate` |
| Activate environment (macOS/Linux) | `source venv/bin/activate` |
| Install dependencies | `pip install -r requirements.txt` |
| Install MongoDB (if not installed) | [MongoDB Installation Guide](https://www.mongodb.com/docs/manual/installation/) |

---

## Startup Apps

| Task | Command |
|------|---------|
| Start MongoDB server | `mongod` |
| Run the chatbot web app | `streamlit run main.py` |
| Access the app | Open `http://localhost:8501` in your browser |

---

## Requirements

streamlit pymongo langchain openai pyyaml.


