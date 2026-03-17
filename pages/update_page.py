import streamlit as st
import pandas as pd
import read
import update
import constants

def process_update_modify():
    name = st.session_state["name"]
    age = st.session_state["age"]
    email = st.session_state["email"]

    with st.form("Update_form"):
        new_name = st.text_input("Update customer name", value=name)
        new_age = st.number_input("Update customer age", min_value=1, step=1, value=int(age))
        new_email = st.text_input("Update customer email", value=email)
        update_button = st.form_submit_button("Update Record")

        if update_button:
            if constants.validate_email(new_email):
                update.update(name, age, email, new_name, new_age, new_email)
                st.success("Customer record updated")
            else:
                st.warning("Please enter a valid email address")
    return

def process_update_select():
    records = st.session_state["records"]
    if records:
        record_list = constants.arrange_records(records)

        with st.form("Select_record_form"):
            select_records = st.radio("Select record to update", record_list)
            select_button = st.form_submit_button("Select")
            
            if select_records:
                if select_button:
                    [name, age, email] = select_records.split(",")
                    st.session_state["name"] = name
                    st.session_state["age"] = age
                    st.session_state["email"] = email
                    st.session_state["Update_select"] = False
                    st.session_state["Update_modify"] = True
                    st.rerun()

    else:
        st.warning("No record found to update")
    
    return

def process_update_search():
    update_by = st.radio("Select records to update by name or email", ["Name", "Email"])

    if update_by == "Name":
        name = st.text_input("Enter customer name: ")
        read_button = st.button("Show Records")
        if read_button:
            records = read.read_from_name(name)
            st.session_state["records"] = records
            st.session_state["Update_search"] = False
            st.session_state["Update_select"] = True
            st.rerun()

    elif update_by == "Email":
        email = st.text_input("Enter customer email: ")
        read_button = st.button("Show Records")
        if read_button:
            records = read.read_from_email(email)
            st.session_state["records"] = records
            st.session_state["Update_search"] = False
            st.session_state["Update_select"] = True
            st.rerun()

    return


def render_update_page():
    APP = st.navigation(["app.py"], position="hidden")

    if st.session_state["Update"]:
        st.title("Update")

        if st.session_state["Update_search"]:
            process_update_search()

        elif st.session_state["Update_select"]:
            process_update_select()

        elif st.session_state["Update_modify"]:
            process_update_modify()

        if st.button("Back"):
            st.session_state["Main"] = True
            st.session_state["Update"] = False
            st.session_state["Update_search"] = False
            st.session_state["Update_select"] = False
            st.session_state["Update_modify"] = False
            st.session_state["records"] = []
            st.session_state["name"] = ""
            st.session_state["age"] = ""
            st.session_state["email"] = ""

            APP.run()
            st.rerun()

    return

render_update_page()