#coding: utf-8
  import pandas as pd
import numpy as np

df = pd.read_csv('olympics.csv', index_col=0, skiprows=1)

for col in df.columns:
    if col[:2] == '01':
        df.rename(columns={col: 'Gold' + col[4:]}, inplace=True)
    if col[:2] == '02':
        df.rename(columns={col: 'Silver' + col[4:]}, inplace=True)
    if col[:2] == '03':
        df.rename(columns={col: 'Bronze' + col[4:]}, inplace=True)
    if col[:1] == '№':
        df.rename(columns={col: '#' + col[1:]}, inplace=True)

#gold_summ = 0
#gold_wint = 0


# Find the maximum difference
#def answer_three():
    #df1 = df[(df['Gold'] >= 1) & (df['Gold.1'] >= 1)]  # / df['Gold.2'].max()
    #df2 = df[(df1.max() - df1.min())]
    # #df2 = df[(df1.max() - df1.min())]
    #if df['Gold'] >= 1:
     #   for i in gold_summ:
      #      i = i + gold_summ
      #  return df['Gold'].max()

    # ORIGINAL df1 = df[(df["Gold"] >= 1) | (df["Gold.1"] >= 1)]

    #df = df.groupby(df['Gold']>=1)&(df['Gold.1']>=1).agg(['max', 'min']).diff(axis=1)

    #df1 = df[(df('Gold'] > 0) & (df['Gold.1'] > 0)]
    #df1['delta'] = (df1['Gold'] >= 1) - (df['Gold.1'] >= 1]).abs() / df['Gold.2']

    #return ((df1['Gold'] - df1['Gold.1']) / df1['Gold.2']).argmax()

#PREVIOUS ANSWER 03.26.17
#def answer_three():
    #df1 = df[(df['Gold'] >=1) & (df['Gold.1'] >=1)]
    #return ((df1['Gold'] - df1['Gold.1']) / df1['Gold.2']).idxmax()
    #previous answer: "Bulgaria"
#PREVIOUS ANSWER

def answer_three():
    df1 = df[df['Gold']>0]
    df2 = df[df['Gold.1']>0]

    df2 = df1[df1['Gold.1']>0]

    summer_gold = df2['Gold']
    winter_gold = df2['Gold.1']

    total = summer_gold + winter_gold

    percent = (summer_gold - winter_gold) / total

    return percent[percent == max(percent)].index[0]

print answer_three()


    #df1 = df[(df['Gold']>=1).max() & (df['Gold.1']>=1).min() / df['Gold.2'].max()
    #df1 = (df['Gold']-df['Gold.1']).abs()/ df['Gold.2']

    #df2 = df['Gold'].max() - df['Gold.1'].min()

    # for each country, find the GREATEST DIFFERENCE btw Summer Gold medals and Winter gold medals


 #   return df1


#def answer_three():
#   largest = None

#    for item in df["Gold"]:
#        if largest is None or item > largest:
#             # following line is ingenious; it equates the largest with the itervar, but only if the itervar > "largest seen so far
#            largest = item
#            return item, largest


#print answer_three()


#== df.max() and
    #return df


#answer_three()