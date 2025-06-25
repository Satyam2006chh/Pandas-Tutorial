# Hello EveryOne HERE we will be doing the Pandas

import pandas as pd
import numpy as np

# We are Starting By reading the CSV Files and for that I m including a csv file in repo

df  = pd.read_csv('pandas.csv')
print(df)


# What is basically a dataframe - ?

# A DataFrame is a two-dimensional, size-mutable and potentially heterogeneous tabular data structure with labeled axes (rows and columns).


# Now to write the data in the CSV -

nme = ["aparna", "pankaj", "sudhir", "Geeku"]
deg = ["MBA", "BCA", "M.Tech", "MBA"]
scr = [90, 40, 80, 98]

dict = {"Name":nme , "Degree":deg, "Score":scr}
df.to_csv("file.csv")

# It will automatically create A csv to your folder
