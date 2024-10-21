# load the data
import pandas as pd

def load_data(data_path: str) -> pd.DataFrame:   
    try:
        df = pd.read_excel(data_path)
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

data_path = r"C:\Users\yings\Onedrive\桌面\D100\gdp_data.xlsx"
gdp_data = load_data(data_path)

print(gdp_data.head())


#clean the data
import pandas as pd

def clean_gdp_data(df: pd.DataFrame) -> pd.DataFrame:
  
    try:
        # Melt the data from wide to long format
        df_melted = df.melt(id_vars=["Country Name"], var_name="Year", value_name="GDP")
        
        # Convert the 'Year' column to integer
        df_melted["Year"] = df_melted["Year"].astype(int)
        
        # Check for and handle missing values (if any)
        df_clean = df_melted.dropna()
        
        return df_clean
    except Exception as e:
        print(f"Error cleaning data: {e}")
        return None

# Assuming your loaded data is called `gdp_data`
cleaned_gdp_data = clean_gdp_data(gdp_data)

# Display the first few rows of the cleaned data
print(cleaned_gdp_data.head())