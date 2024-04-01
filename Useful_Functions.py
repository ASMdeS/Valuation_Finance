import yfinance as yf

def get_element_income_statement(ticker_symbol, element):
    company_data = yf.Ticker(ticker_symbol)
    income_statement = company_data.incomestmt
    result_element = income_statement.loc[element].values[0]

    return result_element

def get_element_cash_flow(ticker_symbol, element):
    company_data = yf.Ticker(ticker_symbol)
    cash_flow_statement = company_data.cash_flow
    result_element = cash_flow_statement.loc[element].values[0]

    return result_element


def get_element_balance_sheet(ticker_symbol, element):
    company_data = yf.Ticker(ticker_symbol)
    cash_flow_statement = company_data.balance_sheet
    result_element = cash_flow_statement.loc[element].values[0]

    return result_element