import streamlit as st
from tax_agent import analyze_tax

st.title("🧾 Tax Compliance Agent")

if st.button("Audit Tax Records"):
    df, result = analyze_tax()

    st.subheader("📂 Financial Summary")
    st.dataframe(df)

    st.subheader("🧠 AI Tax Compliance Report")
    st.write(result)