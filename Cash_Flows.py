# Import functions which will be used in the code
from Useful_Functions import get_element_income_statement, get_element_cash_flow, get_element_balance_sheet

# Company Ticker
company_ticker = "ARZZ3.SA"

# Get the EBIT of the company
ebit_company = get_element_income_statement(company_ticker, 'EBIT')

# Get the country's tax rate
country_tax_rate = 0.34

# Get the capital expenditure of the company
capital_expenditure_company = get_element_cash_flow(company_ticker, 'Capital Expenditure')

# Get the depreciation of the company
depreciation_company = get_element_cash_flow(company_ticker, 'Depreciation')

# Get the change in working capital of the company
change_in_working_capital_company = get_element_cash_flow(company_ticker, 'Change In Working Capital')

# Calculate the free cash flow to firm of the company
free_cash_flow_to_firm = ebit_company * (1 - country_tax_rate) - (
            - capital_expenditure_company - depreciation_company) - change_in_working_capital_company
