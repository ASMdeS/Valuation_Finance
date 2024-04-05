from Cash_Flows import free_cash_flow_firm, free_cash_flow_equity
from Growth import expected_growth_net, reinvestment_rate
from Yahoo_Finance_Functions import get_element_income_statement, get_total_outstanding_shares
from Cost_Debt_Capital import cost_capital, cost_equity
from Company_and_Country import company_ticker, country_tax_rate, terminal_growth

print(f'Expected growth based on Net Income: {expected_growth_net}')
print(f'Free Cash Flow to Firm: {free_cash_flow_firm}')
print(f'Cost of Capital: {cost_capital}')
print(f'Free Cash Flow to Equity: {free_cash_flow_equity}')
print(f'Cost of Equity: {cost_equity}')

# Total shares of the company
total_outstanding_shares = get_total_outstanding_shares(company_ticker)

# Get the EBIT of the company
ebit_company = get_element_income_statement(company_ticker, 'EBIT')

# Defining the EBIT for the FCFF valuation
fcff_ebit_company = ebit_company

# Defining the stock value
fcff_company_value = 0

# Setting the expected growth
fcff_expected_growth = expected_growth_net

# Calculating the growth slowing factor
growth_slowing_factor = (fcff_expected_growth - terminal_growth) / 5

# Calculating the FCFF discounted by the cost of capital in the growth period
for i in range(1, 6):
    fcff_ebit_company *= 1 + fcff_expected_growth
    fcff_company_value += free_cash_flow_firm / ((1 + cost_capital) ** i)
    free_cash_flow_firm *= 1 + fcff_expected_growth
    fcff_expected_growth -= growth_slowing_factor

# Calculating the company's terminal value
fcff_terminal_value = (fcff_ebit_company * (1 - country_tax_rate) * (1 - reinvestment_rate)) / (
        cost_capital - terminal_growth)

# Calculating the final company's value
fcff_company_value += fcff_terminal_value

# Calculating the final stock's value
fcff_stock_value = fcff_company_value / total_outstanding_shares

# Defining the stock value
fcfe_company_value = 0

# Defining the EBIT for the FCFE valuation
fcfe_ebit_company = ebit_company

# Setting the expected growth
fcfe_expected_growth = expected_growth_net

# Calculating the FCFF discounted by the cost of capital in the growth period
for i in range(1, 6):
    fcfe_ebit_company *= 1 + fcfe_expected_growth
    fcfe_company_value += free_cash_flow_equity / ((1 + cost_equity) ** i)
    free_cash_flow_equity *= 1 + fcfe_expected_growth
    fcfe_expected_growth -= growth_slowing_factor

# Calculating the company's terminal value
fcfe_terminal_value = (fcfe_ebit_company * (1 - country_tax_rate) * (1 - reinvestment_rate)) / (
        cost_capital - terminal_growth)

# Calculating the final company's value
fcfe_company_value += fcfe_terminal_value

# Calculating the final stock's value
fcfe_stock_value = fcfe_company_value / total_outstanding_shares

print(f'Valuation based on the FCFF discounted by the cost of capital: {fcff_company_value}')

print(f'Price of share based on FCFF Valuation: {fcff_stock_value}')

print(f'Valuation based on the FCFE discounted by the cost of equity: {fcfe_company_value}')

print(f'Price of share based on FCFE Valuation: {fcfe_stock_value}')
