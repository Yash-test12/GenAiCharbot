from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")

vectorStore = Chroma(
    embedding_function=embeddings,
    persist_directory="VectorStore",
    collection_name="test",
)
from langchain.schema import Document

# Create LangChain documents for IPL players
lis=[{"content": "Virat Kohli is one of the most successful and consistent batsmen in IPL history. Known for his aggressive batting style and fitness, he has led the Royal Challengers Bangalore in multiple seasons.", "metaData": {"name": "Virat Kohli", "team": "Royal Challengers Bangalore"}},
    {"content": "Rohit Sharma is the most successful captain in IPL history, leading Mumbai Indians to five titles. He's known for his calm demeanor and ability to play big innings under pressure", "metaData": {"name": "Rohit Sharma", "team": "Mumbai Indians"}},
    {"content": "MS Dhoni, famously known as Captain Cool, has led Chennai Super Kings to multiple IPL titles. His finishing skills, wicketkeeping, and leadership are legendary.", "metaData": {"name": "MS Dhoni", "team": "Chennai Super Kings"}},
    {"content": "Sachin Tendulkar is a batsman from India, also known as god of cricket.", "metaData": {"name": "Sachin Tendulkar", "team": "Mumbai Indians"}},
    {"content": "Jasprit Bumrah is considered one of the best fast bowlers in T20 cricket. Playing for Mumbai Indians, he is known for his yorkers and death-over expertise.", "metaData": {"name": "AB de Villiers", "team": "Royal Challengers Bangalore"}},
]
# for item in lis:
#     content = item["content"]
#     metaData = item["metaData"]
#     # Create a LangChain document
#     doc = Document(
#         page_content=content,metadata=metaData
#      )
    # Add the document to the vector store
    # vectorStore.add_documents([doc])
res=vectorStore.similarity_search(
    query='Who among these are a bowler?',
    k=1
)
print(res['content'])