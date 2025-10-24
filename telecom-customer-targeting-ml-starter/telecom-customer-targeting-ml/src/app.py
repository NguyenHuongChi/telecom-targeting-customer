import streamlit as st

st.set_page_config(page_title="Telecom Customer Targeting", layout="centered")
st.title("📡 Telecom Customer Targeting (Demo Placeholder)")

st.write("""
This is a minimal Streamlit placeholder. 
- Add your feature engineering / modelling code here.
- For portfolio: show charts, a confusion matrix, or scenario sliders.
""")
prompt = st.text_input("Try a simple input (e.g., age=45, has_tv_package=yes):")
if st.button("Predict"):
    st.success("Demo only — plug in your model to run inference here.")
