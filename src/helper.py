import os
import sys
from src.exception import CustomException
from src.logger import logging
from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings



#Extract data from the PDF
def load_single_pdf(file_path):
    try:
        loader = PyPDFLoader(file_path)
        document = loader.load()

        logging.info("pdf file load sucessfully")
        return document
    
      
    except Exception as e:
        logging.info("Exception occured at the document loading stage .")
        raise CustomException(e, sys)
    


#Create text chunks
def text_split(extracted_data):
    try:
        text_splitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap = 20)
        text_chunks = text_splitter.split_documents(extracted_data)

        logging.info("text spliting successfull")
        return text_chunks
    
    except Exception as e:
        logging.info("Exception occured at the text spliting stage .")
        raise CustomException(e, sys)
    

#download embedding model
def download_hugging_face_embeddings():
    try:
        embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        logging.info("Embedding model download sucessfull")
        return embeddings
    
    except Exception as e:
        logging.info("Exception occured at the text spliting stage .")
        raise CustomException(e, sys)
    

    

