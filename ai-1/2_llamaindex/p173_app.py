import logging
import sys
from llama_index import SimpleDirectoryReader
from llama_index import GPTVectorStoreIndex, ServiceContext, LLMPredictor
from langchain.chat_models import ChatOpenAI


# logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, force=True)

documents = SimpleDirectoryReader('data').load_data()
llm_predictor = LLMPredictor(llm=ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo"))
service_context = ServiceContext.from_defaults(
    llm_predictor=llm_predictor 
)

index = GPTVectorStoreIndex.from_documents(documents, service_context=service_context)

query_engine = index.as_query_engine()

print('-'*50)
print(query_engine.query("현주의 별명은?"))

print('-'*50)
print(query_engine.query("야바문의 이름은?"))


print('-'*50)
print(query_engine.query("야바문의 성격은?"))
