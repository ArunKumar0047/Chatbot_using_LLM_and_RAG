# components/chatbot.py
"""
This module defines the Chatbot class, which encapsulates the logic for generating responses
to user queries using the provided vectorstore and language model.

Author: Arunkumar
"""

from typing import Optional
from dotenv import load_dotenv
load_dotenv()
import os
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

class Chatbot:
    """
    Chatbot class for generating responses to user queries.
    """

    def __init__(self, vectorstore):
        
        """
        Initialize the Chatbot instance.

        Args:
            vectorstore (VectorStore): The vectorstore instance to use for retrieving relevant context.
        """
        self.model = ChatOpenAI(openai_api_key=os.getenv("API_KEY"))
        self.retriever = vectorstore.as_retriever()

        # Define the prompt template for the chatbot
        prompt_template = """You are an assistant for question-answering tasks.

        Answer the question based only on the following context:
        
        Summarize and answer

        Keep the answer within 5 lines as much as possible.



        {context}

        Question: {question}
        """

        # Create the chat prompt template
        self.template = ChatPromptTemplate.from_template(prompt_template)

        # Set up the chain with the retriever, prompt, model, and output parser
        self.chain = (
            {"context": self.retriever, "question": RunnablePassthrough()}
            | self.template
            | self.model
            | StrOutputParser()
        )

    def generate_response(self, query: str) -> Optional[str]:
        """
        Generate a response to the given user query.

        Args:
            query (str): The user query.

        Returns:
            Optional[str]: The generated response, or None if an error occurred.
        """
        try:
            result = self.chain.invoke(query)
            return result
        except Exception as e:
            print(f"An error occurred: {e}")
            return None