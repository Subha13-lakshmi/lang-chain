from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.memory import ConversationBufferMemory
from langchain.tools import Tool
from langchain.agents import initialize_agent, AgentType
from langchain_core.output_parsers import StrOutputParser
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain.schema import Document

# -----------------------------
# 1. LLM
# -----------------------------
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

# -----------------------------
# 2. Prompt Template
# -----------------------------
prompt = ChatPromptTemplate.from_template(
    """
    Answer the question using the context.

    Context:
    {context}

    Question:
    {question}
    """
)

# -----------------------------
# 3. Memory
# -----------------------------
memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True
)

# -----------------------------
# 4. Documents
# -----------------------------
docs = [
    Document(page_content="Snowflake is a cloud data warehouse."),
    Document(page_content="DBT is used for SQL transformations."),
    Document(page_content="LangChain helps build LLM applications.")
]

# -----------------------------
# 5. Embeddings
# -----------------------------
embedding = OpenAIEmbeddings()

# -----------------------------
# 6. Vector Store
# -----------------------------
vector_db = FAISS.from_documents(
    docs,
    embedding
)

# -----------------------------
# 7. Retriever
# -----------------------------
retriever = vector_db.as_retriever(
    search_kwargs={"k": 2}
)

# -----------------------------
# 8. Tool
# -----------------------------
def search_docs(query):
    results = retriever.invoke(query)
    return "\n".join([doc.page_content for doc in results])

search_tool = Tool(
    name="DocumentSearch",
    func=search_docs,
    description="Search information from knowledge base"
)

# -----------------------------
# 9. Agent
# -----------------------------
agent = initialize_agent(
    tools=[search_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    memory=memory,
    verbose=True
)

# -----------------------------
# 10. User Question
# -----------------------------
question = "What is DBT?"

# Retrieve Context
context_docs = retriever.invoke(question)

context = "\n".join(
    [doc.page_content for doc in context_docs]
)

# -----------------------------
# 11. Chain
# -----------------------------
chain = prompt | llm | StrOutputParser()

response = chain.invoke({
    "context": context,
    "question": question
})

print("\nAnswer:")
print(response)

# -----------------------------
# 12. Agent Execution
# -----------------------------
agent_response = agent.invoke(
    {"input": "Explain Snowflake"}
)

print("\nAgent Response:")
print(agent_response)