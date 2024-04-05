from Growth import expected_growth_operating, expected_growth_net
from Cash_Flows import free_cash_flow_firm, free_cash_flow_equity
from Relative_Risk_Measure import levered_beta
from Cost_Equity_Premium import equity_risk_premium
from Growth import return_capital, expected_growth_operating, expected_growth_net, reinvestment_rate
from Yahoo_Finance_Functions import get_element_balance_sheet, get_element_cash_flow, get_element_income_statement
from Cost_Debt_Capital import cost_debt, cost_equity, cost_capital
from Company_and_Country import company_ticker, country_tax_rate, terminal_growth

# Get the EBIT of the company
ebit_company = get_element_income_statement(company_ticker, 'EBIT')

# Defining the stock value
company_value = 0

# Calculating the growth slowing factor
growth_slowing_factor = (expected_growth_net - terminal_growth) / 5

# Calculating the FCFF discounted by the cost of capital in the growth period
for i in range(1, 6):
    ebit_company *= 1 + (expected_growth_net)
    company_value += free_cash_flow_firm / ((1 + cost_capital) ** i)
    free_cash_flow_firm *= 1 + (expected_growth_net)
    expected_growth_net -= growth_slowing_factor

# Calculating the company's terminal value
terminal_value = (ebit_company * (1 - country_tax_rate) * (1 - reinvestment_rate)) / (cost_capital - terminal_growth)

# Calculating the final company's value
company_value += terminal_value

print(company_value)