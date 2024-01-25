#!/usr/bin/env python3
# Libraries
import streamlit as st
import subprocess
import csv
import getopt
import os
import sys

import pandas as pd

def findValueInRange(column, dataframe, userInp):
    st.write("The range calculated here includes both of the end parts of the range. I.e. [2,5] will count all values that are 2, or 5")
    st.write("Decimals are supported")
    lowestVal = st.text_input("Input your lowest value here: ")
    highestVal = st.text_input("Input your highest value here: ")
    while not lowestVal.isdigit() and not highestVal.isdigit():
        lowestVal = st.text_input("Input your lowest value here: ")
        highestVal = st.text_input("Input your highest value here: ")
    
    st.write("Your csv file may be far too long to iterate through to find matching values.")
    certainRange = st.text_input("Input a max (positive) line value that the function will abort once reached: ")
    while not certainRange.isdigit():
        certainRange = st.text_input("Input a max (positive) line value that the function will abort once reached: ")
    certainRange = int(certainRange)
    for row in range(len(dataframe)):
        certainRange -= 1
        val = dataframe.iloc[row, userInp]
        if str(val).isdigit():
            if float(val) >= float(lowestVal) and float(val) <= float(highestVal):
                st.write(dataframe.loc[row])
        if certainRange == 0:
            break

