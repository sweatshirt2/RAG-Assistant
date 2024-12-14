from dotenv import load_dotenv, find_dotenv
from os import getenv

load_dotenv(find_dotenv())

llm_key = getenv("LLM_KEY")
vector_key = getenv("VECTOR_DB_KEY")


def getLLM():
    """create a custom model

    Return:
    the custom model created
    """

    from langchain_groq import ChatGroq

    return ChatGroq(
        model="llama3-8b-8192",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=3,
        api_key=llm_key,
    )
