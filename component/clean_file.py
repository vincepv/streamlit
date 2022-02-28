import pandas as pd
import streamlit as st

def clean_file(): 
    
    st.header("Supprimer les doublons")
    uploaded_file = st.file_uploader("Choisir un fichier, format CSV utf8.")
    
    
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)   
        df.drop_duplicates(subset=['id'],keep='first',inplace=True)
        csv = df.to_csv().encode('utf-8')

        st.download_button(
            label="Télécharger le  fichier",
            data= csv,
            file_name='no_duplicate.csv',
            mime='text/csv',
        )