# PDF --> Extract Text --> Split into Chunks --> 
# Create Embeddings --> Store in ChromaDB -->
# User Question --> Embedding --> Similarity Search
# --> Relevent Chuncks --> LLM --> Answer.

#----------------------------------------------------------
# Imports:
from langchain_community.document_loaders import PyPDFLoader
from langchain_classic.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
import os
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")

# Load Data
loader = PyPDFLoader("./dataFiles/sanjeev_rdbms.pdf")
documents = loader.load()

# Split Text
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

chunks = splitter.split_documents(documents=documents)

# Create Embeddings:
embeddings = OpenAIEmbeddings(api_key=API_KEY)


# Store Embeddings in ChromaDB
db = Chroma.from_documents(
    chunks,
    embeddings,
    persist_directory="./db"
)


query = "What is the use of Rollback Command?"

docs = db.similarity_search(query=query, k=3)
# for doc in docs:
#     print(doc.page_content)

# Ask AI
client = OpenAI(api_key=API_KEY)
context= "\n\n".join([doc.page_content for doc in docs])
prompt = f"""
Answer the questions using only the context bellow.

context: {context}

question: {query}
"""
response = client.responses.create(
    model="gpt-4.1-mini",
    input=prompt
)

print(response.output_text)
