import streamlit as st
import pandas as pd
import read

def render_read_page():
    APP = st.navigation(["app.py"], position="hidden")

    if st.session_state["Read"]:
        st.title("Read")

        search_by = st.radio("Read records by name or email", ["Name", "Email"])
        
        if search_by == "Name":
            name = st.text_input("Enter customer name")
            read_button = st.button("Show Records")
            if read_button:
                records = read.read_from_name(name)
                df = pd.DataFrame(records, columns=["Name", "Age", "Email"])
                st.dataframe(df, hide_index=True)

        elif search_by == "Email":
            email = st.text_input("Enter customer email")
            read_button = st.button("Show Records")
            if read_button:
                records = read.read_from_email(email)
                df = pd.DataFrame(records, columns=["Name", "Age", "Email"])
                st.dataframe(df, hide_index=True)

        

        if st.button("Back"):
            st.session_state["Main"] = True
            st.session_state["Read"] = False
            APP.run()
            st.rerun()

render_read_page()