import streamlit as st
import create
import constants

def render_create_page():
    APP = st.navigation(["app.py"], position="hidden")

    if st.session_state["Create"]:
        st.title("Create")

        with st.form("Create_form"):
            name = st.text_input("Enter customer name")
            age = st.number_input("Enter customer age", min_value=1, step=1)
            email = st.text_input("Enter customer email")
            create_button = st.form_submit_button("Create Record")

            if name and age and constants.validate_email(email):
                if create_button:
                    create.create(name, age, email)
                    st.success("Customer record created")
            
            else:
                if create_button:
                    if(constants.alidate_email(email) == False):
                        st.warning("Please enter a valid email address")
                    else:
                        st.warning("Please enter all the fields before submitting")

        if st.button("Back"):
            st.session_state["Main"] = True
            st.session_state["Create"] = False
            APP.run()
            st.rerun()

render_create_page()