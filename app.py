import streamlit as st
# Ensure you have 'tax_agent.py' in the same folder
from tax_agent import analyze_tax

# Set page to wide mode so the table and report fit side-by-side
st.set_page_config(page_title="Tax Compliance Audit", layout="wide", page_icon="🧾")

st.title("🧾 Tax Compliance & Audit Agent")
st.markdown("### AI-Powered Forensic Analysis System")

# Primary button for main action
if st.button("Run Compliance Audit", type="primary"):
    
    # Spinner for better UX while the AI thinks
    with st.spinner("Conducting Forensic Audit..."):
        
        # Call the agent
        df, result = analyze_tax()

        if df is not None:
            # Create two columns: Left for Data, Right for the Report
            col1, col2 = st.columns([1, 1.2])

            with col1:
                st.subheader("📂 Ledger Data")
                # Highlight the table for better readability
                st.dataframe(df, use_container_width=True, height=500)

            with col2:
                st.subheader("⚖️ Audit Findings")
                # Use markdown to render the bolding and lists from the AI correctly
                st.markdown(result)
                
                # Add a download button for the report (Optional feature)
                st.download_button(
                    label="Download Audit Report",
                    data=result,
                    file_name="audit_report.md",
                    mime="text/markdown"
                )
        else:
            st.error(result) # Display the error message returned by the agent