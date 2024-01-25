#!/usr/bin/env python3
# Libraries
import streamlit as st
import subprocess
import csv
import getopt
import os
import sys

import pandas as pd

def queryWord(column, dataframe, columnList):
    st.write("The string you want to query is case-sensitive.")
    string = st.text_input("Input the string you want to query: ")
    #dataframe.contains(word)
    # Use str.contains to filter the DataFrame
    filtered_df = dataframe[dataframe[column].str.contains(string, regex=True, na=False)]
    
    if not filtered_df.empty:
        st.write("ROW LIST:")
        num = 0
        for colWord in columnList:
            num = num + 1
            st.write(str(num) + ": " + colWord)
        st.write("Place the number for each column you want printed for each iteration of " + string + " found.")
        st.write("Delimit each number by a comma. Spaces are ignored. Place a -1 if you want all of the columns printed.")
        values = input("Your input: ")
        values = values.replace(" ", "")
        values = values.split(",")
        fixedValues = []
        if values == -1:
            st.write("Printing all values found in the same row as " + string)
        else:
            for val in values:
                if val.isdigit():
                    if int(val) >= 1 and int(val) <= num:
                        fixedValues.append(int(val) - 1)
                    else:
                        st.write("The value " + val + " is out of bounds and will be ignored")
                else:
                    st.write("The value " + val + " is illegal and will be ignored.")
       
        for index, row in filtered_df.iterrows():
            if fixedValues != []:
                for i in fixedValues:
                    st.write(row[i])
            else:
                st.write(row)

            st.write()

    else:
        st.write("Not found")


