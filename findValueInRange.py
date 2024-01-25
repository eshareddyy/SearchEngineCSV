#!/usr/bin/env python3
# Libraries
import subprocess
import csv
import getopt
import os
import sys

import pandas as pd

def findValueInRange(column, dataframe, userInp):
    print("The range calculated here includes both of the end parts of the range. I.e. [2,5] will count all values that are 2, or 5")
    print("Decimals are supported")
    lowestVal = input("Input your lowest value here: ")
    highestVal = input("Input your highest value here: ")
    while not lowestVal.isdigit() and not highestVal.isdigit():
        lowestVal = input("Input your lowest value here: ")
        highestVal = input("Input your highest value here: ")
    
    print("Your csv file may be far too long to iterate through to find matching values.")
    certainRange = input("Input a max (positive) line value that the function will abort once reached: ")
    while not certainRange.isdigit():
        certainRange = input("Input a max (positive) line value that the function will abort once reached: ")
    certainRange = int(certainRange)
    for row in range(len(dataframe)):
        certainRange -= 1
        val = dataframe.iloc[row, userInp]
        if str(val).isdigit():
            if float(val) >= float(lowestVal) and float(val) <= float(highestVal):
                print(dataframe.loc[row])
        if certainRange == 0:
            break

