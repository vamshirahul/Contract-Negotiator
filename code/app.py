import streamlit as st
import tempfile
from services.pdf_loader import load_pdf_text
from services.clause_extractor import extract_clauses
from services.risk_analyzer import analyze_risks

st.title("Contract Intelligence – Energy")

uploaded_file = st.file_uploader("Upload Contract PDF", type=["pdf"])

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(uploaded_file.read())
        path = tmp.name

    with st.spinner("Reading contract..."):
        contract_text = load_pdf_text(path)

    if st.button("Analyze Contract"):
        with st.spinner("Extracting clauses..."):
            clauses = extract_clauses(contract_text)

        st.subheader("Extracted Clauses")
        st.json(clauses)

        with st.spinner("Analyzing risks..."):
            risks = analyze_risks(clauses)

        st.subheader("Risk Register")
        st.json(risks)
