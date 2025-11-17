AmbedkarGPT Intern QA System
🎯 Overview
AmbedkarGPT is a fully local, command-line AI that answers questions about a speech by Dr. B.R. Ambedkar.
It demonstrates a simple but modern Retrieval-Augmented Generation (RAG) pipeline using 📦 LangChain, 🔎 ChromaDB, 🤗 HuggingFace, and 🦙 Ollama/Mistral—all 100% free, with no API keys or logins required.

✨ Key Features
RAG Workflow: End-to-end retrieval augmented generation, all local.

ChromaDB Vector Store: Stores and retrieves semantic embeddings efficiently.

HuggingFace MiniLM Embeddings: Transforms text for precise chunk-level search.

Local LLM (Mistral 7B): Private LLM inference using Ollama.

Zero Cloud Dependency: No paid APIs, no accounts, no internet needed after setup.

🏗️ Architecture
text
┌─────────────┐        ┌──────────────┐        ┌─────────────┐
│ speech.txt  │─→[splitter]─→│ Embedding DB │─→[retriever]─→│    LLM/QA    │
└─────────────┘        └──────────────┘        └─────────────┘
      ↑                                              │
      └───────[user questions & answers]─────────────┘
🚀 Getting Started
Prerequisites
Python 3.8+

Ollama (https://ollama.com/download)

Mistral LLM via Ollama (ollama pull mistral)

Installation
Clone the repository:

bash
git clone https://github.com/mahika29/AmbedkarGPT-Intern-Task.git
cd AmbedkarGPT-Intern-Task
Create and activate a virtual environment:

Windows:

bash
python -m venv venv
.\venv\Scripts\activate
Mac/Linux:

bash
python3 -m venv venv
source venv/bin/activate
Install Python dependencies:

bash
pip install -r requirements.txt
Make sure you have pulled the Mistral model:

bash
ollama pull mistral
Running the Application
bash
python main.py
Type your questions at the prompt and get answers directly from the Ambedkar speech provided.

📁 Project Structure
text
AmbedkarGPT-Intern-Task/
├── main.py              # Main pipeline code
├── requirements.txt     # Required Python packages
├── speech.txt           # Source text being queried
└── README.md            # This documentation
💡 Example Questions
What does Ambedkar say is the real remedy for caste?

Why must belief in the shastras be challenged?

How does the passage describe “social reform”?

🛠️ Troubleshooting
Slow answers: Local LLM inference takes time. Performance depends on your hardware.

Ollama issues: Ensure Ollama is installed, in PATH, and running (restart your terminal if needed).

Dependency warnings: LangChain deprecation notes can be ignored if the code runs.

📜 Assignment Compliance
Single-file command-line QA app.

NO API keys, accounts, or paid services.

Core pipeline: LangChain, ChromaDB, HuggingFace, and Ollama/Mistral only.

All logic and requirements clearly documented for reviewers.

👤 Maintainer
MAHIKA HARIKUMAR 
Email: mahikaharikumar29@gmail.com

Open an issue if you need help or have suggestions!
