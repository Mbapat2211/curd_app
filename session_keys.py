import streamlit as st

def init_session_keys():
    if "Main" not in st.session_state:
        st.session_state["Main"] = True

    if "Create" not in st.session_state:
        st.session_state["Create"] = False

    if "Read" not in st.session_state:
        st.session_state["Read"] = False

    if "Update" not in st.session_state:
        st.session_state["Update"] = False

    if "Delete" not in st.session_state:
        st.session_state["Delete"] = False

    if "Update_search" not in st.session_state:
        st.session_state["Update_search"] = False

    if "Update_select" not in st.session_state:
        st.session_state["Update_select"] = False
    
    if "Update_modify" not in st.session_state:
        st.session_state["Update_modify"] = False

    if "Delete_search" not in st.session_state:
        st.session_state["Delete_search"] = False

    if "Delete_select" not in st.session_state:
        st.session_state["Delete_select"] = False

    if "records" not in st.session_state:
        st.session_state["records"] = []

    if "name" not in st.session_state:
        st.session_state["name"] = ""
    
    if "age" not in st.session_state:
        st.session_state["age"] = ""
    
    if "email" not in st.session_state:
        st.session_state["email"] = ""

    return