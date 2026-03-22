import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("📊 Netflix Churn Analysis Dashboard")

df = pd.read_csv(r"D:\netflix\netflix_user_behavior_dataset.csv")

st.subheader("Dataset Preview")
st.write(df.head())

st.subheader("Churn Distribution")
fig, ax = plt.subplots()
sns.countplot(x='churned', data=df, ax=ax)
st.pyplot(fig)

st.subheader("Feature Importance")

importance = {
    "monthly_fee": 0.145,
    "rating_given": 0.069,
    "avg_watch_time": 0.063,
    "recommendation_click_rate": 0.060,
    "completion_rate": 0.058
}

imp_df = pd.DataFrame(list(importance.items()), columns=["Feature", "Importance"])

fig2, ax2 = plt.subplots()
ax2.bar(imp_df["Feature"], imp_df["Importance"])
plt.xticks(rotation=45)
st.pyplot(fig2)

st.subheader("Insights")
st.write("""
- Pricing is the most important churn factor
- User satisfaction impacts retention
- Engagement drives user loyalty
""")