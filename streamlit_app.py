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
