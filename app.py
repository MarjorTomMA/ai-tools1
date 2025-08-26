import streamlit as st
st.title("my first Streamlit App")
name = st.text_input("Input your name：")
if name:
    st.write(f"Hey, {name}!")
