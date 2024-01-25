#!/usr/bin/env python3
# Libraries
import csv
import getopt
import os
import sys

import pandas as pd
# Function to find and print the row with the highest value in a DataFrame for a specific column

# Function to find and print the row with the highest value in a DataFrame for a specific column
def findHighest(file_path, column_name):
    df = pd.read_csv(file_path)  # Read the CSV file using the file path

    if not pd.api.types.is_numeric_dtype(df[column_name]):
        print(f"Error: The column '{column_name}' does not contain numeric values.")
        return

    highest_index = df[column_name].idxmax()
    highest_row = df.loc[highest_index]

    print("\n")
    print(f"Highest value in {column_name}: {highest_row[column_name]}")  # Print the specified column value first
    print(f"{column_name}: {highest_row[column_name]}")  # Print the specified column value first
    print("\n")
    for column in df.columns:
        print(f"{column}: {highest_row[column]}")

        print(f"{column}: {highest_row[column]}")
