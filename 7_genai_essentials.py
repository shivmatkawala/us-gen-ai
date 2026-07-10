# Context Management:
    # Context Window 
    # Tokens
    # Conversation Hstory

    # Short History ==> Cheaper  ==> May loose Memory
    # Long History ==> Expensive ==> Better Memory

# Embeddings:
    # I love Cricket
    # I Enjoy Playing Cricket
    # Cricket is my favourte Game

    # LOVE, ENJOY, FAVOURATE  ==> Vectors are very Close

    # NOTE: Different Words but Same Meaning

    # TEXT => Embedding Model ==> Vector ==> [0.32, 0.92, 0.88...]

    # CAT, DOG, TIGER ==> Vectors Very Close
    # CAT, LAPTOP ==> Vectors are very Far


# VECTOR DATABASE:
    # Normal database:
    # SELECT * FROM EMPLOYEES WHERE NAME = 'RAHUL';    # Works on exact values

    # Vector dtaabase
    # find  similar meaning

    # Vector databses do use similarity search.

    # Resume --> Embedding --> Store --> Search 
    # Question --> Embedding --> Nearest Match

    # Some Vector Databses:
        # Chroma DB: Local Library, Fast for Prototypes
        # FAISS: Beginner Friendly Local
        # Pinecone: Cloud
        # Weaviate
        # Milvus
#-------------------------------------------------------------
# RAG:
    # Without RAG:
        # User --> LLM --> Hallucination
    # With RAG:
        # Question --> Emedding --> Vector Search --> Relevent Document --> LLM --> Answer

