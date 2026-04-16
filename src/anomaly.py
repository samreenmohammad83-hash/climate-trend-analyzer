def detect_anomalies(df):
    mean = df['temperature'].mean()
    std = df['temperature'].std()

    df['anomaly'] = ((df['temperature'] > mean + 2*std) |
                     (df['temperature'] < mean - 2*std))

    print("⚠️ Anomalies detected:", df['anomaly'].sum())
    return df