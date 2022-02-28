import requests
import streamlit as st

def get_age ():
    name = st.text_input('Please enter a name', '')
    url_api ="https://api.agify.io?name="+name
    response = requests.get(url_api)
    st.write(response.text)
        

