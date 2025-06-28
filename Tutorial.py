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
# data = {
#     'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
#     'Age': [24, 27, 22, 32, None],
#     'Marks': [85, 90, 78, None, 88],
#     'Gender': ['F', 'M', 'M', 'M', 'F']
# }
# df = pd.DataFrame(data)

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


# Here we will use the new df

# data = {
#     'Name': ['Alice', 'Bob', 'Charlie', 'David'],
#     'Marks': [85, 92, 78, 88]
# }
# df = pd.DataFrame(data)

# Adding New column in df
# df['Subject'] = ['Math', 'Science', 'English', 'Math']

# ➕ Add a column with same value
# df['Passed'] = True

# 🎯 Increase marks by 5 for all students
# df['Marks'] = df['Marks'] + 5

# Now the most important part  - IS TO DROP A COLUMN

# df.drop('Passed', axis=1, inplace=True) 
# axis = 1 means column
# axis = 0 means row 
# if u dont write inplace  = True then after the drop command if u print the df it will again show u the dropped column so do inplace = true 

# ❌ Drop multiple columns:
# df.drop(['Subject', 'Grade'], axis=1, inplace=True)




# 📌 Topic 6: Indexing and Resetting Index 

# Now when we make a excel sheet basically there r the values like the 0,1,2--- and so on which r the indexes and now You wnt that a particular field in Your table must be inplace of the index means index  = 'Name' where Name is the column name 

# df.set_index('Name', inplace=True)
# print(df)

# for ex this -  Here Name is index 
#          Marks
# Name           
# Alice       85
# Bob         92
# Charlie     78
# David       88

# df.loc['Bob'] - This is valid now as 'Bob' is now the index 

# Output - 
# Marks    92
# Name: Bob, dtype: int64


# Now to make the index back to 0,1,2,3.... and so on

# df.reset_index(inplace=True)
# print(df)



# --------------------------------------------------------



# 🎯 Topic 7: Sorting Data in Pandas

#  1. Sort by Single Column-

# df.sort_values('Marks')- 📊 Sorted from lowest to highest marks.

# for the descending values  -
# df.sort_values('Marks', ascending=False)

# sorting of multiple columns -
# df.sort_values(['Age', 'Marks'])

# Multi-column with descending + ascending mix:
# df.sort_values(['Age', 'Marks'], ascending=[True, False])


# Sort by Index--

# df.sort_index() - Ascending

# df.sort_index(ascending=False) - Descending 

# # The most important point 

# Sort In-Place (modify original DataFrame)

# df.sort_values('Marks', ascending=False, inplace=True)


# --------------------------------------------------------

# 🎯 GOAL: Learn how to rename column names and row indexes with rename(), columns=, and index=

# FOR THIS WE R USING Another DF-

# data = {
#     'StudID': [101, 102, 103],
#     'Name ': ['Aman', 'Bobby', 'Chetan'],   # Notice extra space!
#     'Marks': [76, 89, 91]
# }

# df = pd.DataFrame(data)
# print(df)


# 'Name ' has a space 😒
# StudID is maybe better as ID

# To basicaLLY rename a specific column

# df.rename(columns={'StudID': 'ID', 'Name ': 'Name'}, inplace=True)
# print(df)


# to rename everything in one go for the columns
# df.columns = ['Student_ID', 'Student_Name', 'Score']



# Remove Spaces from All Column Names (Super Hack)
# df.columns = df.columns.str.strip()
# print(df)


# To rename the indexes
# df.index = ['Roll_1', 'Roll_2','Roll_3']
# print(df)



# -------------------------



# Handling Missing Data (NaN)



# Real data is NEVER clean. You’ll always run into:

# Blank cells
# NULL values
# NaN (Not a Number)
# Corrupted / incomplete data

# Handling this properly is the first step in real data science.


# data = {
#     'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
#     'Marks': [85, np.nan, 78, 88, np.nan],
#     'Subject': ['Math', 'Science', 'English', np.nan, 'Science']
# }

# df = pd.DataFrame(data)
# print(df)

# You can see:

# Bob & Eva have missing marks
# David has no subject

# Now to detect the missing data 

# print(df.isnull())
# it will  return true whereever the data is missing 

# print(df.isnull().sum())
# Count total missing in each column:

# To drop the missing data - along the rows 
# print(df.dropna())


# To drop the missing data - along the columns
# print(df.dropna(axis=1))


# 🧃Fill Missing Data (Imputation)
# df['Marks'].fillna(0, inplace=True)
# print(df)


# Fill missing marks with column average:
# avg= df['Marks'].mean()
# df['Marks'].fillna(avg,inplace=True)
# print(df)

# 🔹 Forward Fill (fill with previous row’s value):
# df.fillna(method='ffill', inplace=True)
# print(df)

# Backward Fill:
# df.fillna(method='bfill', inplace=True)

# 🧠 4. Replace Specific Values (Not just NaN)
# df.replace('Science', 'Sci', inplace=True)
# print(df)



# ====================================

# 🧩 Topic 11: Combining DataFrames (Concatenation + Merging)\

# Real projects? Real datasets? They never come in one nice table.
# You’ll often have data:

# Split across files
# Spread in multiple sheets
# In multiple related tables

# And your job?
# Combine it all together like a boss 💪🐼



# df1 = pd.DataFrame({
#     'ID': [1, 2, 3],
#     'Name': ['Alice', 'Bob', 'Charlie']
# })

# df2 = pd.DataFrame({
#     'ID': [4, 5],
#     'Name': ['David', 'Eva']
# })

# 🔹 1. Concatenation – Combine Vertically (Stacking)

# print(pd.concat([df1, df2], ignore_index=True))
# ignore_index=True gives clean index from 0

# otherwise index will look like - 0,1,2,0,1


# 🔸 Horizontal Concatenation (side by side)
# print(pd.concat([df1, df2], axis=1))
# ⚠️ Rows must match in count, or you'll get NaN.



# 🔹 2. Merging – Combine on a Key (Like SQL Join)\

# students = pd.DataFrame({
#     'ID': [1, 2, 3],
#     'Name': ['Alice', 'Bob', 'Charlie']
# })

# scores = pd.DataFrame({
#     'ID': [1, 2, 3],
#     'Marks': [85, 92, 78]
# })

# merged = pd.merge(students, scores, on='ID')
# print(merged)



# =============================================


# 🧠 Topic 12: Applying Functions with .apply() and lambda

# ✅ You can:

# Create new columns with logic
# Clean messy data
# Use if-else, math, text ops, etc.
# Apply your own functions row-wise or column-wise

# Sample df
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Marks': [92, 76, 89, 60]
})

# 🔹 1. Apply a Lambda Function to a Column
# ✅ Add a column 'Result' with Pass/Fail logic:

# df['Resultt'] = df['Marks'].apply(lambda x:'Pass' if x>=75 else 'Fail')
# print(df)


# 🔹 2. Create a Grading System
# def get_grade(m):
#     if m >= 90:
#         return 'A'
#     elif m >= 80:
#         return 'B'
#     elif m >= 70:
#         return 'C'
#     else:
#         return 'D'
    
# df['Grade'] = df['Marks'].apply(get_grade)
# print(df)


# 🔹 3. Apply on Multiple Columns (Use axis=1)
# df['Info'] = df.apply(lambda row: f"{row['Name']} scored {row['Marks']}", axis=1)



# 🔹 4. Modify String Columns
# ✅ Converts all names to uppercase.

# df['Name'] = df['Name'].apply(lambda x: x.upper())


# 🔹 5. Use .map() (shortcut for single-column transformation)/
# df['Result'] = df['Marks'].map(lambda x: 'Pass' if x > 75 else 'Fail')


# ===========================================


# Duplicate rows = same data multiple times
# And that means:

# Wrong average
# Wrong counts
# Fake outliers
# Bad analysis

# So your job? Detect + Remove like a pro 🧼

import pandas as pd

data = {
    'Name': ['Aman', 'Bobby', 'Aman', 'Divya', 'Eva', 'Eva'],
    'Subject': ['Math', 'Science', 'Math', 'Math', 'Science', 'Science'],
    'Marks': [85, 90, 85, 67, 88, 88]
}
df = pd.DataFrame(data)
