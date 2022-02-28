import pandas as pd
import streamlit as st

def clean_file(): 
    
    uploaded_file = st.file_uploader("Choose a file. Important should be CSV utf8 only")
    
    
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)   
        df['test'] = df['rue']+' test ici'
        csv = df.to_csv().encode('utf-8')

        st.download_button(
            label="Download data as CSV",
            data= csv,
            file_name='large_df.csv',
            mime='text/csv',
        )