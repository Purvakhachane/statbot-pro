import matplotlib.pyplot as plt

# Histogram
def create_histogram(df, column):
    fig, ax = plt.subplots()
    ax.hist(df[column].dropna(), bins=10)
    ax.set_title(f"Distribution of {column}")
    ax.set_xlabel(column)
    ax.set_ylabel("Frequency")
    return fig


# Bar Chart
def create_bar_chart(df, x_col, y_col):
    fig, ax = plt.subplots()
    ax.bar(df[x_col], df[y_col])
    ax.set_title(f"{x_col} vs {y_col}")
    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)
    plt.xticks(rotation=45)
    return fig


# Line Chart
def create_line_chart(df, x_col, y_col):
    fig, ax = plt.subplots()
    ax.plot(df[x_col], df[y_col], marker='o')
    ax.set_title(f"{x_col} vs {y_col}")
    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)
    return fig

# Pie chart
def create_pie_chart(df, column):

    import matplotlib.pyplot as plt

    data = df[column].value_counts()

    fig, ax = plt.subplots(figsize=(6,6))

    ax.pie(
        data.values,
        labels=data.index,
        autopct='%1.1f%%'
    )

    ax.set_title(f"{column} Distribution")

    return fig
    
# Scatter Chart (NEW ADDITION - missing earlier)
def create_scatter_chart(df, x_col, y_col):
    fig, ax = plt.subplots()
    ax.scatter(df[x_col], df[y_col])
    ax.set_title(f"{x_col} vs {y_col}")
    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)
    return fig
