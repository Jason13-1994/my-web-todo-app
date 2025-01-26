import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n" # st.session_state - Stores persistent values across reruns.
    todos.append(todo)
    functions.write_todos(todos)

st.title("My Todo App")
st.subheader("Jason's new todo app")
st.write("An app to increase productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label=" ", placeholder="Enter a new task...", on_change=add_todo, key="new_todo")