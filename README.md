# LLM-Powered Knowledge Base Assistant

An AI-powered Knowledge Base Assistant built using **Python**, **LangChain**, **OpenAI GPT-4o-mini**, and **FAISS**. The application uses Retrieval-Augmented Generation (RAG) to retrieve relevant information from a custom knowledge base and generate accurate, context-aware responses.

---

## Features

- Answer questions using natural language
- Semantic search with OpenAI Embeddings
- Retrieval-Augmented Generation (RAG)
- FAISS vector database for efficient document retrieval
- LangChain prompt templates and output parsers
- Conversation memory for multi-turn interactions
- Agent-based document search using LangChain Tools
- Simple and modular architecture

---

## Tech Stack

- Python
- LangChain
- OpenAI GPT-4o-mini
- OpenAI Embeddings
- FAISS
- LangChain Agents
- ConversationBufferMemory

---

## Project Workflow

1. Create knowledge base documents.
2. Generate embeddings using OpenAI Embeddings.
3. Store document vectors in FAISS.
4. Receive user query.
5. Retrieve the most relevant documents.
6. Pass retrieved context to the LLM.
7. Generate an accurate response.
8. Maintain conversation history using memory.

---

## Project Structure

```
LLM-Powered-Knowledge-Base-Assistant/
│── app.py
│── requirements.txt
│── README.md
```

---

## Installation

### Clone the repository

```bash
git clone https://github.com/your-username/LLM-Powered-Knowledge-Base-Assistant.git

cd LLM-Powered-Knowledge-Base-Assistant
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Configure API Key

Create a `.env` file in the project folder and add:

```text
OPENAI_API_KEY=your_openai_api_key
```

### Run the application

```bash
python app.py
```

---

## Example

**Input**

```
What is DBT?
```

**Output**

```
DBT is used for SQL transformations.
```

---

## Concepts Used

- Large Language Models (LLMs)
- Retrieval-Augmented Generation (RAG)
- Prompt Engineering
- Semantic Search
- Vector Embeddings
- FAISS Vector Database
- LangChain
- AI Agents
- Conversation Memory

---

## Future Enhancements

- Upload PDF documents
- Streamlit web application
- Multiple document support
- Source citations
- Persistent chat history
- Support for additional LLM providers

---

## Author

**Subhalakshmi Chandran**

Generative AI | Python | LangChain | LLMs | RAG | FAISS | OpenAI
