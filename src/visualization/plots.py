import matplotlib.pyplot as plt

def plot_revenue_prediction(X_test, y_test, y_pred, filename):
    plt.figure(figsize=(12, 6))
    plt.scatter(X_test, y_test, color='blue', label='Actual')
    plt.plot(X_test, y_pred, color='red', label='Predicted')
    plt.title('Revenue Prediction - Linear Regression')
    plt.xlabel('Days')
    plt.ylabel('Revenue')
    plt.legend()
    plt.savefig(f'results/figures/{filename}')
    plt.close()

def plot_arima_forecast(historical_data, forecast, filename):
    plt.figure(figsize=(12, 6))
    plt.plot(historical_data.index, historical_data['Revenue'], label='Historical')
    plt.plot(forecast.index, forecast, color='red', label='Forecast')
    plt.title('Revenue Prediction - ARIMA')
    plt.xlabel('Date')
    plt.ylabel('Revenue')
    plt.legend()
    plt.savefig(f'results/figures/{filename}')
    plt.close()
    