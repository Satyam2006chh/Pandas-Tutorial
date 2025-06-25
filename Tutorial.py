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

# 

# print(df)

# to access the age column


# age_column = df["Age"]
# print(age_column)

# if want to access multiple columns at a time 

# print(df[['Name', 'Age']])

# Now accessing the rows of the df

# print(df.iloc[0])
# print(df.loc[0])

# here whats the difference between the loc and the iloc - 
# iloc -  It uses the integer location where 0 is the first row
# loc - It uses the label location 
# where 0 is the row with index 0


# to understand better of the iloc and the loc 

# a   Alice     85
# b     Bob     92
# c Charlie     78

# suppose this is the dataframe 

# df.iloc[0] means the first row that is alice row 
# even though the label is a , but iloc[0] means first row no matter what the label is 

# df.loc['a'] - means that get the row with the label 'a' however output of above and this will be same 



# Accessing the Cell means row and column through the loc and the iloc 

# print(df.iloc[1,0])
# means second row and the first column that is 'Bob'

# print(df.loc['b','Name'])
# Row label 'b', column 'Name' ➝ 'Bob'



# Inspecting the data -

# here we r using another dataframe as per as the requirements
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [24, 27, 22, 32, None],
    'Marks': [85, 90, 78, None, 88],
    'Gender': ['F', 'M', 'M', 'M', 'F']
}
df = pd.DataFrame(data)

# 1- df.head(n)
# it will get u the first n rows 
# by default the value of the n = 5;