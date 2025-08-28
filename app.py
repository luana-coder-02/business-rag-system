import streamlit as st
from datasets import load_dataset
from sentence_transformers import SentenceTransformer
from chromadb import PersistentClient
import ollama
import json
from datetime import datetime
import os

MODEL = "mistral:latest"
openai = ollama.OpenAI(
    base_url="http://localhost:11434/v1",
    api_key=os.environ.get("OLLAMA_API_KEY")
)

dataset = load_dataset("aumghag/Data-Analytics-Digital-Marketing-Project-Management-QA_DB")
train_data = dataset["train"]

texts = []
metadatas = []

for item in train_data:
    question = item["question"]
    answer = item["answer"]
    texts.append(f"Q: {question}\nA: {answer}")
    metadatas.append({"source": "commercial_dataset"})

model_emb = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = model_emb.encode(texts, convert_to_numpy=True)

persist_dir = "chroma_db"
client = PersistentClient(path=persist_dir)

collection_names = [c.name for c in client.list_collections()]
if "commercial_qa" in collection_names:
    collection = client.get_collection("commercial_qa")
else:
    collection = client.create_collection("commercial_qa")

if len(collection.get()["ids"]) == 0:
    collection.add(
        documents=texts,
        embeddings=embeddings.tolist(),
        metadatas=metadatas,
        ids=[str(i) for i in range(len(texts))]
    )
    print(f"✅ {len(texts)} documentos indexados en chroma_db")
else:
    print(f"📚 La colección ya tiene {len(collection.get()['ids'])} documentos.")

LOG_FILE = "chat_log.jsonl"
user_histories = {}

def log_interaction_jsonl(question, answer, context_docs=None, user_id="unknown"):
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "user_id": user_id,
        "question": question,
        "answer": answer,
        "context_docs": context_docs
    }
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(log_entry, ensure_ascii=False) + "\n")

def rag_answer(question, user_id, k=3, history_rounds=3):
    if user_id not in user_histories:
        user_histories[user_id] = []

    chat_log = user_histories[user_id]

    results = collection.query(
        query_texts=[question],
        n_results=k,
        include=["documents", "metadatas"]
    )
    relevant_texts = results["documents"][0]
    context = "\n\n".join(relevant_texts)

    history_text = ""
    for turn in chat_log[-history_rounds:]:
        history_text += f"User: {turn['question']}\nAssistant: {turn['answer']}\n"

    prompt = f"""You are an expert assistant in analytics, digital marketing, and project management.
Use ONLY the context below to answer clearly and accurately.
If the answer is not in the context, say 'I don't know'.

Context:
{context}

Conversation history:
{history_text}

New question:
{question}

Answer clearly and concisely based ONLY on the context above.
"""

    response = ollama.chat(
        model="mistral:latest",
        messages=[
            {"role": "system", "content": "You are a helpful and precise business assistant."},
            {"role": "user", "content": prompt}
        ]
    )

    answer = response['message']['content'].strip()
    log_interaction_jsonl(question, answer, context_docs=relevant_texts, user_id=user_id)

    chat_log.append({"question": question, "answer": answer})
    user_histories[user_id] = chat_log

    return answer

st.title("💼 Commercial RAG Chat")

user_id = st.text_input("Enter your user ID:")

if user_id:
    st.write(f"Welcome, **{user_id}**! Ask questions below:")

    question = st.text_input("Your question:")

    if st.button("Ask") and question:
        answer = rag_answer(question, user_id)
        st.success(answer)

    # Mostrar historial del usuario
    if user_id in user_histories and user_histories[user_id]:
        st.subheader("📜 Conversation history")
        for i, turn in enumerate(user_histories[user_id][::-1]):
            with st.expander(f"Q{i+1}: {turn['question']}", expanded=False):
                st.write(turn['answer'])
