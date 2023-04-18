import streamlit as st

st.set_page_config(
    page_title="AI Apps",
    page_icon="🚝",
)

st.markdown("### Select an App from the sidebar:")
st.markdown("1. DuckGpt: Let GPT query your data using DuckDB")
st.markdown("2. Prompt Demo: Build a Prompt product using your own data")
st.markdown("3. Chat Demo: Build a Chat product using your own data")

st.sidebar.success("Select an App from above")
