# Get a 10-year bond yield from your country
bond_yield = 0.11

# Get your country's Credit Default Swap's spread
cds_spread = 0.023

# Calculate the risk-free rate
risk_free = bond_yield - cds_spread

# Get your country's main index value
today_index = 128106

# Get your country's index value in one year (use future indexes)
future_index = 139555

# Get the expected return on stocks
expected_return_on_stocks = (future_index - today_index) / today_index

# Calculate the equity risk premium
equity_risk_premium = expected_return_on_stocks - risk_free
