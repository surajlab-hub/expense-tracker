import streamlit as st
import pandas as pd

st.title("💰 Simple Expense Tracker")

if "expenses" not in st.session_state:
    st.session_state.expenses = []

amount = st.number_input("Enter Amount", min_value=0.0)
category = st.selectbox("Category", ["Food", "Travel", "Shopping", "Other"])
date = st.date_input("Select Date")

if st.button("Add Expense"):
    st.session_state.expenses.append({
        "Amount": amount,
        "Category": category,
        "Date": date
    })
    st.success("Expense added!")

if st.session_state.expenses:
    df = pd.DataFrame(st.session_state.expenses)
    st.subheader("📊 Your Expenses")
    st.dataframe(df)

    total = df["Amount"].sum()
    st.write(f"### Total Spending: ₹{total}")import streamlit as st
import pandas as pd

st.title("💰 Simple Expense Tracker")

if "expenses" not in st.session_state:
    st.session_state.expenses = []

amount = st.number_input("Enter Amount", min_value=0.0)
category = st.selectbox("Category", ["Food", "Travel", "Shopping", "Other"])
date = st.date_input("Select Date")

if st.button("Add Expense"):
    st.session_state.expenses.append({
        "Amount": amount,
        "Category": category,
        "Date": date
    })
    st.success("Expense added!")

if st.session_state.expenses:
    df = pd.DataFrame(st.session_state.expenses)
    st.subheader("📊 Your Expenses")
    st.dataframe(df)

    total = df["Amount"].sum()
    st.write(f"### Total Spending: ₹{total}")
