#!/usr/bin/env python3
# Libraries
import subprocess
import csv
import getopt
import os
import sys

import pandas as pd

from findHighest import findHighest
from findLowest import findLowest
from subsetGraph import subsetGraph
from queryWord import queryWord
from findValueInRange import findValueInRange

#prompting the user for command line input
def main( argv ):
  #splitting command line based on spaces
  path = argv

  if filename != None:
    if os.path.isfile(path):
      setNewDelim = input("Do you want to set a custom delimiter? Y for Yes, N for No: ")
      userDelim = None
      if setNewDelim.upper() == 'Y':
        print ("Set the delimiter")
        userDelim = input("Delimiter: ")
      else:
        userDelim = ','

    else:
      print("Nonexistent file. Exitting!")
      sys.exit(2)
  else:
    print("Filename has not been set. Exitting!")
    sys.exit(2)

  file = pd.read_csv(path, delimiter = userDelim)
  #printing all the columns which exist
  columnList = file.columns.tolist()
  num = 0
  print ("Columns: ")
  #print (file.columns.tolist())
  for column in columnList:
    num = num + 1
    print("\n" + str(num) + ": " + column)

  while True:
    int(num)
    userInp = -1
    userInp = int(input("Which column would you like to learn more about? "))
      
    if userInp >= 0 or userInp <= num:
      columnChoice = columnList[userInp - 1]
      print ("You chose column: " + columnChoice)
      df = file[columnChoice]
  
      while True: 
        print ("What would you like to see for the chosen column?\n")
        print ("1. Find the highest Numerical Value")
        print ("2. Find the lowest Numerical Value")
        print ("3. Find a value in a certain range")
        print ("4. Graph a subset of the dataset")
        print ("5. Query a word into the column")
        print ("0. Choose a different column")
        print ("11. To exit")
        actionChoice = input("\nWhat would you like to see for the chosen column? ")
        if (actionChoice.isdigit() == True):
          #pass (column, dataframe) in that order
          if int(actionChoice) == 1:
            findHighest(filename, columnChoice)
          elif int(actionChoice) == 2:
            findLowest(filename, columnChoice)
          elif int(actionChoice) == 3:
            findValueInRange(columnChoice, file, userInp - 1)
          elif int(actionChoice) == 4:
            subsetGraph(df)
          elif int(actionChoice) == 5:
            queryWord(columnChoice, file, columnList)
        
          elif int(actionChoice) == 0:
            num = 0
            for column in columnList:
              num = num + 1
              print("\n" + str(num) + ": " + column)
            break
          elif int(actionChoice) == 11:
            sys.exit(2)
          
        else:  
          print("Invalid choice!")
          
    else:
      print ("Invalid column choice :(")
    
if __name__ == "__main__":
  if len(sys.argv) != 2:
    print ("Usage: python main.py <path>")
    sys.exit(1)

  filename = sys.argv[1]
  main(filename)



