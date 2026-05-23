# Missing Values Analysis
def get_missing_values(df):

    return df.isnull().sum()

# Dataset Shape
def get_dataset_shape(df):

    return df.shape

# Correlation Matrix
def get_correlation(df):

    return df.corr(numeric_only=True)
    