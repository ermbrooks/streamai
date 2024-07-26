import streamlit as st

import authenticate as authenticate

st.set_page_config(
    page_title="Home",
    page_icon="👋",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Check authentication when user lands on the home page.
# authenticate.set_st_state_vars()

# # Add login/logout buttons
# if st.session_state["authenticated"]:
#     authenticate.button_logout()
# else:
#     authenticate.button_login()

# st.session_state

# with st.echo("below"):
from st_pages import add_page_title, show_pages, Page

show_pages(
    [
        Page("streamlit_app.py", "Home"),
    ]
)

add_page_title()  # Optional method to add title and icon to current page
# Also calls add_indentation() by default, which indents pages within a section

st.write("""
         Welcome,
         
         This is a playground app for AI projects.
         """)


st.text_input("Ask a question", placeholder="Why did the chicken cross the road?")
st.button("Submit")

with st.chat_message("assistant"):
    st.write("How may I help you?")


prompt = st.chat_input("Say something")
if prompt:
    st.write(f"User has sent the following prompt: {prompt}")

with st.sidebar:
    st.write("sidebar text")
    st.write("sidebar text 2")

