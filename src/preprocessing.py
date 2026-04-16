import pandas as pd

def clean_data(df):
    df['date'] = pd.to_datetime(df['date'])
    df = df.dropna()
    return df