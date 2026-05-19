from langchain_ollama import ChatOllama
import ollama
from database_for_cats import get_cat_facts

llm = ChatOllama(model="llama3.2")

def ask_cat_bot(question):
    facts = get_cat_facts()

    if not facts:
        return "I cannot find a fact that is in my database"
    context = "\n".join(facts)


    prompt = f"""
use the following cat facts to answer the user's question

cat Facts:
{context}

Question:
{question}
"""
    response = ollama.chat(
        model="llama3.2",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"]

if __name__ == "__main__":
    while True:
        question = input("Ask about cats: ")

        if question.lower() == "exit":
            break

        answer = ask_cat_bot(question)
        print("\nBot:",answer)