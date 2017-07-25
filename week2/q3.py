# coding: utf-8
import pandas as pd


df = pd.read_csv('olympics.csv', index_col = 0, skiprows=1)

 
for col in df.columns:
    if col[:2]=='01':
        df.rename(columns={col:'Gold' + col[4:]}, inplace=True)
    if col[:2]=='02':
        df.rename(columns={col:'Silver' + col[4:]}, inplace=True)
    if col[:2]=='03':
        df.rename(columns={col:'Bronze' + col[4:]}, inplace=True)
    if col[:1]=='№':
        df.rename(columns={col:'#' + col[1:]}, inplace=True)

#names_ids = df.index.str.split('\s\(') # split the index by '('


#df = df.drop('Totals')
#df.head()

#def answer_three():

#df1 = (df['Gold'] - df['Gold.1']).abs() / ((df['Gold.2']))
  #  return df1.idxmax()

   #if (df['Gold.2']).idxmax() > (df['Gold'] - df['Gold.1']).abs():
#    return (df['Gold.2']).idxmax()
    #else:
    #   return

#df = len(df['Gold']  | df['Gold.1'])


#STUDY THE STRUCTURE BELOW

#print df

# Find the maximum difference
def answer_three():

    df1 = df[(df['Gold'] >= 1) & (df['Gold.1'] >= 1)] #/ df['Gold.2'].max()

    df2 = df[(df1.max() - df1.min())]
    #
    df2 = df[(df1.max() - df1.min())]

    return df2


    #/ df['Gold.2'].idxmax()

    #return df2
    #df2.reset_index()
    #return df2.iloc[0]['ID']
    #df2 = df1 / df['Gold.2']
    #df2 = df1.abs() / df['Gold.2']
    #return df2.max()

print answer_three()

#answer_three()