
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

df = df.drop('Totals')


def answer_four():

    df['Points'] = df['Gold.2'] * 3 + df['Silver.2'] * 2 + df['Bronze.2'] * 1
    df['Points'] = pd.Series('Points')
    return len(df['Points']) #.dropna())
    #s = df['Gold.2']*3 + df['Silver.2']*2 + df['Bronze.2']*1
    #s = pd.Series(['Points'], index=['Gold', 'Silver', 'Bronze'])

    #return len(pd.Series['Points']) #.dropna())

print answer_four()

    # The function should return ONLY the column (a Series Object) that you created.

    #Points = ['Gold.2', 'Silver.2', 'Bronze.2']

    #df1 = pd.Series('Points')
    # #df1 = df1.loc[:, 'Points'] = Points

    #df.assign(Points = df['Gold.2'] = 3 + df['Silver.2'] = 2 +  df['Bronze.2'] = 1)


    #df['Gold.2'] = 3
    #df['Silver.2'] = 2
    #df['Bronze.2'] = 1

#df = df.drop('Totals')



#PREVIOUS ANSWER 03.26.17
#def answer-four():
#   df['Points'] = df['Gold.2']*3 + df['Silver.2']*2 + df['Bronze.2']*1
#    return len(df['Points']) #.dropna())
#print answer_four()
#PREVIOUS ANSWER