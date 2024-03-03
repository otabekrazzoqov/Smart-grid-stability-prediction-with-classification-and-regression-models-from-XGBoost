"""              Pandas - Analyzing DataFrames           """

"""


Viewing the Data

One of the most used method for getting a quick overview of the DataFrame, 
is the head() method.
The head() method returns the headers and a specified number of rows, 
starting from the top.

"""

# Get a quick overview by printing the first 10 rows of the DataFrame:

    
import pandas as pd
df = pd.read_csv('data.csv')
print(df.head(10))


print("--------------------------------------")

# Print the first 5 rows of the DataFrame:

import pandas as pd
df = pd.read_csv('data.csv')
print(df.head())




# There is also a tail() method for viewing the last rows of the DataFrame.
# The tail() method returns the headers and a specified number of rows, 
# starting from the bottom.

# Print the last 5 rows of the DataFrame:

print(df.tail())



# The DataFrames object has a method called info(), 
# that gives you more information about the data set.

# Print information about the data:

print(df.info())





# Null Values

"""
The info() method also tells us how many Non-Null 
values there are present in each column, and in our data set 
it seems like there are 164 of 169 Non-Null values in the "Calories" column.
Which means that there are 5 rows with no value at all, 
in the "Calories" column, for whatever reason.

Empty values, or Null values, can be bad when analyzing data, 
and you should consider removing rows with empty values. 
This is a step towards what is called cleaning data, and you will 
learn more about that in the next chapters.

"""




 