#import required libraries
import streamlit as st
from langchain.llms import OpenAI
from langchain import PromptTemplate

st.set_page_config(page_title='Blog Outline Generator App', page_icon='🔮')
st.title('Blog Outline Generator App')
openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')

def generate_response(topic):
    llm = OpenAI(model_name = 'text-davinci-003', temperature = 0.7, openai_api_key  = openai_api_key)
    #prompt
    template = 'As an experienced data scientist and technical writer, generate an outline for a blog about {topic}.'
    prompt = PromptTemplate(input_variables = ['topic'], template = template)
    prompt_query = prompt.format(topic = topic)
    #Run LLM model and print out the response
    response = llm(prompt_query)
    return st.info(response)
with st.form('my_form'):
    topic_text = st.text_input('Enter your topic here', " ")
    submitted = st.form_submit_button('Generate response')
    if not openai_api_key.startswith('sk-'):
        st.warning('Please enter your OpenAI API key in the sidebar', icon = '🔑')
    if submitted and openai_api_key.startswith('sk-'):
        generate_response(topic_text)