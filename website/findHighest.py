#!/usr/bin/env python3
# Libraries
import streamlit as st
import subprocess
import csv
import getopt
import os
import sys

import pandas as pd

# Function to find and print the row with the highest value in a DataFrame for a specific column
# Function to find and print the row with the highest value in a DataFrame for a specific column
def findHighest(df, column_name):
    if not pd.api.types.is_numeric_dtype(df[column_name]):
        st.write(f"Error: The column '{column_name}' does not contain numeric values.")
        return

    highest_index = df[column_name].idxmax()
    highest_row = df.loc[highest_index]

    st.write("\n")
    st.write(f"{column_name}: {highest_row[column_name]}")  # Print the specified column value first
    st.write("\n")
    for column in df.columns:
        st.write(f"{column}: {highest_row[column]}")
