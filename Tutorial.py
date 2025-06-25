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


# df.iloc[1:3]
# rows at index 1 and 2 


# df.loc[1:3]
# rows at index 1 and 2 and 3 too



# Conditional Accessing 
# df[(df['Marks'] > 80) & (df['Gender'] == 'M')]



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

# 2- df.tail(n)
# it will give u the last n rows 

# print(df.shape)
# it will give u the size of the df
# means for the above df it will give u the output as (5,4)
# where 5 is rows and 4 is columns 


# print(df.columns) - 
# it will list all the columns of the df 

# print(df.index)-
# it will tell u the range of your index 0 to N by default 

# print(df.dtypes)
# Will give You the Data Type of Each Column


# print(df.info())
# Will give u the full summary of Your df

# MOST USED 
# df.describe();
# it will give u the statistical summary of numbers only 


# print(df.isnull().sum())
# it will check for the missing values for the df 



# Filtering Of data using Conditions in df 
# ✅ Students with marks > 80
# df[df['Marks'] > 80]

# ✅ Students who study Math
# df[df['Subject'] == 'Math']

# 🔗 AND Condition: Both must be True
# df[(df['Marks'] > 80) & (df['Gender'] == 'M')]

# 🔗 OR Condition: At least one must be True
# df[(df['Marks'] > 90) | (df['Subject'] == 'Math')]


# 📌 Using .query() – Cleaner Syntax for Conditions
# df.query("Marks > 80 and Subject == 'Math'")




# 🧩 Topic 5: Adding, Updating, and Deleting Columns