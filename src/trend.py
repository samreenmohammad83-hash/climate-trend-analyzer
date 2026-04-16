from sklearn.linear_model import LinearRegression
import numpy as np

def analyze_trend(df):
    df['time'] = np.arange(len(df))
    model = LinearRegression()
    model.fit(df[['time']], df['temperature'])

    print("📈 Trend slope:", model.coef_[0])