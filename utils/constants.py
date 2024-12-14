from dotenv import load_dotenv, find_dotenv
from os import getenv

load_dotenv(find_dotenv())

LLM_KEY = getenv("LLM_KEY")
VECTOR_DB_KEY = getenv("VECTOR_DB_KEY")
