🚀 AmbedkarGPT — Local RAG QA System (Intern Task)

A fully local Retrieval-Augmented Generation pipeline for querying Dr. B.R. Ambedkar’s speech.

✨ Overview

AmbedkarGPT is a command-line intelligent QA system built entirely with local, offline tools.
It demonstrates a modern RAG (Retrieval-Augmented Generation) workflow using:

🧠 Local LLM: Mistral 7B via Ollama

🔎 ChromaDB: High-performance vector database

📦 LangChain: Modular RAG pipeline framework

🤗 HuggingFace MiniLM: Lightweight, accurate embedding model

All components run 100% locally, with no paid APIs, no tokens, and no internet needed after setup.

🔥 Key Features

⚙️ Full Local RAG Pipeline
End-to-end question answering over the provided speech text.

🧩 Efficient Text Splitting & Embedding
Uses MiniLM embeddings for high-quality semantic search.

🗂️ Chroma Vector Store
Stores and retrieves text chunks with fast cosine similarity search.

🤖 Private Local LLM (Mistral 7B)
via Ollama, ensuring fast and fully offline inference.

🛑 Zero Cloud Dependency
No OpenAI, no HuggingFace API, no accounts required.

🏗️ Architecture
┌─────────────┐        ┌────────────────┐        ┌────────────┐
│ speech.txt  │ ──→ [ Text Splitter ] ──→ │ Embedding DB  │ ──→ [ Retriever ] ──→ [ LLM QA ]
└─────────────┘        └────────────────┘        └────────────┘
                                      ↑
                                      │
                     └────── User Questions & Answers ───────┘

📥 Installation & Setup
✅ Prerequisites

Python 3.8+

Ollama installed → https://ollama.com/download

Mistral LLM pulled locally:

ollama pull mistral

🧰 Setup Instructions
1️⃣ Clone the Repository
git clone https://github.com/mahika29/AmbedkarGPT-Intern-Task.git
cd AmbedkarGPT-Intern-Task

2️⃣ Create Virtual Environment
Windows:
python -m venv venv
.\venv\Scripts\activate

Mac / Linux:
python3 -m venv venv
source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run the Application
python main.py


Start asking questions like:

“What does Ambedkar say is the remedy for caste?”

“Why must belief in the shastras be challenged?”

🗂️ Project Structure
AmbedkarGPT-Intern-Task/
│
├── main.py           # Main RAG pipeline logic
├── speech.txt        # The source speech for QA
├── requirements.txt  # Python dependencies
└── README.md         # Project documentation

💡 Example Queries

Try asking:

“What is Ambedkar’s view on caste as a social system?”

“How does the speech define social reform?”

“Why is challenging scripture important according to Ambedkar?”

🛠️ Troubleshooting
Issue	Solution
⏳ Slow answers	Local LLMs depend on CPU/GPU power
❌ Ollama not recognized	Restart terminal; ensure Ollama is installed & running
⚠️ LangChain warnings	Safe to ignore if the app works
🧠 Mistral not found	Run: ollama pull mistral
📜 Assignment Requirements – Verified

✔️ Single-file command-line QA app
✔️ Local RAG pipeline with LangChain + ChromaDB
✔️ HuggingFace MiniLM embeddings
✔️ Local LLM using Ollama/Mistral
✔️ No APIs, no cloud, no paid services
✔️ Clean and complete documentation

👤 Maintainer

MAHIKA HARIKUMAR
📧 Email: mahikaharikumar29@gmail.com

If you encounter issues or want to suggest improvements, feel free to open an issue.
