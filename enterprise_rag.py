from langchain.llms import OpenAI
from langchain.chains import RetrievalQA

def build_enterprise_rag(vector_store):
    llm = OpenAI(temperature=0)
    qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=vector_store.as_retriever())
    return qa