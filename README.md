# Intro to Predictive Accounting Analytics

This project is a demonstration for current cohort of accounting students that undertaking Chartered Accounting Data Analytics elective to demonstrate a combination of predictive analytics with traditional financial analysis techniques for comprehensive accounting insights.

## Features

1. Revenue Prediction
   - Linear Regression model
   - ARIMA time series forecasting

2. Financial Statement Analysis
   - Trend Analysis
   - Horizontal Analysis
   - Vertical Analysis
   - Key Financial Ratios

3. Data Generation
   - Revenue time series
   - Financial statement data

4. Visualizations
   - Interactive Plotly graphs

## Analyses Available

- Revenue forecasting
- Historical financial performance trends
- Profitability and efficiency metrics
- Financial structure composition
- Comparative period analysis

## Tools Used

- Python
- Pandas, NumPy
- Scikit-learn, Statsmodels
- Plotly

## Getting Started

1. Clone this repository
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`
4. Install requirements: `pip install -r requirements.txt`

## Usage

1. Generate sample data: `python src/data/generate_data.py`
2. Run revenue prediction models: `python src/models/revenue_prediction.py`
3. Explore the Jupyter notebook for detailed analysis: `jupyter notebook notebooks/revenue_analysis.ipynb`

## Project Structure

- `data/`: Contains raw and processed data
- `notebooks/`: Jupyter notebooks for analysis
- `src/`: Source code for data generation, models, and visualization
- `results/`: Output figures and analysis results

## Folder Structure
intro-predictive-accounting-analytics/
│
├── data/
│   ├── raw/
│   │   ├── revenue_data.csv
│   │   └── financial_data.csv
│   └── processed/
│
├── notebooks/
│   ├── revenue_analysis.ipynb
│   └── financial_analysis.ipynb
│
├── src/
│   ├── data/
│   │   ├── generate_data.py
│   │   └── generate_financial_data.py
│   ├── models/
│   │   └── revenue_prediction.py
│   └── visualization/
│       └── plots.py
│
├── results/
│   └── figures/
│
├── requirements.txt
└── README.md

##  To run the project
1. Create the folder structure as shown above.
2. Copy and paste the provided code into the respective files.
3. Open a terminal and navigate to the project root directory.
4. Run the following commands in order:
    - `python src/data/generate_data.py`
    - `python src/data/generate_financial_data.py`
    - `python src/models/revenue_prediction.py`
    - `jupyter notebook notebooks/revenue_analysis.ipynb`


## What will happen after running the commands?
- This will generate the data files and run the analyses, creating output in the results directory.
- Remember, you don't run the Python files to create them - you create them first, then run them to execute the code they contain.
- For the Jupyter notebooks, you would typically open them using Jupyter Lab or Jupyter Notebook and add content interactively.
- This process will set up the basic structure of your project. You can then start filling in the details, writing more code, and expanding the analysis as needed.

## The analysis includes:
- Trend Analysis
- Horizontal Analysis
- Vertical Analysis
- Financial Ratios

## When you are done
- You can add more data and models to the project as needed.
- You can also use this as a template for your own projects.
- Or deactivate the virtual environment using the command `deactivate`.

## Important Notes
- This is a simple example to get you started. In a real-world scenario, you would likely use more sophisticated models and techniques.
- This project is not intended to be a comprehensive analysis of accounting data. It is simply a demonstration of the basic techniques.
- You need to activate the virtual environment every time you open a new terminal window and want to work on this project.
Make sure you're in the project root directory when activating the virtual environment and running the scripts.
- If you're using an IDE like PyCharm or VS Code, you may need to select the virtual environment as the Python interpreter for your project.
- If you're still having trouble, please let me know what specific error you're encountering, and I'll be happy to help further.

- ## Repository Stats
![GitHub language count](https://img.shields.io/github/languages/count/Syarmine/intro-predictive-accounting-analytics)
![GitHub top language](https://img.shields.io/github/languages/top/Syarmine/intro-predictive-accounting-analytics)
![GitHub repo size](https://img.shields.io/github/repo-size/Syarmine/intro-predictive-accounting-analytics)
![GitHub last commit](https://img.shields.io/github/last-commit/Syarmine/intro-predictive-accounting-analytics)
