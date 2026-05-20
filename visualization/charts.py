import matplotlib.pyplot as plt
import pandas as pd

def create_bar_chart(df, x_col, y_col):
    plt.figure(figsize=(8,5))
    plt.bar(df[x_col], df[y_col])


    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.title(f"{y_col} by {x_col}")

    plt.show()
