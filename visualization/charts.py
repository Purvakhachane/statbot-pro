import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st

# Bar Chart
def create_bar_chart(df, x_col, y_col):

    fig, ax = plt.subplots(figsize=(8,5))

    ax.bar(df[x_col], df[y_col])

    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)

    ax.set_title(f"{y_col} by {x_col}")

    st.pyplot(fig)

# Heatmap
def create_heatmap(df):

    corr = df.corr(numeric_only=True)

    fig, ax = plt.subplots(figsize=(8,6))

    sns.heatmap(
        corr,
        annot=True,
        cmap="Blues",
        ax=ax
    )

    st.pyplot(fig)