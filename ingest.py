"""Load html from files, clean up, split, ingest into Weaviate."""
import pickle

from langchain.document_loaders import ReadTheDocsLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores.faiss import FAISS

from scrapchat.ScrapboxLoader import ScrapboxLoader


def ingest_scrapbox():
    """Get documents from web pages."""
    # Replace this with your own json file path
    loader = ScrapboxLoader("source_docs/blu3mo_cleaned.json")
    raw_documents = loader.load()
    print(raw_documents)
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
    )
    documents = text_splitter.split_documents(raw_documents)
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(documents, embeddings)

    # Save vectorstore
    with open("vectorstore.pkl", "wb") as f:
        pickle.dump(vectorstore, f)

if __name__ == "__main__":
    ingest_scrapbox()
