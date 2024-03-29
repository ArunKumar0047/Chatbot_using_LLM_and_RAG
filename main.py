# main.py
"""
This module provides the main entry point for the Streamlit-based chatbot application.

Author: Arunkumar
"""

import os
from dotenv import load_dotenv
load_dotenv()

import streamlit as st

from components.chatbot import Chatbot
from components.vectorstore import initialize_vectorstore



# Initialize the vectorstore
vectorstore = initialize_vectorstore(persist_directory="path/to/persist/directory")

# Initialize the chatbot
chatbot = Chatbot(vectorstore)

# Streamlit UI
st.set_page_config(page_title="Chatbot for the Airline Dataset")
st.title("Chatbot for the Airline Dataset")

# Get user input
user_query = st.text_area("Enter your query:")

# Generate the response when the button is clicked
if st.button("Generate"):
    st.write("Generating...")
    try:
        result = chatbot.generate_response(user_query)
        st.write(result)
    except Exception as e:
        st.error(f"An error occurred: {e}")