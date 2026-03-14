import streamlit as st

# Initializing session state cookies

if "Main" not in st.session_state:
    st.session_state["Main"] = False

if "Create" not in st.session_state:
    st.session_state["Create"] = False

if "Read" not in st.session_state:
    st.session_state["Read"] = False

if "Update" not in st.session_state:
    st.session_state["Update"] = False

if "Delete" not in st.session_state:
    st.session_state["Delete"] = False

def handle_back(operation_String):
    st.session_state[operation_String] = False
    st.session_state["Main"] = True

# Handling CRUD Operations on the application page

def handle_create():
    if st.session_state["Main"]:
        st.session_state["Main"] = False
        st.session_state["Create"] = True

        st.button("Back", on_click=handle_back, args=("Create", ))

    return

def handle_read():
    if st.session_state["Main"]:
        st.session_state["Main"] = False
        st.session_state["Read"] = True

        st.button("Back", on_click=handle_back, args=("Read", ))
    
    return

def handle_update():
    if st.session_state["Main"]:
        st.session_state["Main"] = False
        st.session_state["Update"] = True

        st.button("Back", on_click=handle_back, args=("Update", ))

    return

def handle_delete():
    if st.session_state["Main"]:
        st.session_state["Main"] = False
        st.session_state["Delete"] = True

        st.button("Back", on_click=handle_back, args=("Delete", ))

    return

def no_active_state():
    if st.session_state["Main"]:
        return False
    
    if st.session_state["Create"]:
        return False
    
    if st.session_state["Read"]:
        return False

    if st.session_state["Update"]:
        return False
    
    if st.session_state["Delete"]:
        return False
    
    return True

def go_to_operation():
    if st.session_state["Create"]:
        handle_create()
    
    if st.session_state["Read"]:
        handle_read()

    if st.session_state["Update"]:
        handle_update()
    
    if st.session_state["Delete"]:
        handle_delete()
    
    return

def main():

    if no_active_state():
        st.session_state["Main"] = True
    else:
        go_to_operation()

    if st.session_state["Main"]:
        st.title('CRUD Application')

        st.button("Create", on_click=handle_create)
        st.button("Read", on_click=handle_read)
        st.button("Update", on_click=handle_update)
        st.button("Delete", on_click=handle_delete)

    return

main()