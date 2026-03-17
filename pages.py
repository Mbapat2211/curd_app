import streamlit as st

def register_pages():
    CREATE = st.navigation(["pages/create_page.py"], position="hidden")
    READ = st.navigation(["pages/read_page.py"], position="hidden")
    UPDATE = st.navigation(["pages/update_page.py"], position="hidden")
    DELETE = st.navigation(["pages/delete_page.py"], position="hidden")
    APP = st.navigation(["app.py"], position="hidden")
    return CREATE, READ, UPDATE, DELETE