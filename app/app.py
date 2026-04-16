import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from statsmodels.tsa.arima.model import ARIMA

st.set_page_config(page_title="Climate Trend Analyzer", layout="wide")

st.title("🌍 Climate Trend Analyzer Dashboard")

# -----------------------------
# Generate Synthetic Data
# -----------------------------
@st.cache_data
def load_data():
    dates = pd.date_range(start="2000-01-01", periods=500)

    data = pd.DataFrame({
        "date": dates,
        "temperature": np.random.normal(25, 5, len(dates)).cumsum()/50 + 25,
        "rainfall": np.random.normal(5, 2, len(dates)),
        "humidity": np.random.normal(60, 10, len(dates))
    })

    return data

df = load_data()

# Sidebar
st.sidebar.header("Controls")

metric = st.sidebar.selectbox(
    "Select Climate Metric",
    ["temperature", "rainfall", "humidity"]
)

# -----------------------------
# DATA PREVIEW
# -----------------------------
st.subheader("📊 Dataset Preview")
st.dataframe(df.head())

# -----------------------------
# TREND GRAPH
# -----------------------------
st.subheader(f"📈 {metric.capitalize()} Trend")

fig, ax = plt.subplots()
ax.plot(df["date"], df[metric])
ax.set_title(f"{metric.capitalize()} Over Time")
ax.set_xlabel("Date")
ax.set_ylabel(metric.capitalize())

st.pyplot(fig)

# -----------------------------
# TREND ANALYSIS
# -----------------------------
st.subheader("📉 Trend Analysis")

df['time'] = np.arange(len(df))

model = LinearRegression()
model.fit(df[['time']], df[metric])

trend_slope = model.coef_[0]

if trend_slope > 0:
    st.success(f"📈 Increasing Trend Detected (Slope: {trend_slope:.4f})")
else:
    st.error(f"📉 Decreasing Trend Detected (Slope: {trend_slope:.4f})")

# -----------------------------
# ANOMALY DETECTION
# -----------------------------
st.subheader("⚠️ Anomaly Detection")

mean = df[metric].mean()
std = df[metric].std()

df['anomaly'] = ((df[metric] > mean + 2*std) |
                 (df[metric] < mean - 2*std))

anomaly_count = df['anomaly'].sum()

st.write(f"Total Anomalies Detected: {anomaly_count}")

fig2, ax2 = plt.subplots()
ax2.plot(df["date"], df[metric])
ax2.scatter(df["date"][df["anomaly"]],
            df[metric][df["anomaly"]],
            marker='o')

ax2.set_title("Anomaly Detection")

st.pyplot(fig2)

# -----------------------------
# FORECASTING
# -----------------------------
st.subheader("🔮 Forecasting (Next 10 Days)")

model = ARIMA(df[metric], order=(2,1,2))
model_fit = model.fit()

forecast = model_fit.forecast(steps=10)

st.write(forecast)

fig3, ax3 = plt.subplots()
ax3.plot(df[metric], label="Historical")
ax3.plot(range(len(df), len(df)+10), forecast, label="Forecast")
ax3.legend()

st.pyplot(fig3)

# -----------------------------
# INSIGHTS
# -----------------------------
st.subheader("🧠 Insights")

st.write(f"""
- The {metric} shows a **{'rising' if trend_slope > 0 else 'falling'} trend**
- Total anomalies detected: **{anomaly_count}**
- Forecast indicates expected future behavior
""")