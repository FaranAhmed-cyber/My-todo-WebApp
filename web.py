import streamlit as sl
import functions


sl.title("Todo Web App")
sl.subheader('Hello everyone.')
sl.text("i am Faran Ahmed.")

data_file = functions.read_file()


def add_todo():
    data = sl.session_state["add"] + "\n"
    data_file.append(data)
    functions.write_file(data_file)


for index, row in enumerate(data_file):
    checkbox = sl.checkbox(row, key=row)
    if checkbox:
        data_file.pop(index)
        functions.write_file(data_file)
        del sl.session_state[row]
        sl.experimental_rerun()

sl.text_input(label="", placeholder="Add a todo...",
                    key="add", on_change=add_todo)