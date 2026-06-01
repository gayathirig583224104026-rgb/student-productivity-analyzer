import pandas as pd


df = pd.read_csv("data/student_data.csv")

total_expense = df["Expense"].sum()


average_study = df["StudyHours"].mean()


top_category = df.groupby("Category")["Expense"].sum().idxmax()


productivity_score = (
    df["StudyHours"].mean() * 10
    + df["SleepHours"].mean() * 5
)

print("\n===== STUDENT PRODUCTIVITY REPORT =====\n")

print("Total Expense:", total_expense)

print("Average Study Hours:", round(average_study, 2))

print("Highest Expense Category:", top_category)

print("Productivity Score:", round(productivity_score, 2))

print("\n===== AI-LIKE SUGGESTIONS =====\n")

if average_study < 4:
    print("Study hours are low. Try improving consistency.")
else:
    print("Good study consistency maintained!")

if top_category == "Food":
    print("Food expenses are highest this week.")

print("\nAnalysis Completed Successfully!")

