# 🤖 AI Dev Assistant — AI-First Engineering Copilot

An end-to-end AI-powered developer assistant that combines **RAG (Retrieval-Augmented Generation)**, **LLM orchestration**, and an **agentic workflow layer** to help engineers debug, understand, and improve codebases faster.

---

## 🚀 Features

### 🧠 AI Agent (Core)

* Intelligent query classification (`fix`, `tests`, `architecture`, `general`)
* Multi-step reasoning workflows
* Dynamic routing across specialized pipelines

### 🔍 RAG over Codebase

* Semantic search over code and documentation
* Context-aware responses
* FAISS vector database for fast retrieval

### 🛠 Developer Tools

* 🔧 Bug fixing suggestions
* 🧪 Automated test generation
* 🏗 Architecture explanation
* 💬 General Q&A

### 🌐 SaaS-style UI

* ChatGPT-like interface
* Multi-tool sidebar
* File upload + code editor
* GitHub repo input
* Streaming responses
* Dark/Light mode

---

## 🏗 Architecture

```text
Streamlit UI
    ↓
FastAPI Backend
    ↓
Agent Layer (Decision Engine)
    ↓
RAG Service (FAISS)
    ↓
LLM Service (OpenAI / Ollama)
```

---

## ⚙️ Tech Stack

### Backend

* FastAPI
* Python 3.11
* LangChain
* FAISS
* OpenAI / Ollama (LLMs)

### Frontend

* Streamlit

### AI Concepts

* Retrieval-Augmented Generation (RAG)
* Agentic Workflows
* Prompt Engineering
* LLM Orchestration

---

## 📦 Project Structure

```text
ai-dev-assistant/
│
├── app/
│   ├── api/              # FastAPI routes
│   ├── services/         # RAG, LLM, Agent logic
│   ├── models.py         # Request schemas
│   ├── main.py           # App entry point
│
├── ui.py                 # Streamlit UI
├── repo/                 # Sample codebase (for RAG)
├── .env                  # API keys
```

---

## 🚀 Getting Started

### 1️⃣ Clone Repo

```bash
git clone <your-repo-url>
cd ai-dev-assistant
```

---

### 2️⃣ Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Add Environment Variables

Create `.env`:

```env
OPENAI_API_KEY=your_api_key_here
```

---

### 5️⃣ Run Backend

```bash
uvicorn app.main:app --reload
```

---

### 6️⃣ Run UI

```bash
streamlit run ui.py
```

---

## 🧪 Example Use Cases

### 🔧 Fix Bugs

> "Fix authentication issue in this code"

### 🧪 Generate Tests

> "Write unit tests for login function"

### 🏗 Explain Architecture

> "Explain how routing works in this project"

### 🤖 Agent Mode

> Automatically decides the best workflow based on query

---

## 🧠 Key Highlights

* Built an **AI-first engineering system**
* Designed **agentic orchestration layer**
* Integrated **RAG + LLM pipelines**
* Developed **multi-modal UI (chat + tools + code input)**
* Supports **real-world developer workflows**

---

## 🎯 Future Improvements

* GitHub repo auto-ingestion
* Real-time codebase indexing
* Multi-file understanding
* Team collaboration features
* CI/CD integration

---

## 👨‍💻 Author

Yogesh Yadav
LinkedIn: https://www.linkedin.com/in/yogesh-y-a8a41b36/ 
GitHub: https://github.com/yogeshy13/

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!
# AI-Developer-Assistant
Helping developers to review code, generate test cases and help business to get to know the code
