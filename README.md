# Chatbot_using_LLM_and_RAG
### Creating chatbot for a dataset using LLM and RAG technique

The main idea of this project is to use a LLM to develop a chatbot for a particular dataset and then integrate RAG(Retrieval-Augmented Generation) technique.


## Table of contents:
- A brief inroduction
- Features
- How does it work?
- How to run?

### Introduction
The development of a LLM from scratch is a very tediuos and time consuming task. There are various LLM models that are pre-trained and available either through API's or open-sourced. So by using the already available LLM's, we can create a chatbot for our own data. This is the basic idea behind this project. I have built a chatbot application using Langchain for framework, Streamlit for UI and OpenAI model using API calls for the summarizing and generating part. This tool provides a custom chatbot that can be built on any type of data. 

### Features
- Utilizes RAG technique for context retrieval and answer generation.
- Framework: Langchain
- Data Vectorization: Chroma (Langchain)
- Embedding Function: Huggingface
- Model: OpenAI (integrated within Langchain)
- User Interface: Streamlit

### How does it work?
1. The dataset is observed for missing values. Appropriate measures are taken to reduce the missing values and prepare the dataset
2. Using Chroma from Langchain and an embedding function from Huggingface, the dataset is vectorized and stored as a database
3. Get OpenAI model from Langchain and connect OpenAI using the API key.
4. The user query is loaded and using the retriever, the most relevant context is got from the created database.
5. OpenAI is used to then generate and summarize to retrieved context from the retriever.
6. Streamlit is used to get the user input and display the end answer

### How to run?
The project follows a modular structure with the following files:

- `main.py`: The entry point of the application. Run `streamlit run main.py` to launch the chatbot in your browser.
- components
  1. `chatbot.py`: This file contains the code related to the OpenAI LLM integration for generating responses based on the retrieved context.
  2. `vectorstore.py`: This file handles the vectorization and embedding of the custom dataset using Chroma (Langchain) and Hugging Face embedding function.
  3. `.env` : contains the OpenAI's API key

- `requirements.txt` : To download the necessary libraries `pip install -r requirements.txt`
- `Vectorizing_Data` : This ipynb is initially run to create an embedding for the data and then stored/persisted for later use in the `vectorstore.py`.








