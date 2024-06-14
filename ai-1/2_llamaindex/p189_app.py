from llama_index import download_loader, GPTVectorStoreIndex, ServiceContext, LLMPredictor, LangchainEmbedding
from llama_index.readers import BeautifulSoupReader
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import HuggingFaceEmbeddings
from llama_index import Document

loader = BeautifulSoupReader()

documents = loader.load_data(url=["https://openai.com/blog/planning-for-agi-and-beyond"])
print("Documents loaded successfully")
print(f"Loaded documents: {documents}")

document_objects = [Document(text=doc.text) for doc in documents]

embed_model = LangchainEmbedding(HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2"))
print("Embedding Model initialized successfully")

llm_predictor = LLMPredictor(llm=ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo"))