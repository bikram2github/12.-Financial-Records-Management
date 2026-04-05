import streamlit as st
from datetime import datetime


with st.form("Financial Records Management System"):
    st.write("Please fill the details below")
    amount = st.number_input("Amount", min_value=0.0, step=0.01)
    record_type = st.selectbox("Record Type", ["income", "expense"])
    category = st.selectbox("Category", ["Salary","Business","Bonus","Rent", "Groceries", "Education","Internet/Mobile", "Entertainment", "Utilities", "Transportation", "Healthcare","Gym/Fitness","Loan/EMI", "Other"])
    note = st.text_area("Note")

    submitted = st.form_submit_button("Submit")
    if submitted:
        st.success("Record submitted successfully!")
        st.write(f"Amount: {amount}")
        st.write(f"Record Type: {record_type}")
        st.write(f"Category: {category}")
        st.write(f"Note: {note}")
        st.write(f"Date: {datetime.now().strftime('%Y-%m-%d')}")