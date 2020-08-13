# Streamlit dependencies
import streamlit as st

# Data handling dependencies
import pandas as pd

# App declaration
def main():
    page_options = ["Home","About me"]

    page_selection = st.sidebar.selectbox("Choose Option", page_options)
    if page_selection == "Home":
        # Header contents
        st.title('#Home')
        
    if page_selection == "About me":
        st.title("About me")

if __name__ == '__main__':
    main()
