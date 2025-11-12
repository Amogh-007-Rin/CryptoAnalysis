import pandas as pd
import os

def load_data(file_name):
    """
    Load the cryptocurrency market sentiment and price data from the raw directory.

    Parameters:
    file_name (str): The name of the file to load.

    Returns:
    DataFrame: A pandas DataFrame containing the loaded data.
    """
    raw_data_path = os.path.join('data', 'raw', file_name)
    
    if not os.path.exists(raw_data_path):
        raise FileNotFoundError(f"The file {file_name} does not exist in the raw data directory.")
    
    # Load the dataset
    data = pd.read_csv(raw_data_path)
    
    return data

def main():
    # Example usage
    try:
        data = load_data('cryptocurrency_sentiment_2025.csv')
        print("Data loaded successfully.")
        print(data.head())
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()