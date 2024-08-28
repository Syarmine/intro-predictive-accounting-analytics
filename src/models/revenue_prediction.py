import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from statsmodels.tsa.arima.model import ARIMA

def linear_regression_prediction(data):
    # Convert datetime index to number of days since the first date
    X = (data.index - data.index[0]).days.values.reshape(-1, 1)
    y = data['Revenue'].values

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    return model, X_test, y_test, y_pred, mse, r2

def arima_prediction(data, steps=30):
    model = ARIMA(data['Revenue'], order=(1, 1, 1))
    results = model.fit()

    forecast = results.forecast(steps=steps)

    return results, forecast

if __name__ == "__main__":
    revenue_data = pd.read_csv('data/raw/revenue_data.csv', parse_dates=['Date'])
    revenue_data.set_index('Date', inplace=True)

    lr_model, X_test, y_test, y_pred, mse, r2 = linear_regression_prediction(revenue_data)
    print(f"Linear Regression - MSE: {mse:.2f}, R2: {r2:.2f}")

    arima_results, forecast = arima_prediction(revenue_data)
    print("ARIMA model fitted and forecast generated.")