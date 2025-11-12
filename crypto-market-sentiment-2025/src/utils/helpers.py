def load_data(file_path):
    import pandas as pd
    """Load dataset from the specified file path."""
    try:
        data = pd.read_csv(file_path)
        print(f"Data loaded successfully from {file_path}")
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def preprocess_data(data):
    """Preprocess the dataset by handling missing values and normalizing."""
    # Handle missing values
    data.fillna(method='ffill', inplace=True)
    
    # Normalize numerical features
    from sklearn.preprocessing import MinMaxScaler
    scaler = MinMaxScaler()
    numerical_cols = data.select_dtypes(include=['float64', 'int64']).columns
    data[numerical_cols] = scaler.fit_transform(data[numerical_cols])
    
    print("Data preprocessing completed.")
    return data

def visualize_data(data, column):
    """Visualize the specified column of the dataset."""
    import matplotlib.pyplot as plt
    import seaborn as sns
    
    plt.figure(figsize=(10, 6))
    sns.histplot(data[column], bins=30, kde=True)
    plt.title(f'Distribution of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.show()

def calculate_metrics(y_true, y_pred):
    """Calculate and return evaluation metrics."""
    from sklearn.metrics import mean_squared_error, r2_score
    
    mse = mean_squared_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)
    
    return {'MSE': mse, 'R2': r2}

def save_results(results, file_path):
    """Save results to a specified file path."""
    import json
    try:
        with open(file_path, 'w') as f:
            json.dump(results, f)
        print(f"Results saved successfully to {file_path}")
    except Exception as e:
        print(f"Error saving results: {e}")