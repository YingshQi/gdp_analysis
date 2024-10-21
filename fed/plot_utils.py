import matplotlib.pyplot as plt
import pandas as pd 

def plot_gdp(df: pd.DataFrame, country: str):
    """
    Plots the GDP data for a specific country.
    
    Args:
    df (pd.DataFrame): The cleaned GDP data.
    country (str): The name of the country to plot.
    
    Returns:
    None
    """
    # Filter the data for the specified country
    df_country = df[df['Country Name'] == country]
    
    # Plot GDP over time
    plt.figure(figsize=(10, 6))
    plt.plot(df_country['Year'], df_country['GDP'], marker='o')
    plt.title(f'GDP of {country} from 2000 to 2022')
    plt.xlabel('Year')
    plt.ylabel('GDP (in trillions)')
    plt.xticks(df_country['Year'], rotation=45)
    plt.grid(True)
    plt.show()