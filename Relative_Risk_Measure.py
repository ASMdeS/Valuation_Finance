# Import yfinance to get data
import yfinance as yf

# Import statsmodels.api to get regression beta
import statsmodels.api as sm


# Get a company's debt
def get_company_debt(ticker_symbol):
    company_data = yf.Ticker(ticker_symbol)
    balance_sheet = company_data.balance_sheet
    total_liabilities = balance_sheet.loc['Total Debt'].values[0]

    return total_liabilities


# Get a company's equity
def get_company_equity(ticker_symbol):
    company_data = yf.Ticker(ticker_symbol)
    balance_sheet = company_data.balance_sheet
    total_equity = balance_sheet.loc['Total Equity Gross Minority Interest'].values[0]

    return total_equity


# Get the first trading day of a stock
def get_ipo_date(ticker_symbol):
    stock_data = yf.Ticker(ticker_symbol)
    history = stock_data.history(period="max").tz_localize(None)
    first_trading_date = history.index[0].date()

    return first_trading_date


# Get daily return of a stock
def get_daily_returns(ticker_symbol, date):
    historical_data = yf.download(ticker_symbol, date, end="2024-03-31")
    daily_returns = historical_data['Adj Close'].pct_change()

    return daily_returns.dropna()


# Get the regression beta between stocks and their country's main index
def regression_beta(stock_returns, index_returns):
    X = sm.add_constant(index_returns)
    model = sm.OLS(stock_returns, X)
    results = model.fit()
    beta_stock, beta_index = results.params

    return beta_index

# Country's tax rate
tax_rate = 0.34

# Companies within the sector
tickers_sector = ["ALPA4.SA", "CEAB3.SA", "GUAR3.SA", "SOMA3.SA", "LREN3.SA", "TFCO4.SA", "SBFG3.SA"]

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
debt_company = [get_company_debt(ticker) for ticker in tickers_sector]

# List of equities for companies within the sector
equity_company = [get_company_equity(ticker) for ticker in tickers_sector]

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
unlevered_beta = average_beta / (1 + (1 - tax_rate) * average_debt_equity)

# Levered beta for the company
levered_beta = unlevered_beta * (1 + (1 - tax_rate) * (get_company_debt("ARZZ3.SA") / get_company_equity("ARZZ3.SA")))
