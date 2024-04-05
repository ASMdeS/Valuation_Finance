# Importing the necessary relative risk measure variables
from Relative_Risk_Measure import levered_beta, average_debt, average_equity, country_tax_rate

# Importing the necessary Country Equity Premium variables
from Cost_Equity_Premium import risk_free, equity_risk_premium

# Importing function to calculate the interest coverage ratio
from Yahoo_Finance_Functions import get_element_income_statement

# Importing company's ticker
from Company_and_Country import company_ticker

# Importing Pandas to read the CSV file
import pandas as pd


def get_last_row_greater_than_value(csv_file, column_name, value):
    df = pd.read_csv(csv_file, delimiter=';')
    last_row = df[df[column_name] < value].iloc[-1]

    return float(last_row['Spread is'][: -1]) / 100


# Calculating the interest coverage_ratio
interest_coverage_ratio = get_element_income_statement(company_ticker, 'EBIT') / get_element_income_statement(
    company_ticker,
    'Interest Expense')

# Example usage:
csv_file = 'Company_Default_Spread.csv'  # Replace with the path to your CSV file
column_name = 'greater than'  # Replace with the name of the column
value = interest_coverage_ratio
company_default_spread = get_last_row_greater_than_value(csv_file, column_name, value)

# Calculating the cost of equity
cost_equity = risk_free + levered_beta * equity_risk_premium

# Calculating the cost of debt
cost_debt = risk_free + company_default_spread

# Calculating the cost of capital
cost_capital = cost_equity * (average_equity / (average_debt + average_equity)) + cost_debt * (1 - country_tax_rate) * (
        average_debt / (average_debt + average_equity))
print(cost_capital)
print(cost_equity)
