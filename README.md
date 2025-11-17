AmbedkarGPT Intern QA System
📚 Project Overview
AmbedkarGPT lets you ask questions about a speech excerpt from Dr. B.R. Ambedkar and get answers using a Retrieval-Augmented Generation pipeline—everything local and free.

🚀 How It Works
Loads the provided speech.txt excerpt

Splits the passage into manageable chunks

Creates embeddings from each chunk using HuggingFace sentence-transformers

Stores embeddings locally in ChromaDB

Finds best context chunks for your question

Uses the Mistral 7B LLM via Ollama for accurate, text-grounded answers

🗂️ Repository Contents
main.py – Main app logic, with comments

requirements.txt – List of dependencies

speech.txt – Source speech excerpt

⚙️ Setup Guide
1. Prerequisites
Python 3.8+

Ollama (installed locally)

Mistral 7B model downloaded

2. Installation
bash
git clone https://github.com/mahika29/AmbedkarGPT-Intern-Task.git
cd AmbedkarGPT-Intern-Task
Create and activate your Python environment:

Windows

bash
python -m venv venv
.\venv\Scripts\activate
Mac/Linux

bash
python3 -m venv venv
source venv/bin/activate
Install dependencies:

bash
pip install -r requirements.txt
Pull the Mistral model in Ollama:

bash
ollama pull mistral
3. Running the App
bash
python main.py
You’ll see a prompt — just ask any question about the speech excerpt!

💡 Example Usage
text
Ask a question (or type 'exit' to quit): What does Ambedkar say is the remedy for caste?
Answer: According to Ambedkar, the remedy is to destroy belief in the sanctity of the shastras...
🛠️ Common Issues
LLM answers are slow: Local inference takes a few seconds per question; depends on your PC.

Ollama not found: Make sure it’s installed and in PATH; restart terminal if needed.

Warnings: You may see library deprecation warnings—ignore these, the code works.

🎯 Assignment Brief
This project fulfills the Kalpit Pvt Ltd AI Intern requirements:

Retrieval-based answering from a provided text file

Uses LangChain, ChromaDB, HuggingFace, and local LLM (Mistral 7B) via Ollama

No API keys or external services required

🤝 Need Help?
Open an issue in the GitHub repo or contact me at mahikaharikumar29@gmail.com!

Thanks for reviewing and testing AmbedkarGPT!
