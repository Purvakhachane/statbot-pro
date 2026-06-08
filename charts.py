import streamlit as st
from visualization import (
    create_bar_chart,
    create_line_chart,
    create_scatter_chart,
    create_histogram
)

def show_chart(fig):
    st.pyplot(fig)


def render_bar(df, x, y):
    fig = create_bar_chart(df, x, y)
    show_chart(fig)


def render_line(df, x, y):
    fig = create_line_chart(df, x, y)
    show_chart(fig)


def render_scatter(df, x, y):
    fig = create_scatter_chart(df, x, y)
    show_chart(fig)


def render_histogram(df, col):
    fig = create_histogram(df, col)
    show_chart(fig)