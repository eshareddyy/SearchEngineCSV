#!/usr/bin/env python3
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def subsetGraph(df, startPoint, endPoint):
    try:
        st.write(f"startPoint: {startPoint}, endPoint: {endPoint}")  # Debugging output
        
        if startPoint < endPoint:
            subset = df.iloc[startPoint:endPoint + 1]

            if subset.apply(lambda x: pd.to_numeric(x, errors='coerce')).notna().all():
                return subset  # Return the subset DataFrame

            else:
                st.warning("Selected column contains non-numeric values.")

        else:
            st.error("Invalid row range. The starting row should be less than the ending row.")

    except ValueError:
        st.error("Invalid input")
