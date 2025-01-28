from dotenv import load_dotenv
from langchain_groq import ChatGroq
from model import create_chat_groq
import chain
import streamlit as st

load_dotenv()

def poem_generator_app():
    '''Function for poem generator app'''
    with st.form('poem_genertator'):
        topic = st.text_input('Enter the topic for Poem ')
        submitted = st.form_submit_button('Submit')

        if submitted==True:
            response = chain.generate_poem(topic)
            st.info(response)

poem_generator_app()
    