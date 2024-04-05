# Importing the function to get today's value
from Yahoo_Finance_Functions import get_today_value

# Importing Pandas to read the CSV file
import pandas as pd


# Getting the data from the CSV file
def get_country_data(csv_path, desired_country, data_column):
    df = pd.read_csv(csv_path, delimiter=';')
    country_data = df[df['Country'] == desired_country]

    if not country_data.empty:
        data_value = country_data[data_column].iloc[0]
        return float(data_value[:-1]) / 100

    else:
        raise ValueError(f"No data found for country '{desired_country}'.")


# Estabilishing file path
file_path = 'Country_Default_Spreads_and_Risk_Premiums.csv'  # Update with your file path

# Defining the country's name
country_name = 'Brazil'

# Getting the equity risk premium of the country
equity_risk_premium = get_country_data(file_path, country_name, 'Equity Risk Premium')

# Getting today's USA 10 year bond yield
bond_yield = get_today_value("^TNX") / 100

# Getting the country's risk premium
country_risk_premium = get_country_data(file_path, country_name, 'Country Risk Premium')

# Getting the country's corporate tax rate
country_tax_rate = get_country_data(file_path, country_name, 'Corporate Tax Rate')

# Estabilishing the company's name
company_ticker = 'ARZZ3.SA'

# Companies within the sector
tickers_sector = ["ALPA4.SA", "CEAB3.SA", "GUAR3.SA", "SOMA3.SA", "LREN3.SA", "TFCO4.SA", "SBFG3.SA"]

# Country's terminal growth rate
terminal_growth = 0.02
