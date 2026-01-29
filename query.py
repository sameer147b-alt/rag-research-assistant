from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import Ollama

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough


# 1. Load embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# 2. Load FAISS index
vectorstore = FAISS.load_local(
    "faiss_index",
    embeddings,
    allow_dangerous_deserialization=True
)

retriever = vectorstore.as_retriever(search_kwargs={"k": 5})

# 3. Load local LLM via Ollama
llm = Ollama(model="llama3")

# 4. Prompt (THIS FIXES YOUR RANDOM ANSWERS)
prompt = ChatPromptTemplate.from_template("""
You are a research assistant.

Answer the question ONLY using the provided context.
If the answer is not present in the context, say:
"I could not find this information in the document."

<context>
{context}
</context>

Question: {question}
""")

# 5. Build RAG chain (NEW LANGCHAIN WAY)
rag_chain = (
    {
        "context": retriever,
        "question": RunnablePassthrough()
    }
    | prompt
    | llm
    | StrOutputParser()
)

# 6. Ask questions in a loop
while True:
    question = input("\nAsk a question about your document (or type 'exit'): ")
    if question.lower() == "exit":
        break

    answer = rag_chain.invoke(question)
    print("\nAnswer:\n", answer)
