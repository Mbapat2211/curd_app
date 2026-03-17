import streamlit as st
import constants
import read
import delete

def process_delete_select():
    records = st.session_state["records"]
    if records:
        record_list = constants.arrange_records(records)

        with st.form("Select_record_form"):
            select_records = st.radio("Select record to delete", record_list)
            delete_button = st.form_submit_button("Delete Record")
            
            if select_records:
                if delete_button:
                    [name, age, email] = select_records.split(",")
                    delete.delete(name, age, email)
                    st.success("Record deleted successfully")
    else:
        st.warning("No record found to delete")
    
    return

def process_delete_search():
    delete_by = st.radio("Select records to delete by name or email", ["Name", "Email"])

    if delete_by == "Name":
        name = st.text_input("Enter customer name: ")
        read_button = st.button("Show Records")
        if read_button:
            records = read.read_from_name(name)
            st.session_state["records"] = records
            st.session_state["Delete_search"] = False
            st.session_state["Delete_select"] = True
            st.rerun()

    elif delete_by == "Email":
        email = st.text_input("Enter customer email: ")
        read_button = st.button("Show Records")
        if read_button:
            records = read.read_from_email(email)
            st.session_state["records"] = records
            st.session_state["Delete_search"] = False
            st.session_state["Delete_select"] = True
            st.rerun()

    return

def render_delete_page():
    APP = st.navigation(["app.py"], position="hidden")

    if st.session_state["Delete"]:
        st.title("Delete")

        if st.session_state["Delete_search"]:
            process_delete_search()

        elif st.session_state["Delete_select"]:
            process_delete_select()

        if st.button("Back"):
            st.session_state["Main"] = True
            st.session_state["Delete"] = False
            st.session_state["Delete_search"] = False
            st.session_state["Delete_select"] = False
            st.session_state["records"] = []
            APP.run()
            st.rerun()

render_delete_page()