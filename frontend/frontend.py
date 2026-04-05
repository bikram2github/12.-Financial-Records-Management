import streamlit as st
import requests
import pandas as pd
from datetime import datetime

import sqlite3


def delete_table():
    with sqlite3.connect("financial_db.db") as conn:
        cur = conn.cursor()

        cur.execute("DROP TABLE IF EXISTS financial_records;")


url = "https://financial-records-management-production.up.railway.app"



st.title("💰 Financial Records Manager")
st.caption("Track your income & expenses easily")



option = st.sidebar.pills(
    "📌 Menu",
    ["➕ Add Record", "📊 View / Analyze Records","❌ Delete All Records"]
)

if option == "➕ Add Record":

    with st.form("Financial Records Management System"):
        amount = st.number_input("Amount", min_value=0.0, step=0.01)
        record_type = st.selectbox("Record Type", ["income", "expense"])
        category = st.selectbox(
            "Category",
            ["Salary","Business","Bonus","Rent", "Groceries", "Education",
             "Internet/Mobile", "Entertainment", "Utilities","Saving/Investment",
             "Transportation", "Medical/Healthcare","Gym/Fitness","Loan/EMI", "Other"]
        )
        note = st.text_area("Note")

        submitted = st.form_submit_button("Submit")

        if submitted:
            if amount <= 0:
                st.error("Amount must be greater than 0")
                st.stop()

            data = {
                "amount": amount,
                "record_type": record_type,
                "category": category,
                "note": note
            }

            try:
                response = requests.post(f"{url}/create", json=data)

                if response.status_code == 200:
                    st.success("✅ Record submitted successfully!")
                    st.write(f"Amount: {amount}")
                    st.write(f"Record Type: {record_type}")
                    st.write(f"Category: {category}")
                    st.write(f"Note: {note}")
                    st.write(f"Date: {datetime.now().strftime('%Y-%m-%d')}")
                else:
                    st.error(f"❌ Error: {response.text}")

            except Exception as e:
                st.error(f"🚨 Server error: {e}")


elif option == "📊 View / Analyze Records":

    st.subheader("📄 All Records")

    try:
        res = requests.get(f"{url}/records")

        if res.status_code == 200:
            records = res.json().get("records", [])

            if not records:
                st.warning("No records found")
            else:
                df = pd.DataFrame(records)

  
                st.dataframe(df)

                st.subheader("📊 Analytics")

                total_income = df[df["record_type"] == "income"]["amount"].sum()
                total_expense = df[df["record_type"] == "expense"]["amount"].sum()

                col1, col2 = st.columns(2)

                col1.metric("💰 Total Income", total_income)
                col2.metric("💸 Total Expense", total_expense)

                st.metric("📉 Balance", total_income - total_expense)

                import pandas as pd

                df["date"] = pd.to_datetime(df["date"])

                df["month"] = df["date"].dt.to_period("M").astype(str)


                monthly_summary = df.groupby(["month", "record_type"])["amount"].sum().unstack()


                monthly_summary = monthly_summary.fillna(0)

                st.subheader("📊 Monthly Income vs Expense")


                st.dataframe(monthly_summary)
                #st.area_chart(monthly_summary)

                st.subheader("💰 Income by Category")

                income_df = df[df["record_type"] == "income"]

                if not income_df.empty:
                    income_summary = income_df.groupby("category")["amount"].sum()
                    st.dataframe(income_summary)
                else:
                    st.info("No income data available")

                st.subheader("💸 Expense by Category")

                expense_df = df[df["record_type"] == "expense"]

                if not expense_df.empty:
                    expense_summary = expense_df.groupby("category")["amount"].sum()
                    st.dataframe(expense_summary)
                    st.bar_chart(expense_summary)
                else:
                    st.info("No expense data available")

  

        else:
            st.error("Failed to fetch records")

    except Exception as e:
        st.error(f"Error: {e}")

elif option == "❌ Delete All Records":
    st.warning("⚠️ This will permanently delete all records. Proceed with caution!")
    if st.button("Delete All Records"):
        try:
            delete_table()
            st.success("✅ All records deleted successfully!") 
        except Exception as e:
            st.error(f"Error: {e}")

    