#!/usr/bin/env python3
import streamlit as st
import pandas as pd
import matplotlib as plt
from findHighest import findHighest
from findLowest import findLowest
from findValueInRange import findValueInRange
from queryWord import queryWord
from subsetGraph import subsetGraph

"""
# CSV Search Engine

Made for your convenience
"""

# Allowing the user to upload a CSV file
uploaded_file = st.file_uploader("Upload a CSV File", type=["csv"])

if uploaded_file is not None:
    st.success("CSV file uploaded successfully!")

    # Reading the CSV into a DataFrame
    df = pd.read_csv(uploaded_file)
    st.write("Columns in the CSV file:")
    columnChoice = st.selectbox("Select a column:", df.columns)

    # Displaying a confirmation message
    st.success("Script execution completed successfully!")

    # Main Menu
    st.write("Main Menu:")
    option = st.selectbox("Select an option:", ["", "Find the highest Numerical Value", "Find the lowest Numerical Value", "Find a value in a certain range", "Graph a subset of the dataset", "Query a word into the column"])

    if st.button("Go"):
        if option == "Find the highest Numerical Value":
                st.write("Result of Find Highest Numerical Value:")
                findHighest(df, columnChoice)
        elif option == "Find the lowest Numerical Value":
            st.write("Result of Find Lowest Numerical Value:")
            findLowest(uploaded_file, df[columnChoice])
        elif option == "Find a value in a certain range":
            st.write("Result of Find Value in Certain Range:")
            findValueInRange(df[columnChoice], df, df[columnChoice].index)
        elif option == "Graph a subset of the dataset":
            st.write("Result of Subset Graph:")
            # Ask for inputs here
            startPoint = st.number_input("Enter the starting row for the graph:", min_value=0, max_value=len(df) - 1)
            endPoint = st.number_input("Enter the ending row for the graph:", min_value=0, max_value=len(df) - 1)

            st.write(f"Received startPoint: {startPoint}, endPoint: {endPoint}")  # Debugging output

            if st.button("Generate Graph"):
                subset = subsetGraph(df, startPoint, endPoint)
                
                if subset is not None:
                    st.pyplot(plt.figure())
                    plt.plot(subset)
                    plt.title(f"Subset of Column: {df.columns[0]}")
                    plt.xlabel("Rows " + str(startPoint) + "-" + str(endPoint))
                    plt.ylabel("Value")
                    plt.legend([df.columns[0]])
                    st.pyplot(plt)

            
        elif option == "Query a word into the column":
            st.write("Result of Query a Word:")
            queryWord(df[columnChoice], df, df.columns)
