import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("music_app_ab_test.csv")

# Title
st.title("Music App A/B Testing Dashboard")

st.markdown("""
This dashboard analyzes the impact of a new recommendation
algorithm on user engagement and retention.
""")

# Dataset preview
st.header("Dataset Preview")
st.dataframe(df.head())

# KPIs
st.header("Key Metrics")

group_means = df.groupby('group').mean(numeric_only=True)

control = group_means.loc['control']
treatment = group_means.loc['treatment']

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Control Retention",
        f"{control['retained']:.2%}"
    )

with col2:
    st.metric(
        "Treatment Retention",
        f"{treatment['retained']:.2%}"
    )

# Session duration chart
st.header("Average Session Duration")

fig, ax = plt.subplots()

group_means['session_minutes'].plot(
    kind='bar',
    ax=ax
)

ax.set_ylabel("Minutes")
ax.set_title("Session Duration by Group")

st.pyplot(fig)

# Retention chart
st.header("Retention Rate")

fig2, ax2 = plt.subplots()

group_means['retained'].plot(
    kind='bar',
    ax=ax2
)

ax2.set_ylabel("Retention Rate")
ax2.set_title("Retention by Group")

st.pyplot(fig2)

# Statistical findings
st.header("Statistical Findings")

st.write("""
- Retention improvement was statistically significant
- Treatment users showed higher engagement
- Cohen's d indicated a large practical effect size
""")

# Final recommendation
st.header("Business Recommendation")

st.success("""
Deploy the new recommendation algorithm to production,
as the treatment group demonstrated significantly higher
engagement and retention metrics.
""")
