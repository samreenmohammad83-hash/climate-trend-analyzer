from src.data_loader import load_data
from src.preprocessing import clean_data
from src.eda import plot_basic_trends
from src.trend import analyze_trend
from src.anomaly import detect_anomalies
from src.forecast import forecast_temperature

df = load_data()
df = clean_data(df)

plot_basic_trends(df)
analyze_trend(df)
df = detect_anomalies(df)
forecast_temperature(df)

print("✅ Project executed successfully!")