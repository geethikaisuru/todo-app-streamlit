import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    print(todo)
    todos.append(todo)
    functions.write_todos(todos)

st.title('Todo App 📋')
st.subheader('A simple todo app using Streamlit ')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label='Enter',label_visibility='hidden',
              placeholder='Enter a to-do..',
              on_change=add_todo, key='new_todo')

#st.session_state


st.write("")
st.write("")
st.write("")
st.write("--")
st.write('Made with ❤️ by Geethika')
