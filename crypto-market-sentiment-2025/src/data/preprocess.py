import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.impute import SimpleImputer

def load_data(file_path):
    """Load the dataset from the specified file path."""
    data = pd.read_csv(file_path)
    return data

def clean_data(data):
    """Clean the dataset by handling missing values and duplicates."""
    # Remove duplicates
    data = data.drop_duplicates()
    
    # Handle missing values
    imputer = SimpleImputer(strategy='mean')
    data.iloc[:, :] = imputer.fit_transform(data)
    
    return data

def normalize_data(data):
    """Normalize the dataset using Min-Max scaling."""
    scaler = MinMaxScaler()
    normalized_data = scaler.fit_transform(data)
    return pd.DataFrame(normalized_data, columns=data.columns)

def preprocess_data(file_path):
    """Main function to preprocess the data."""
    # Load data
    data = load_data(file_path)
    
    # Clean data
    data = clean_data(data)
    
    # Normalize data
    data = normalize_data(data)
    
    return data

if __name__ == "__main__":
    # Example usage
    file_path = '../data/raw/cryptocurrency_data_2025.csv'  # Adjust the path as necessary
    processed_data = preprocess_data(file_path)
    processed_data.to_csv('../data/processed/processed_data_2025.csv', index=False)