import pandas as pd
import numpy as np

def generate_financial_data(years=3, quarters_per_year=4):
    periods = years * quarters_per_year
    dates = pd.date_range(start='2020-01-01', periods=periods, freq='Q')
    
    np.random.seed(42)  # for reproducibility
    
    data = {
        'Date': dates,
        'Revenue': np.random.normal(1000000, 100000, periods).cumsum(),
        'COGS': np.random.normal(600000, 60000, periods).cumsum(),
        'Operating_Expenses': np.random.normal(200000, 20000, periods).cumsum(),
        'Other_Income': np.random.normal(10000, 1000, periods).cumsum(),
        'Interest_Expense': np.random.normal(5000, 500, periods).cumsum()
    }
    
    df = pd.DataFrame(data)
    df['Gross_Profit'] = df['Revenue'] - df['COGS']
    df['Operating_Income'] = df['Gross_Profit'] - df['Operating_Expenses']
    df['Net_Income'] = df['Operating_Income'] + df['Other_Income'] - df['Interest_Expense']
    
    return df

if __name__ == "__main__":
    financial_data = generate_financial_data()
    financial_data.to_csv('data/raw/financial_data.csv', index=False)
    print("Financial data generated and saved to data/raw/financial_data.csv")