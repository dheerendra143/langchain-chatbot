import streamlit as st
import llm.config as chain


st.title("Chat Ollama")
query = st.text_input("Enter your query")
if query:
    resource = chain.invoke(query)
    st.write(resource.content)