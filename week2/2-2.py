#2-2

import pandas as pd

purchase_1 = pd.Series({'Name': 'Chris',
						'Item Purchased': 'Dog Food',
						'Cost': 22.50})

purchase_2 = pd.Series({'Name': 'Kevyn',
						'Item Purchased': 'Kitty Litter',
						'Cost': 2.50})

purchase_3 = pd.Series({'Name': 'Vinod',
						'Item Purchased': 'Bird Seed',
						'Cost': '5.00'})

df = pd.DataFrame([purchase_1, purchase_2, purchase_3], index = ['Store 1', 'Store 1', 'Store 2'])
print df.head()

# HOW TO APPLY A DISCOUNT OF %20 BELOW???
# This works in Jupyter Notebook, but it does NOT work here.
#TypeError: can't multiply sequence by non-int of type 'float'
df['Cost']*= .8
print df

#To obtain Store 2 data only...
print df.loc['Store 2']

#check what type of data is returned
print type(df.loc['Store 2'])

#df = pd.DataFrame([purchase_1, purchase_2, purchase_3], index=['Store 1', 'Store 1', 'Store 2'])

# Just show the store and cost data
print df.loc['Store 1', 'Cost']

# 'T' stands for transpose; swaps the columns and rows. TURNS COLUMN NAMES INTO INDICES
print df.T

print df.T.loc['Cost']





df['Name']
print df.head()

                        
#WHAT IS THE PURPOSE OF THE INDEX CALL AT THE END???
df = pd.DataFrame([purchase_1, purchase_2, purchase_3], index=['Store 1', 'Store 1', 'Store 2'])

#how to get a list of all items that were purchased from and details?
print df['Item Purchased']


#way of selectively extracting data
print df.loc['Store 1', 'Cost']

print df.T
#transpose display of data

print df.T.loc('Cost')
print
# chain information together; avoid this!!!
# disadvantage: Pandas returns a copy rather than a view on the df
print df.loc['Store 1'] ['Cost']
print

# extract ALL of the Cost at ALL of the Stores. NOTE: SLICING IS SUPPORTED!!!
print df.loc[:, ['Name', 'Cost']]

# To delete data use the 'drop' function
print
print "Drop Store 1"
print df.drop('Store 1') # BE CAREFUL!
print

# following method deletes it from copy view
copy_df = df.copy()
print "copy_df = copy_df.drop('Store 1')"
copy_df = copy_df.drop('Store 1')
print copy_df
print
# following methods deletes it immediately for good
del copy_df['Name']
print "Delete method (del copy_df['Name'], is irreversible."
print copy_df
print

# ADD A NEW COLUMN
df['Location'] = None
print "New column, Location, was added."
print df