# Importing the necessary relative risk measure variables
from Relative_Risk_Measure import levered_beta, average_debt, average_equity, tax_rate

# Importing the necessary Country Equity Premium variables
from Country_Equity_Premium import risk_free, equity_risk_premium, cds_spread

# Import yfinance to get data
import yfinance as yf


# Get a company's EBIT
def get_ebit(ticker_symbol):
    company_data = yf.Ticker(ticker_symbol)
    income_statement = company_data.incomestmt
    ebit = income_statement.loc['EBIT'].values[0]

    return ebit


# Get a company's Interest Expense
def get_interest_expense(ticker_symbol):
    company_data = yf.Ticker(ticker_symbol)
    income_statement = company_data.incomestmt
    interest_expense = income_statement.loc['Interest Expense'].values[0]

    return interest_expense


# Calculating the cost of equity
cost_equity = risk_free + levered_beta * equity_risk_premium

# Calculating the interest coverage_ratio
interest_coverage_ratio = get_ebit("ARZZ3.SA") / get_interest_expense("ARZZ3.SA")

# Setting the company's default spread based on its interest coverage ratio
company_default_spread = 0.01

# Calculating the cost of debt
cost_debt = risk_free + cds_spread + company_default_spread

# Calculating the cost of capital
cost_capital = cost_equity * (average_equity / (average_debt + average_equity)) + cost_debt * (1 - tax_rate) * (
        average_debt / (average_debt + average_equity))
