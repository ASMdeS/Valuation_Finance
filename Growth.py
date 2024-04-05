# Import functions which will be used in the code
from Yahoo_Finance_Functions import get_element_income_statement, get_element_cash_flow, get_element_balance_sheet

# Importing the company ticker and tax rate
from Company_and_Country import company_ticker, country_tax_rate

# Get the dividends of the company
dividends_company = get_element_cash_flow(company_ticker, 'Cash Dividends Paid')

# Get the Net Income of the company
net_income_company = get_element_income_statement(company_ticker, 'Net Income')

# Get the Total Assets of the company
assets_company = get_element_balance_sheet(company_ticker, 'Total Assets')

# Get the Total Liabilities of the company
liabilities_company = get_element_balance_sheet(company_ticker, 'Total Liabilities Net Minority Interest')

# Get the capital expenditure of the company
capital_expenditure_company = get_element_cash_flow(company_ticker, 'Capital Expenditure')

# Get the depreciation of the company
depreciation_company = get_element_cash_flow(company_ticker, 'Depreciation')

# Get the change in working capital of the company
change_in_working_capital_company = get_element_cash_flow(company_ticker, 'Change In Working Capital')

# Get the EBIT of the company
ebit_company = get_element_income_statement(company_ticker, 'EBIT')

# Get the Total Debt of the company
debt_company = get_element_balance_sheet(company_ticker, 'Total Debt')

# Get the Cash of the company
cash_company = get_element_balance_sheet(company_ticker, 'Cash Financial')

# Calculate the Retention Ratio of the Company
retention_ratio = 1 - (dividends_company / net_income_company)

# Calculate the Return on Equity of the Company
return_equity = net_income_company / (assets_company - liabilities_company)

# Calculate the Reinvestment rate of the Company
reinvestment_rate = ((
                             - capital_expenditure_company - depreciation_company) + change_in_working_capital_company) / (
                            ebit_company * (
                            1 - country_tax_rate))

# Calculate the Return on Capital of the Company
return_capital = (ebit_company * (1 - country_tax_rate)) / (
        debt_company + (assets_company - liabilities_company) - cash_company)

expected_growth_net = retention_ratio * return_equity

expected_growth_operating = reinvestment_rate * return_capital
