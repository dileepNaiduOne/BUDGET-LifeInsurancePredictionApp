import streamlit as st

st.set_page_config(layout="wide")

with open( "style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

home_page = st.Page(
    page="papers/home_page.py", 
    title="Home Page"
)

pipe_page = st.Page(
    page="papers/pipe_page.py", 
    title="Pipeline Page"
)

data_page = st.Page(
    page="papers/data_page.py", 
    title="Data Page"
)

random_page = st.Page(
    page="papers/random_page.py", 
    title="Random Page"
)


pg = st.navigation(pages=[home_page, pipe_page, data_page, random_page], position="hidden")

pg.run()