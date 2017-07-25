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
df = df.drop('Totals')


#names_ids = df.index.str.split('\s\(') # split the index by '('


# df = len(df[(df["Gold"]>0) | df["Gold.1"]>0])

#largest = 0
#smallest = 0


#def answer_two():
#    for number in df[(df["Gold"]>0)]:
#        if largest is 0 or number > largest:
#            largest = largest + 1
#        return largest

#print answer_two()


def answer_two():
    #df1 - create a new dataframe;
    #Use parens around sum product of subtraction of (Gold - Gold.1).abs() AND return its absolute value.
    # Then divide subtraction sum by the TOTAL amount of gold medals, Gold.2
    #df1 = (df['Gold']-df['Gold.1']).abs()/ df['Gold.2']
    # next return the new dataset that shows the max value
    #return df1.idxmax()

    #gold_summer = df['Gold']
    #gold_winter = df['Gold.1']
    #diff = gold_summer - gold_winter
    #return diff[diff == max(diff)].index[0]


    df1 = df['Gold'] - df['Gold.1']
    return df1[df1 == max(df1)].index[0]


print answer_two()


# ALT version: DOESN'T WORK!!
#largest = 0
#smallest = 0

#def answer_twoo():
#    for number in df[df['Gold']>0]:
#        if largest is None or number > largest:
#            largest = largest + 1
#    print largest

#    for number in df[df['Gold.1']>0]:
#        if smallest is None or number < smallest:
#            smallest = number
#    print smallest
#print largest - smallest


#def answer_three1():
#    _df = df[(df['Gold'] > 0) & (df['Gold.1'] > 0)]

#    return ((_df['Gold'] - _df['Gold.1']) / _df['Gold.2']).argmax() answer_three()

#print  answer_three1()


#print df


#def  answer_two():
    #  most_gold = df[df['Gold'] > 0]
    #least_gold = df[df['Gold.1']








#df = df.drop('Totals')
#df.head()

#def answer_zero():
#	(df['Gold'] - df['Gold.1'])
#	answer_zero.idxmax()

#print answer_zero()

#largest = 0
#smallest = 0


#def answer_two():

#  for number in df['Gold']>0:
#      if largest is 0 or number > largest:
#            largest = largest + 1
#            #df['Gold'].max()

#    for number in df(['Gold.1']>0):
#        if smallest is 0 or number < smallest:
#            smallest = number
#            #df['Gold.1'].min()

#    return largest - smallest

#print df

#df['Gold'].max() - df['Gold.1'].min()
#print largest - smallest
