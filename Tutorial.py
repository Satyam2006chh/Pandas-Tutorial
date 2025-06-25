# Hello EveryOne HERE we will be doing the Pandas

import pandas as pd
import numpy as np

# We are Starting By reading the CSV Files and for that I m including a csv file in repo

# df  = pd.read_csv('pandas.csv')
# print(df)


# What is basically a dataframe - ?

# A DataFrame is a two-dimensional, size-mutable and potentially heterogeneous tabular data structure with labeled axes (rows and columns).


# Now to write the data in the CSV -

# nme = ["aparna", "pankaj", "sudhir", "Geeku"]
# deg = ["MBA", "BCA", "M.Tech", "MBA"]
# scr = [90, 40, 80, 98]

# dict = {"Name":nme , "Degree":deg, "Score":scr}
# df.to_csv("file.csv")




# It will automatically create A csv to your folder




# Now Accessing the dataframe parts

data = {'Name': ['John', 'Alice', 'Bob', 'Eve',
'Charlie'], 
'Age': [25, 30, 22, 35, 28], 
'Gender': ['Male', 'Female', 'Male', 'Female', 'Male'], 
'Salary': [50000, 55000, 40000, 70000, 48000]}

df = pd.DataFrame(data)
# print(df)

# to access the age column
age_column = df["Age"]
print(age_column)

# if want to access multiple columns at a time 

print(df[['Name', 'Age']])



