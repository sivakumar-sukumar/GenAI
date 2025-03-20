import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores.faiss import FAISS
from googlesearch import search #pip install --upgrade pip | pip3 install googlesearch-python
from langchain.chains.question_answering import load_qa_chain
from langchain_community.chat_models import ChatOpenAI
from langchain_community.llms import Ollama
from langchain_community.document_loaders import WebBaseLoader
from langchain.chains.summarize import load_summarize_chain
from langchain_ollama import OllamaEmbeddings
import ssl
import urllib3
import bs4, requests
import sys
from pymongo import MongoClient
import numpy as np
import io
import PyPDF2

# Connect to the MongoDB server
client = MongoClient('localhost', 27017)
# Create (or switch to) the database
db = client['vector_database']
# Create (or switch to) the collection
collection = db['vectors']

# This script is called from AI_Sustainathon using subprocess

#arg1 = sys.argv[1]
arg1 = 'pls summarize about wild animals in southern india'
#arg1 = 'print the table for India’s Floral Species Diversity and Endemism from EnviStats India'
OPENAI_API_KEY = "***KEY***" #Pass your key here
wildlife = 'https://cwsindia.org/publication/'
wl = 'https://en.wikipedia.org/wiki/Wildlife_of_India'
test_url = 'https://www.mospi.gov.in/sites/default/files/reports_and_publication/statistical_publication/EnviStats/Chap7-Biodiversity_envst22.pdf'
test_url1 = 'https://zsi.gov.in/uploads/documents/importantLinks/english/Annual_Report_2020-21.pdf'  # takes lot of power since it contains images
test_url2 = 'https://moef.gov.in/uploads/2023/05/Annual-Report-English-2023-24.pdf'  # # takes lot of power since it contains images

def google(query):
    links = []
    for j in search(query, num_results=20,ssl_verify=False):
        #st.write(j)
        links.append(j)
    return links

import ssl
import urllib.request

#Upload PDF files
st.header("GenAI testing")
'''
with  st.sidebar:
    st.title("Your Documents")
    file = st.file_uploader(" Upload a PDf file and start asking questions", type="pdf")
    '''
file = "test"
#Extract the text

class CustomHttpAdapter (requests.adapters.HTTPAdapter):
    # "Transport adapter" that allows us to use custom ssl_context.

    def __init__(self, ssl_context=None, **kwargs):
        self.ssl_context = ssl_context
        super().__init__(**kwargs)

    def init_poolmanager(self, connections, maxsize, block=False):
        self.poolmanager = urllib3.poolmanager.PoolManager(
            num_pools=connections, maxsize=maxsize,
            block=block, ssl_context=self.ssl_context)


def get_legacy_session():
    ctx = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    ctx.options |= 0x4  # OP_LEGACY_SERVER_CONNECT
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    session = requests.session()
    session.mount('https://', CustomHttpAdapter(ctx))
    return session

def scrape_url(url):
    r = requests.get(url,verify=False)
    content_type = r.headers.get('content-type')

    if 'application/pdf' in content_type:
        ext = '.pdf'
        print('This is pdf')
        response = pdf_read(url)
    elif 'text/html' in content_type:
        ext = '.html'
        print('This is html')
        response = url_read(url)
    else:
        ext = ''
        print('Unknown type: {}'.format(content_type))
    return response

def url_read(url):
    try:
        response = get_legacy_session().get(url,verify=False)
        soup = bs4.BeautifulSoup(response.text, 'lxml')
    except Exception as e:
        soup = bs4.BeautifulSoup("skip", 'lxml')
    return soup.body.get_text(' ', strip=True)    

def pdf_read(url):
    response = requests.get(url,verify=False)
    pdf_io_bytes = io.BytesIO(response.content)
    text_list = []
    pdf = PyPDF2.PdfReader(pdf_io_bytes)

    num_pages = len(pdf.pages)

    for page in range(num_pages):
        page_text = pdf.pages[page].extract_text()
        text_list.append(page_text)
    text = "\n".join(text_list)
    return text

def wild(url):
    text = scrape_url(url)
    text_splitter = RecursiveCharacterTextSplitter(
            separators="\n",
            chunk_size=2000,
            chunk_overlap=1000,
            length_function=len
        )
    chunks = text_splitter.split_text(text)
    return chunks

user_question = st.text_input("Type Your question here")
st.write("The Questions that you asked:")
st.write(user_question)
user_question = "You are a wildlife conservative scientist in India." + arg1

def main():
    big_chunk = []
    vector_store = None
    training_flag = False
    db_flag = False
    # generating embedding
    embeddings = OllamaEmbeddings(model="llama3.2",)
    try:
        vector_store = FAISS.load_local("/Users/sivaksiv/Documents/My_projects/GenAI/python/GenAI",embeddings,allow_dangerous_deserialization=True)
    except Exception as e:
        print(e)
        vector_store = None
    if vector_store:
        db_flag = False
    metadata = {'description': 'GenAI'}

    if big_chunk:
        training_flag = True
    if user_question and db_flag == False:

        big_chunk = []
        links_2_scrape = google(user_question)
        st.write("I am learning from below websites")
        st.write("WILD ai")
        for url in links_2_scrape[:2]:
            chunks = wild(url)
            big_chunk.append(chunks)

    if big_chunk:
            for bc in big_chunk:
                vector_store = FAISS.from_texts(bc, embeddings)
                vector_store.save_local("/Users/sivaksiv/Documents/My_projects/GenAI/python/GenAI")
                match = vector_store.similarity_search(user_question)
                llm = Ollama(model="llama3.2")
                chain = load_qa_chain(llm, chain_type="stuff")
                response = chain.run(input_documents = match, question = user_question)
                st.write(response)
                print(response)
                return response
            
    if db_flag:
        match = vector_store.similarity_search(user_question)
        #st.write(match)
        #define the LLM
        llm = Ollama(model="llama3.2")
        chain = load_qa_chain(llm, chain_type="stuff")
        response = chain.run(input_documents = match, question = user_question)
        st.write(response)
        print(response)
        return response
    
def insert_vector(vector, metadata):
    document = {
        'vector': vector,
        'metadata': metadata
    }
    collection.insert_one(document)

# To retrieve vectors from the database, we can query the collection:

def get_vector_by_metadata(metadata):
    document = collection.find_one({'metadata.description': metadata})
    if document:
        vector = document['vector']
        return vector
    return None

main()


