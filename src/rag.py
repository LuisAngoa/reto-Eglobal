import os
from dotenv import load_dotenv
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_groq import ChatGroq
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain_core.prompts import PromptTemplate

load_dotenv()

class RAGAssistant:
    def __init__(self, data_path="data/tickets.csv"):
        self.db_dir = "chroma_db"
        # Usamos un modelo gratuito y local para convertir el texto en números
        self.embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        self.llm = ChatGroq(model="llama3-70b-8192", temperature=0.2)
        
        # Si la base de datos no existe, la crea leyendo el CSV
        if not os.path.exists(self.db_dir):
            loader = CSVLoader(file_path=data_path, encoding='utf-8')
            documents = loader.load()
            self.vector_store = Chroma.from_documents(documents, self.embeddings, persist_directory=self.db_dir)
        else:
            # Si ya existe, simplemente la carga para ahorrar tiempo
            self.vector_store = Chroma(persist_directory=self.db_dir, embedding_function=self.embeddings)
            
        with open("prompts/rag_prompt.txt", "r", encoding="utf-8") as f:
            template = f.read()
            
        prompt = PromptTemplate(template=template, input_variables=["context", "input"])
        
        # Configuramos el buscador para que traiga los 4 tickets más relevantes
        retriever = self.vector_store.as_retriever(search_kwargs={"k": 4})
        combine_docs_chain = create_stuff_documents_chain(self.llm, prompt)
        self.qa_chain = create_retrieval_chain(retriever, combine_docs_chain)

    def ask(self, question: str) -> str:
        response = self.qa_chain.invoke({"input": question})
        return response["answer"]