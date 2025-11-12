#!/bin/bash

# This script automates the execution of the entire data analysis pipeline for the Cryptocurrency Market Sentiment & Price Data 2025 dataset.

# Step 1: Load the data
echo "Loading data..."
python src/data/load_data.py

# Step 2: Preprocess the data
echo "Preprocessing data..."
python src/data/preprocess.py

# Step 3: Perform exploratory data analysis
echo "Starting exploratory data analysis..."
jupyter nbconvert --to notebook --execute notebooks/01-exploratory-data-analysis.ipynb --output-dir=notebooks/output

# Step 4: Feature engineering
echo "Performing feature engineering..."
jupyter nbconvert --to notebook --execute notebooks/02-feature-engineering.ipynb --output-dir=notebooks/output

# Step 5: Run sentiment analysis
echo "Running sentiment analysis..."
python src/analysis/sentiment_analysis.py

# Step 6: Train models
echo "Training models..."
python src/models/modeling.py

# Step 7: Evaluate models
echo "Evaluating models..."
# Assuming evaluation code is included in modeling.py or a separate script
python src/models/evaluate_models.py

# Step 8: Generate final report
echo "Generating final report..."
jupyter nbconvert --to markdown --execute notebooks/output/final_report.ipynb --output-dir=reports

echo "Pipeline execution completed!"