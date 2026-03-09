# AI Agent (Python)

Simple AI agent built in Python to experiment with different Large Language Model (LLM) providers.

This project was created as a learning exercise while studying software development. The goal was to explore how an AI agent can interact with different APIs and local models.

## Project Structure

```
AI_Agent
│
├── data/
│   └── tasks.py        # Example tasks for the agent
│
├── src/
│   ├── agent.py        # Agent using OpenAI API
│   ├── agent_hf.py     # Agent using HuggingFace inference
│   └── agent_oll.py    # Agent using Ollama (local LLM)
│
├── main.py             # Entry point of the program
├── requirements.txt    # Python dependencies
├── .gitignore
└── README.md
```

## Experiments

During development several approaches were tested:

- OpenAI API
- HuggingFace Inference API
- Ollama (local LLM)

The final working implementation uses **Ollama with Llama3 running locally**.

The other agents were kept in the repository to document the experimentation process.

## Setup

### 1 Install dependencies

```bash
pip install -r requirements.txt
```

### 2 Install Ollama

Download and install Ollama:

https://ollama.com

### 3 Download the model

```bash
ollama pull llama3
```

### 4 Run the project

```bash
python main.py
```

## Requirements

Python 3.10+

Libraries used:

- python-dotenv
- ollama
- requests

## Purpose

This project was created for learning purposes while studying **DAM (Multiplatform Application Development)** and experimenting with AI tools and APIs.

The main goals were:

- Learn how to interact with LLM APIs
- Experiment with local AI models
- Practice project structure in Python
- Understand basic AI agent workflows

## Author

Maria del Mar Clara Gómez