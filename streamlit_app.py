import streamlit as st

st.title("🎈 fADHIL WORLD")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
import streamlit as st

st.button("Login", type="primary")
if st.button("yes"):
    st.write("yes")
else:
    st.write("no")

if st.button("hahaha", type="tertiary"):
    st.write("HAYUKKK")

import streamlit as st

def get_user_name():
    return 'John'

# ------------------------------------------------
# Want people to see this part of the code...

def get_punctuation():
    return '!!!'

greeting = "Hi there, "
user_name = get_user_name()
punctuation = get_punctuation()

st.write(greeting, user_name, punctuation)

# ...up to here
# ------------------------------------------------


import streamlit as st

with st.sidebar:
    messages = st.container(height=200)
    if prompt := st.chat_input("Say something"):
        messages.chat_message("user").write(prompt)
        messages.chat_message("assistant").write(f"Echo: {prompt}")
foo = 'bar'
st.write('Done!')
