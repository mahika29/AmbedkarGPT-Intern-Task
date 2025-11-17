🚀 AmbedkarGPT — Local RAG QA System (Intern Task)

AmbedkarGPT is a fully local command-line QA system demonstrating a modern Retrieval-Augmented Generation (RAG) pipeline for asking intelligent questions about a speech by Dr. B. R. Ambedkar.

Runs 100% offline, using only free and local tools.

✨ Overview

AmbedkarGPT uses:

🧠 Local LLM (Mistral 7B) via Ollama

🔎 ChromaDB for vector search

🤗 HuggingFace MiniLM Embeddings

📦 LangChain for the pipeline

📝 speech.txt as the knowledge base

No API keys, no cloud calls, no paid services.

🔥 Features

Full RAG workflow (chunk → embed → store → retrieve → answer)

Local, private inference with Mistral

Fast semantic search using ChromaDB

Simple CLI for querying Ambedkar's speech

🏗 Architecture Diagram
┌───────────────┐      ┌────────────────┐      ┌───────────────┐
│   speech.txt   │ ---> │ Text Splitter  │ ---> │ Embedding DB  │
└───────────────┘      └────────────────┘      └───────────────┘
                                                           │
                                                           ▼
                                                    ┌──────────────┐
                                                    │  LLM (QA)     │
                                                    └──────────────┘
                                                           ▲
                                      └────── User Questions ──────┘

📥 Installation & Setup

Follow these steps in order.
(All code blocks include GitHub’s copy button, so you can copy easily.)

1️⃣ Clone Repository
git clone https://github.com/mahika29/AmbedkarGPT-Intern-Task.git
cd AmbedkarGPT-Intern-Task

2️⃣ Create and Activate Virtual Environment
Windows:
python -m venv venv
.\venv\Scripts\activate

macOS / Linux:
python3 -m venv venv
source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Install Mistral Model (via Ollama)

Make sure Ollama is installed.

ollama pull mistral

5️⃣ Run the Application
python main.py


Now just ask questions like:

"What does Ambedkar say about social reform?"

"Why must belief in the shastras be challenged?"

"What is his remedy for caste?"

🗂 Project Structure
File / Folder	Description
main.py	Core RAG pipeline & CLI loop
speech.txt	Source document for Q&A
requirements.txt	Python packages needed
README.md	Full documentation
💡 Example Questions

Try asking:

“What does the speech say about caste discrimination?”

“How does Ambedkar define real reform?”

“Why does Ambedkar reject scriptural authority?”

🛠 Troubleshooting
Issue	Fix
❌ Ollama: command not found	Install Ollama & restart terminal
🧠 Model not loading	Run ollama pull mistral
🐌 Slow answers	Local inference depends on CPU/GPU power
⚠️ LangChain deprecation warnings	Safe to ignore
📜 Assignment Requirements (All Met ✔)
Requirement	Status
Single-file CLI app	✔
Uses LangChain	✔
Uses ChromaDB	✔
Uses HuggingFace MiniLM	✔
Uses local model via Ollama	✔
No paid APIs	✔
👤 Maintainer

Mahika Harikumar
📧 Email: mahikaharikumar29@gmail.com

Feel free to open an issue for help or suggestions!
