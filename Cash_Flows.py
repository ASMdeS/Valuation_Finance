# Import functions which will be used in the code
from Yahoo_Finance_Functions import get_element_income_statement, get_element_cash_flow, get_element_balance_sheet

# Importing the cost of equity
from Cost_Debt_Capital import cost_debt

# Importing the ticker and corporate tax rate
from Company_and_Country import company_ticker, country_tax_rate

# Get the Net Income of the company
net_income_company = get_element_income_statement(company_ticker, 'Net Income')

# Get the EBIT of the company
ebit_company = get_element_income_statement(company_ticker, 'EBIT')

# Get the capital expenditure of the company
capital_expenditure_company = get_element_cash_flow(company_ticker, 'Capital Expenditure')

# Get the depreciation of the company
depreciation_company = get_element_cash_flow(company_ticker, 'Depreciation')

# Get the change in working capital of the company
change_in_working_capital_company = get_element_cash_flow(company_ticker, 'Change In Working Capital')

# Get the capital expenditure of the company
repayment_debt_company = get_element_cash_flow(company_ticker, 'Repayment Of Debt')

# Get the capital expenditure of the company
issuance_debt_company = get_element_cash_flow(company_ticker, 'Issuance Of Debt')

# Get the capital expenditure of the company
debt_company = get_element_balance_sheet(company_ticker, 'Total Debt')

# Calculate the free cash flow to firm of the company
free_cash_flow_firm = ebit_company * (1 - country_tax_rate) - (
        - capital_expenditure_company - depreciation_company) - change_in_working_capital_company

# Calculate the free cash flow to equity of the company
free_cash_flow_equity = net_income_company + capital_expenditure_company + depreciation_company + change_in_working_capital_company + (
        debt_company * cost_debt)
