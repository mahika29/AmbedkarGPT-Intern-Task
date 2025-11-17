from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import Ollama
from langchain.chains import RetrievalQA


# 1. Load speech text
with open("speech.txt", "r", encoding="utf-8") as f:
    text = f.read()

# 2. Split text into chunks
splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
docs = splitter.split_text(text)
print(f"Loaded {len(docs)} chunks.")

# 3. Generate embeddings and store in local ChromaDB
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
db = Chroma.from_texts(docs, embedding=embeddings, persist_directory="chroma_db")
print("Embeddings created and stored in ChromaDB.")

# 4. Create retriever and LLM wrapper for Mistral via Ollama
retriever = db.as_retriever(search_kwargs={"k": 3})
llm = Ollama(model="mistral")

# 5. Create the RetrievalQA chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    return_source_documents=True
)

# 6. Command-line QA loop
while True:
    query = input("\nAsk a question (or type 'exit' to quit): ")
    if query.strip().lower() == "exit":
        break
    result = qa_chain(query)
    print("\nAnswer:", result["result"])
