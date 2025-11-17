AmbedkarGPT-Intern-Task
Welcome!
This repo contains the code and setup for my AI Intern RAG QA assignment (Kalpit Pvt Ltd).
It’s designed to answer questions based only on the provided Ambedkar speech excerpt, all running locally and easily set up on any machine.

What does this do?
Loads the provided speech.txt from Dr. B.R. Ambedkar.

Splits the text into chunks for smarter searching.

Turns those chunks into vector embeddings (using HuggingFace).

Stores the vectors locally using ChromaDB.

Uses LangChain to retrieve relevant chunks and answer your questions with the Mistral 7B LLM running in Ollama.

No external APIs, no accounts, and no hidden costs.

Quick Setup
You’ll need:

Python 3.8 or newer

Ollama (installed locally)

Mistral 7B model downloaded with Ollama

Step 1. Clone this repo:

bash
git clone https://github.com/<your-username>/AmbedkarGPT-Intern-Task.git
cd AmbedkarGPT-Intern-Task
Step 2. Start a Python virtual environment:

bash
python -m venv venv
# Activate:
# On Windows:
.\venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
Step 3. Install requirements:

bash
pip install -r requirements.txt
Step 4. Make sure Ollama is installed and the Mistral model is pulled:

bash
ollama pull mistral
Step 5. Run the app:

bash
python main.py
How to use
Type any question about the provided speech excerpt at the prompt.

Example questions:

What is Ambedkar’s remedy for caste?

Why does Ambedkar challenge the shastras?

What analogy is used for social reform?

To exit, just type exit!

Troubleshooting
It’s a little slow? Local LLM inference isn't instant, especially on normal laptops. No worries—it's expected!

Ollama not found? Double-check your PATH and restart the terminal after installing Ollama.

Dependency warnings? You might see LangChain deprecation notes—ignore these, as the code still works and meets the assignment brief.

What’s inside?
main.py — Complete QA pipeline, with helpful comments so you can see what each part does.

speech.txt — The actual text source (Ambedkar speech excerpt).

requirements.txt — All Python libraries you’ll need.

README.md — This guide.

Assignment details
Built as per the Kalpit Pvt Ltd AI Intern assignment brief.
All processing runs locally, and answers are always grounded in the provided text.

If you have any questions, drop me a message or an issue in the repo!
Thanks for checking out the project — hope you enjoy testing it.
