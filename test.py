from Growth import expected_growth_operating, expected_growth_net
from Cash_Flows import free_cash_flow_firm, free_cash_flow_equity
from Relative_Risk_Measure import levered_beta
from Cost_Equity_Premium import equity_risk_premium
from Growth import return_capital, expected_growth_operating, expected_growth_net
from Yahoo_Finance_Functions import get_element_balance_sheet, get_element_cash_flow, get_element_income_statement
from Cost_Debt_Capital import cost_debt, cost_capital

company_ticker = "ARZZ3.SA"

country_tax_rate = 0.34

terminal_growth = 0.02

# Get the EBIT of the company
ebit_company = get_element_income_statement(company_ticker, 'EBIT')

stock_value = free_cash_flow_firm / (1 + cost_capital)

print(stock_value)

for i in range(0, 5):
    free_cash_flow_firm *= (1 + expected_growth_net)
    stock_value += free_cash_flow_firm / (1 + cost_capital)

print(stock_value)

stock_value += (ebit_company * ((1 + expected_growth_operating) ** 5) * (1 - country_tax_rate) * (
            (1 - terminal_growth) / return_capital)) / (cost_capital - terminal_growth)

print(stock_value)

