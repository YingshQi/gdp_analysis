# load the data
import pandas as pd

def load_data(data_path: str) -> pd.DataFrame:   
    try:
        df = pd.read_excel(data_path)
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

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
load_data("D:\24fall\D100\ps1\GDP_analysis\data\gdp_data.xlsx")