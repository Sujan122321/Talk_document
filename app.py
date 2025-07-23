import streamlit as st 
import google.generativeai as genai

from utils.document import load_pdf, load_docx, load_txt,chunk_test
from utils.text_embedder import embed_chunks, retrieve_relevant_chunks
import time

# Page config
st.set_page_config(page_title="Talk with your Document " layout="wide")
st.title("Talk with Your Document")

# sidebar for Gemini API key
st.sidebar.title("Gemini API Key")
user_api_key = st.sidebar.text_input("Enter your Gemini API key", type="password")

if not user_api_key:
    st.warning("Please enter your Gemini API key in the sidebar.")
    st.stop()

