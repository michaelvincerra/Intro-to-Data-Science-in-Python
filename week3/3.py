#coding: utf-8

import pandas as pd

df = pd.DataFrame([{'Name': 'Chris', 'Item Purchased' : ' Sponge', 'Cost': 22.50},
                   {'Name': 'Kevyn', 'Item Purchased': 'Kitty Litter', 'Cost': 2.50},
                   {'Name': 'Filip', 'Item Purchased' : ' Spoon', 'Cost': 5.00}],
                    index = ['Store 1', 'Store1', 'Store 2'])

#NOTE: ABOVE STRUCTURE USES DICTIONARY KEYS--SYNTAX

# We can add a new column, Date, we use the [] brackets on the rest of the dataframe as long as the column is as long as the rest of the records.


df['Date'] = ['December 1', 'January 1', 'mid-May']

df['Delivered']= True

# In order to match the structure of DataFrame, we have to input 'None' values.

df["Feedback"]= ['Positive', 'None', 'Negative']


#NOTE! When Dr. Brooks resets the INDEX, he does this on ONE line first. Thereafter, he MATCHES the new INDEX numbers 0 and 2 to the dates as desired;
# THEREFORE 1: is implied!!!!---It outputs as "NaN"

df1 = df.reset_index()
df1['Date'] = pd.Series({0:'December 1', 2:'mid-May'})

print df1