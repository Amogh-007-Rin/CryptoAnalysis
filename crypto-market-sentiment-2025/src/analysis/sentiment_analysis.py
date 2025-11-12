import pandas as pd
from textblob import TextBlob
import numpy as np

def load_sentiment_data(file_path):
    """
    Load sentiment data from a CSV file.
    
    Parameters:
    file_path (str): The path to the sentiment data CSV file.
    
    Returns:
    DataFrame: A pandas DataFrame containing the sentiment data.
    """
    return pd.read_csv(file_path)

def analyze_sentiment(text):
    """
    Analyze the sentiment of a given text using TextBlob.
    
    Parameters:
    text (str): The text to analyze.
    
    Returns:
    float: The polarity score of the text.
    """
    return TextBlob(text).sentiment.polarity

def add_sentiment_scores(df, text_column):
    """
    Add sentiment scores to the DataFrame based on the specified text column.
    
    Parameters:
    df (DataFrame): The DataFrame to which sentiment scores will be added.
    text_column (str): The name of the column containing text data.
    
    Returns:
    DataFrame: The DataFrame with an additional column for sentiment scores.
    """
    df['sentiment_score'] = df[text_column].apply(analyze_sentiment)
    return df

def main():
    # Load the sentiment data
    sentiment_data = load_sentiment_data('data/processed/sentiment_data.csv')
    
    # Add sentiment scores to the DataFrame
    sentiment_data = add_sentiment_scores(sentiment_data, 'text')
    
    # Save the updated DataFrame with sentiment scores
    sentiment_data.to_csv('data/processed/sentiment_data_with_scores.csv', index=False)

if __name__ == "__main__":
    main()