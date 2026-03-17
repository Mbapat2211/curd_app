import streamlit as st
import pages as pg
import db_init

def main():
    db_init.init_db()
    CREATE, READ, UPDATE, DELETE = pg.register_pages()

    if st.session_state["Main"]:
        st.title('CRUD Application')

        if st.button("Create"):
            st.session_state["Main"] = False
            st.session_state["Create"] = True
            st.rerun()

        if st.button("Read"):
            st.session_state["Main"] = False
            st.session_state["Read"] = True
            st.rerun()

        if st.button("Update"):
            st.session_state["Main"] = False
            st.session_state["Update"] = True
            st.session_state["Update_search"] = True
            st.rerun()

        if st.button("Delete"):
            st.session_state["Main"] = False
            st.session_state["Delete"] = True
            st.session_state["Delete_search"] = True
            st.rerun()

    else:
        if st.session_state["Create"]:
            CREATE.run()
        
        if st.session_state["Read"]:
            READ.run()

        if st.session_state["Update"]:
            UPDATE.run()

        if st.session_state["Delete"]:
            DELETE.run()   

    return

main()