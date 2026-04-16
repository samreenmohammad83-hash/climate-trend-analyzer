from statsmodels.tsa.arima.model import ARIMA

def forecast_temperature(df):
    model = ARIMA(df['temperature'], order=(2,1,2))
    model_fit = model.fit()

    forecast = model_fit.forecast(steps=10)
    print("🔮 Forecast:\n", forecast)