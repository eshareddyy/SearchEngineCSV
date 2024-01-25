#!/usr/bin/env python3
import sys
import getopt
import pandas as pd
import matplotlib.pyplot as plt

def subsetGraph(df):
    try:
        startPoint = int(input("Enter the starting row for the graph: "))
        endPoint = int (input("Enter the ending row for the graph: "))
    
        if startPoint < 0 or endPoint > len(df) or startPoint > endPoint:
            print ("Invalid Row Range")
            return

        subset = df.iloc[startPoint:endPoint + 1]

        if subset.apply(lambda x: pd.to_numeric(x, errors='coerce')).notna().all():
            plt.plot(subset)
            plt.title(f"Subset of Column: {df.name}")
            plt.xlabel("Rows " + str(startPoint) + "-" + str(endPoint))
            plt.ylabel("Value")
            plt.legend([df.name])

            plt.show()
        else:
            print("Selected column contains non numeric values")

    except ValueError:
        print ("Invalid input")