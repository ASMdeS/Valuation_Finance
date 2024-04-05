# Import statsmodels.api to get regression beta
import statsmodels.api as sm

# Import functions which will be used in the code
from Yahoo_Finance_Functions import get_daily_returns, get_element_balance_sheet, get_ipo_date

# Importing the company ticker and sector tickets
from Company_and_Country import company_ticker, tickers_sector, country_tax_rate


# Get the regression beta between stocks and their country's main index
def regression_beta(stock_returns, index_returns):
    X = sm.add_constant(index_returns)
    model = sm.OLS(stock_returns, X)
    results = model.fit()
    beta_stock, beta_index = results.params

    return beta_index


# Dates in which their stock was listed
dates_ipo = [get_ipo_date(ticker) for ticker in tickers_sector]

# To get the largest time period possible in which all stocks were traded, we will get the latest IPO
latest_ipo = max(dates_ipo)

# Get the returns from Brazil's main index
bovespa_returns = get_daily_returns("^BVSP", latest_ipo)

# List of returns for companies within the sector
returns_sector = [get_daily_returns(ticker, latest_ipo) for ticker in tickers_sector]

# List of betas for companies within the sector
beta_company = [regression_beta(get_daily_returns(ticker, latest_ipo), bovespa_returns) for ticker in tickers_sector]

# List of debts for companies within the sector
debt_company = [get_element_balance_sheet(ticker, 'Total Debt') for ticker in tickers_sector]

# List of equities for companies within the sector
equity_company = [get_element_balance_sheet(ticker, 'Total Equity Gross Minority Interest') for ticker in
                  tickers_sector]

# List of debt to equity ratios for companies within the sector
debt_equity = [debt / equity for debt, equity in zip(debt_company, equity_company)]

# Average of betas for companies within the sector
average_debt = sum(debt_company) / len(debt_company)

# Average of betas for companies within the sector
average_equity = sum(equity_company) / len(equity_company)

# Average of betas for companies within the sector
average_beta = sum(beta_company) / len(beta_company)

# Average of debt to equity ratios for companies within the sector
average_debt_equity = sum(debt_equity) / len(debt_equity)

# Unlevered beta for the sector
unlevered_beta = average_beta / (1 + (1 - country_tax_rate) * average_debt_equity)

# Levered beta for the company
levered_beta = unlevered_beta * (1 + (1 - country_tax_rate) * (
        get_element_balance_sheet(company_ticker, 'Total Debt') / get_element_balance_sheet(company_ticker,
                                                                                            'Total Equity Gross Minority Interest')))
