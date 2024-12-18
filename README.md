# Project Assitant
![Static Badge](https://img.shields.io/badge/Project%20Status-ongoing-yellow)

## Descripiton
This is an AI assistant for projects.
I started working on it because expecting raw LLMs like ChatGPT to understand the context and using upto documentations of the tools was a painful experience.
So why not build a tool that can be optimized for your specific usecase.

## Tools used in this project are
- Python
- Pinecone (Vector DB)
- Langchain (prompt composer)
- Groq (LLM)
- pylint (dev dependency for code formatter)

## Prerequisites

To get started, you will need the following:

- Python 3.7 or higher
- A **Pinecone** API key 
- A **Groq** API key

## Install the dependencies by running:

    pip install -r requirements.txt
    
## Project Structure

- main.py
  - where everything begins
- services
  - embedding classes for external services
- utils
  - classes and methods that start and begin within the program
  - reusable tools within the project

## Attention
- This is an ongoing project that has just been started last week
- I'm currently migrating the legacy implementation of the langchain library tools
