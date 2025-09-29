import streamlit as st
import llm.config as chat


st.title("Chat Ollama")
query = st.text_input("Enter your query")
if query:
    # resource = chat.chain.invoke(query)
    # st.write(resource.content)
    resource = chat.llm.stream(query)
    st.write(resource)