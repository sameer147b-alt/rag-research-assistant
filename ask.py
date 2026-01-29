import os
from dotenv import load_dotenv

from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from groq import Groq

# -----------------------------
# Load environment variables
# -----------------------------
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise RuntimeError("GROQ_API_KEY not found in .env")

client = Groq(api_key=GROQ_API_KEY)

# -----------------------------
# Embeddings
# -----------------------------
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# -----------------------------
# Load FAISS index
# -----------------------------
db = FAISS.load_local(
    "faiss_index",
    embeddings,
    allow_dangerous_deserialization=True
)

retriever = db.as_retriever(search_kwargs={"k": 5})

# -----------------------------
# System Prompt (your logic B)
# -----------------------------
SYSTEM_PROMPT = """
You are a document-based question answering assistant.

Rules:
1. Answer primarily using the provided context.
2. If the answer is NOT explicitly stated in the document:
   - Still give the best possible answer inferred from context
   - Clearly mention: "This is not explicitly stated in the document."
3. Do NOT hallucinate facts beyond reasonable inference.
4. Be concise and precise.
"""

print("\nDocument Q&A ready. Type 'exit' to quit.\n")

# -----------------------------
# Ask Loop
# -----------------------------
while True:
    query = input("Question: ").strip()

    if query.lower() in {"exit", "quit"}:
        print("Exiting.")
        break

    # 🔹 Retrieve documents (UPDATED API)
    docs = retriever.invoke(query)

    if not docs:
        context = "No relevant context found in the document."
    else:
        context = "\n\n".join(d.page_content for d in docs)

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {
            "role": "user",
            "content": f"""
Context:
{context}

Question:
{query}
"""
        }
    ]

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages,
        temperature=0.2,
    )

    print("\n--- ANSWER ---")
    print(response.choices[0].message.content.strip())
    print("----------------\n")
