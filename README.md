# AmbedkarGPT Intern QA System

## 📚 Project Summary

Welcome!  
AmbedkarGPT is a command-line QA app answering questions about a classic Dr. B.R. Ambedkar speech, entirely offline. Built for the Kalpit Pvt Ltd AI Intern assignment, it showcases a simple RAG pipeline in Python.


🚀 How It Works
Loads the speech.txt excerpt.

Splits the text into manageable chunks.

Creates meaningful embeddings using HuggingFace sentence-transformers.

Stores those embeddings locally in ChromaDB.

Finds the best context chunks for any question.

Uses the Mistral 7B LLM in Ollama to answer, always grounded in the original text.

🗂️ Repo Structure
main.py — All core logic (well-commented and readable)

speech.txt — The QA source text (Ambedkar speech excerpt)

requirements.txt — All dependencies for setup

README.md — That’s this file!

⚙️ Quick Setup Guide
1. Get Python & Ollama
You’ll need Python 3.8+ (recommended: latest), and Ollama installed.

2. Pull Mistral LLM
Open a terminal and run:

bash
ollama pull mistral
Start Ollama if not running (ollama run mistral should reply!).

3. Clone & Install
Clone the repo and enter its folder:

bash
git clone https://github.com/mahika29/AmbedkarGPT-Intern-Task.git
cd AmbedkarGPT-Intern-Task
Spin up a virtual Python environment:

bash
python -m venv venv
# Windows:
.\venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
Install all requirements:

bash
pip install -r requirements.txt
4. Run the QA App
Just:

bash
python main.py
Type any question about the speech!

💻 Example Usage
text
Ask a question (or type 'exit' to quit): What is Ambedkar’s remedy for caste?
Answer: According to Ambedkar, the real remedy for caste is to destroy the belief in the sanctity of the shastras...
Ask followups, or exit when you’re done.

💬 Common Issues & Tips
Slow to answer?
Local LLMs like Mistral take a few seconds per answer (your hardware matters).

Error about Ollama?
Make sure you installed Ollama AND restarted your terminal so the command is found.

Deprecation or warning messages?
Ignore these—the app works and meets the assignment brief.

🎯 Assignment Details
All code, embeddings, and answering are strictly local.

You never need an API key, login, or payment.

Answers are based only on speech.txt content.

🤝 Need help?
Open an issue on GitHub, or contact by email (mahikaharikuamr29@gmail.com).
Feedback is always welcome!

Thanks for reviewing and testing AmbedkarGPT!
Built for reproducibility, clarity, and easy code review.
