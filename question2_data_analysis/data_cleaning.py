import os
import pandas as pd

RAW_DATA_PATH = "question2_data_analysis/data/raw/" # Path to the raw scraped data
CLEANED_DATA_PATH = "question2_data_analysis/data/cleaned/" # Path to save the cleaned data

RATING_MAP = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5,
}

def clean_data(file_name: str):
    print("\n-- Cleaning Data ---")
    try:
        full_path = os.path.join(RAW_DATA_PATH, file_name)

        if os.path.isfile(full_path):
            df = pd.read_csv(full_path, encoding='utf-8-sig')

            # Before Cleaning
            print("-- Before Cleaning --")
            print(f"Initial Data Shape: {df.shape}")
            print("\nData Types:")
            print('-'*50)
            print(df.dtypes)
            print("\nData Summary:")
            print('-'*50)
            print(df.describe())
            print("\nNULL Data:")
            print('-'*50)
            print(df.isna().sum())
            
            # Price standardization (Remove '£' symbol, convert to float)
            df['price'] = df['price'].str.replace('£', '', regex=False).str.strip()
            df['price'] = pd.to_numeric(df['price'], errors='coerce')
            
            # Rating conversion: Convert text ratings to numeric (1-5)
            df['rating'] = df['rating'].map(RATING_MAP)
            
            # Handle missing data: Identify and address null values
            df['title'] = df['title'].fillna('Unknown')
            df['price'] = df['price'].fillna(df['price'].median())
            df['rating'] = df['rating'].fillna(df['rating'].median())
            df['category'] = df['category'].fillna('Unknown')
            df['availability'] = df['availability'].fillna('Unknown')
            
            # Remove duplicates
            df = df.drop_duplicates(keep='first')
            
            # Categorize Price
            df['price_category'] = pd.cut(
                df['price'], 
                bins=(0, 20, 40, float('inf')),
                right=False,
                labels=['Budget', 'Mid-range', 'Premium']
            ).astype(str)
            
            # Boolean based on availability
            df['in_stock'] = df['availability'].str.contains('In Stock', case=False, na=False)
            
            # Create the csv saving folder if it is not exist
            os.makedirs(CLEANED_DATA_PATH, exist_ok=True)
            output_file_path = os.path.join(CLEANED_DATA_PATH, 'cleaned_'+file_name)
            df.to_csv(output_file_path, index=False, encoding='utf-8-sig')
            
            print(df.head(5))
        else:
            raise FileNotFoundError(f"Can't find the {file_name} file at {RAW_DATA_PATH}")
        
    except Exception as e:
        print(f"Error: {e}")
    

if __name__ == "__main__":
    clean_data('books_data_500.csv')