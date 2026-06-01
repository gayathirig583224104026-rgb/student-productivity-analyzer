import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import io

# Page Settings
st.set_page_config(
    page_title="Student Productivity Analyzer",
    page_icon="📊",
    layout="wide"
)

# Read Data
df = pd.read_csv("data/student_data.csv")

# Calculations
total_expense = df["Expense"].sum()
average_study = df["StudyHours"].mean()

top_category = df.groupby("Category")["Expense"].sum().idxmax()

productivity_score = (
    df["StudyHours"].mean() * 10
    + df["SleepHours"].mean() * 5
)

# Title
st.title("📊 Student Productivity Analytics Dashboard")
st.markdown("Analyze expenses, study habits, and productivity trends.")

# Sidebar
st.sidebar.title("📊 Dashboard Menu")
st.sidebar.info("Student Productivity Analyzer")

# Metrics Row
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("💰 Total Expense", total_expense)

with col2:
    st.metric("📚 Avg Study Hours", round(average_study, 2))

with col3:
    st.metric("🏆 Top Category", top_category)

with col4:
    st.metric("⚡ Productivity Score", round(productivity_score, 2))

# Data Table
st.subheader("📋 Student Data")
st.dataframe(df)



st.subheader("⬇️ Download Data")

csv_buffer = io.StringIO()
df.to_csv(csv_buffer, index=False)

st.download_button(
    label="📥 Download Student Data (CSV)",
    data=csv_buffer.getvalue(),
    file_name="student_data.csv",
    mime="text/csv"
)

# Data for Charts
study_data = df.set_index("Date")["StudyHours"]
category_expense = df.groupby("Category")["Expense"].sum()

# Side-by-Side Charts
col1, col2 = st.columns(2)

with col1:
    st.subheader("📈 Study Hours Trend")
    st.line_chart(study_data)

with col2:
    st.subheader("📊 Expense by Category")
    st.bar_chart(category_expense)

# Pie Chart
st.subheader("🥧 Expense Distribution")

fig, ax = plt.subplots(figsize=(6, 6))

ax.pie(
    category_expense,
    labels=category_expense.index,
    autopct="%1.1f%%"
)

st.pyplot(fig)

# Success Message
st.success("✅ Analysis Completed Successfully!")