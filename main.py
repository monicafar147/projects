# Streamlit dependencies
import streamlit as st

# Data handling dependencies
import pandas as pd

# App declaration
def main():
    page_options = ["Home","About me", "Projects"]

    page_selection = st.sidebar.selectbox("Pages", page_options)
    if page_selection == "Home":
        # Header contents
        st.title('Home')
        #Why data science
       
    if page_selection == "About me":
        st.title("About me")
        # soft skills
        # community
        # education

    if page_selection == "Projects":
        st.title("Projects")
        option = st.sidebar.radio(
            "Categories",
            ("NLP",
             "Recommender systems",
             "Logistic optimisation",
             "Power BI",
             "SQL"
             )
            )

        if option == "NLP":
            # NLP projects
            st.header('NLP')
            st.info('''Natural Language Processing is taking the data science world by storm.
                    Analysing language can provide valuable business market value and Africa can
                    benefit from research in NLP to improve education.''')
            checked = st.checkbox('Climate change tweet classifier')
            if checked:
                st.write('''The climate change tweet classifier can take any text as input and 
                        classify if the text has a sentiment of either
                        \n * Pro Climate change
                        \n * Anti Climate change
                        \n * Neutral towards Climate change
                        \n * News tweets''')
                st.info('Follow the project here:')
            st.checkbox('Vaccine tweet classifier')

        if option == "Recommender systems":
            # Movie recommender
            st.header('Recommender systems')
            st.info('''Recommender systems help users with choice paralysis to find content that
                    the user might want. Streaming platforms such as Netflix changed the way that
                    we view movies and series and by improving their recommender system, Netflix 
                    can save on marketing costs. Recommender systems are also useful tools in 
                    recruiting portals.''')
            st.checkbox('IMDb movie recommender')
        if option == "Logistic optimisation":
            st.header('Logistic optimisation')


if __name__ == '__main__':
    main()

