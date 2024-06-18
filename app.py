import streamlit as st
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, ServiceContext, Settings
from llama_index.llms.openai import OpenAI
from llama_index.embeddings.openai import OpenAIEmbedding
import os

os.environ["OPENAI_API_KEY"] = "sk-Your Api Key"

Settings.llm = OpenAI(model="gpt-3.5-turbo")
Settings.embed_model = OpenAIEmbedding(model="text-embedding-3-small")


def load_and_process_pdfs(pdf_paths):
    pass  
    
def build_index(processed_pdfs):

    pass 

def query_index(question, index):
    response = index.as_query_engine(streaming=True).query(question)
    answers = []
    for result in response:
        answers.append(result.content)
    return answers

# Streamlit UI
st.title("Multi-PDF QA Bot")

# File uploader for PDFs
uploaded_files = st.file_uploader("Upload PDF files", type=["pdf"], accept_multiple_files=True)

if uploaded_files:
    # Process and build index for uploaded PDFs
    processed_pdfs = load_and_process_pdfs(uploaded_files)
    index = build_index(processed_pdfs)

    # Text input for user questions
    user_question = st.text_input("Ask a question about the PDFs:")

    if user_question:
        # Query index and display answer
        answer = query_index(user_question, index)
        st.write(f"Answer: {answer}")
