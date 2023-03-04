"""Load html from files, clean up, split, ingest into Weaviate."""
import pickle

from langchain.document_loaders import ReadTheDocsLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores.faiss import FAISS

from scrapchat.ScrapboxLoader import ScrapboxLoader


def ingest_docs():
    """Get documents from web pages."""
    loader = ScrapboxLoader("keidaroo-blu3mo.json")
    raw_documents = loader.load()
    print(raw_documents)
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
    )
    documents = text_splitter.split_documents(raw_documents)
    print(documents)
    #embeddings = OpenAIEmbeddings()
    #vectorstore = FAISS.from_documents(documents, embeddings)

    # Save vectorstore
    #with open("vectorstore.pkl", "wb") as f:
        #pickle.dump(vectorstore, f)

# def ingest_scrapbox():
#     return
#

if __name__ == "__main__":
    ingest_docs()
