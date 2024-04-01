import yfinance as yf


def get_bovespa_daily_returns():
    # Define the ticker symbol for BOVESPA
    ticker_symbol = "^BVSP"

    # Fetch historical price data using yfinance library
    historical_data = yf.download(ticker_symbol, start="2023-01-01", end="2023-12-31")

    # Calculate daily returns
    daily_returns = historical_data['Adj Close'].pct_change()

    return daily_returns.dropna()

def get_today_bovespa_value():
    # Define the ticker symbol for BOVESPA
    ticker_symbol = "^BVSP"

    # Fetch data using yfinance
    bovespa_data = yf.Ticker(ticker_symbol)

    # Get today's price
    today_price = bovespa_data.history(period="1d")["Close"].iloc[-1]

    return today_price

# Call the function to get today's value of BOVESPA
bovespa_today_value = get_today_bovespa_value()

def get_arezzo_cash_flow():
    # Define the ticker symbol for Arezzo
    ticker_symbol = "ARZZ3.SA"  # Arezzo's ticker symbol on BOVESPA

    # Fetch Arezzo's data including cash flow using yfinance library
    arezzo_data = yf.Ticker(ticker_symbol)

    # Get cash flow statement
    balance_sheet_statement = arezzo_data.income_stmt

    for index, row in balance_sheet_statement.iterrows():
        print(row)

    return balance_sheet_statement


# Call the functions to get BOVESPA yearly returns and Arezzo's cash flow
bovespa_returns = get_bovespa_daily_returns()
arezzo_cash_flow = get_arezzo_cash_flow()

print(arezzo_cash_flow)