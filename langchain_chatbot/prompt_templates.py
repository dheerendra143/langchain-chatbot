import streamlit as st
from langchain_core.prompts import PromptTemplate

import llm.config as chat


st.title("Technical assistance")
st.subheader('This is a small application which help to solve the technical issue for the developer')
query = st.text_input(
    label="Enter your technical query",
    placeholder="Write your query here",
    )


prompt_template = PromptTemplate(
    input_variables=["code"],
    template="""
        You are the a Software architect and your role is to help your team with best technical solution
        based on the given question and the question is : {code} you solution should include the code examples,
        detailed explanation, possible reason and other helpfull details with 
        recommended solution or approach.
    """
)

if query:
    # resource = chat.chain.invoke(query)
    # st.write(resource.content)
    resource = chat.llm.stream(prompt_template.format(code=query))
    with st.container(height=300):  # Adjust height as needed
        st.write_stream(resource)