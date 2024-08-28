import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_financial_data(start_date, periods, base_revenue, growth_rate, seasonality, noise):
    dates = pd.date_range(start=start_date, periods=periods, freq='D')
    trend = np.linspace(0, 1, periods) * growth_rate
    seasonal = np.sin(np.linspace(0, 4*np.pi, periods)) * seasonality
    revenue = base_revenue + base_revenue * (trend + seasonal + np.random.normal(0, noise, periods))
    return pd.DataFrame({'Date': dates, 'Revenue': revenue.clip(min=0)})

def generate_ar_data(revenue_data):
    ar_data = []
    for _, row in revenue_data.iterrows():
        date = row['Date']
        revenue = row['Revenue']
        ar_30 = revenue * np.random.uniform(0.2, 0.4)
        ar_60 = revenue * np.random.uniform(0.1, 0.2)
        ar_90 = revenue * np.random.uniform(0.05, 0.1)
        ar_data.append([date, revenue, ar_30, ar_60, ar_90])
    return pd.DataFrame(ar_data, columns=['Date', 'Revenue', 'AR_30', 'AR_60', 'AR_90'])

if __name__ == "__main__":
    start_date = '2020-01-01'
    revenue_data = generate_financial_data(start_date, 730, 10000, 0.5, 2000, 0.05)
    ar_data = generate_ar_data(revenue_data)

    revenue_data.to_csv('data/raw/revenue_data.csv', index=False)
    ar_data.to_csv('data/raw/ar_data.csv', index=False)

    print("Sample data generated and saved to CSV files.")