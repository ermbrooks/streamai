import streamlit as st
import random
import time
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
# from st_pages import add_page_title, show_pages, Page

# show_pages(
#     [
#         Page("streamlit_app.py", "Home"),
#     ]
# )

# add_page_title()  # Optional method to add title and icon to current page
# # Also calls add_indentation() by default, which indents pages within a section

# st.write("""
#          Welcome,
         
#          This is a playground app for AI projects.
#          """)


# st.text_input("Ask a question", placeholder="Why did the chicken cross the road?")
# st.button("Submit")

# with st.chat_message("assistant"):
#     st.write("How may I help you?")


# prompt = st.chat_input("Say something")
# if prompt:
#     st.write(f"User has sent the following prompt: {prompt}")

with st.sidebar:
    st.write("page 1")
    st.write("page 2")

# Streamed response emulator
def response_generator():
    response = random.choice(
        [
            "Hello there! How can I assist you today?",
            "Hi, human! Is there anything I can help you with?",
            "Do you need help?",
        ]
    )
    for word in response.split():
        yield word + " "
        time.sleep(0.10)


st.title("Simple chat")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        response = st.write_stream(response_generator())
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})