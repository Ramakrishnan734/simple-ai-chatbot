# Simple AI Chatbot

A stateful AI chatbot built with LangGraph and served via FastAPI. Supports multiple users simultaneously with isolated conversation memory per session.

## What it does

- Remembers conversation history across turns using LangGraph checkpointer
- Supports multiple users simultaneously — each with their own isolated memory
- Exposes a clean REST API via FastAPI
- Powered by Groq's Llama 3 (free)

## Tech Stack

- **LangGraph** — stateful agent framework
- **LangChain** — LLM tooling
- **Groq (Llama 3.3 70B)** — free LLM API
- **FastAPI** — REST API framework
- **Uvicorn** — ASGI server

## Project Structure

```
simple-ai-chatbot/
├── chatbot.py      # LangGraph brain — state, nodes, edges, checkpointer
├── main.py         # FastAPI layer — exposes /chat endpoint
└── .env            # API keys (not committed)
```

## Setup

1. Clone the repo
```bash
git clone https://github.com/Ramakrishnan734/simple-ai-chatbot.git
cd simple-ai-chatbot
```

2. Create and activate virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies
```bash
pip install langgraph langchain-groq fastapi uvicorn python-dotenv
```

4. Add your Groq API key
```bash
echo "GROQ_API_KEY=your_key_here" > .env
```
Get a free API key at [console.groq.com](https://console.groq.com)

## Run

**As a REST API (FastAPI):**
```bash
uvicorn main:app --reload
```
Visit `http://127.0.0.1:8000/docs` for the Swagger UI.

**As a terminal chatbot:**
```bash
python chatbot.py
```

## API Usage

**Endpoint:** `POST /chat`

**Request:**
```json
{
  "message": "my name is RK",
  "thread_id": "user-1"
}
```

**Response:**
```json
{
  "response": "Hi RK, nice to meet you! How can I help you today?"
}
```

## How Memory Works

Each `thread_id` maps to an isolated conversation checkpoint in LangGraph. This means:
- `user-1` and `user-2` have completely separate conversation histories
- Each user can resume their conversation anytime using the same `thread_id`

## Author

Ramakrishnan — [github.com/Ramakrishnan734](https://github.com/Ramakrishnan734)
