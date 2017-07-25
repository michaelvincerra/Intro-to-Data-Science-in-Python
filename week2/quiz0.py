#coding: utf-8
import pandas as pd

df = pd.read_csv('olympics.csv', index_col=0, skiprows=1)

for col in df.columns:
    if col[:2]=='01':
        df.rename(columns={col:'Gold' + col[4:]}, inplace=True)
    if col[:2]=='02':
        df.rename(columns={col:'Silver' + col[4:]}, inplace=True)
    if col[:2]=='03':
        df.rename(columns={col:'Bronze' + col[4:]}, inplace=True)
    if col[:1]=='№':
        df.rename(columns={col:'#' + col[1:]}, inplace=True)

names_ids = df.index.str.split('\s\(') # split the index by '('

df.index = names_ids.str[0] # the [0] element is the country name (new index)
df['ID'] = names_ids.str[1].str[:3] # the [1] element is the abbreviation or ID (take first 3 characters from that)

df = df.drop('Totals')

df.head()

largest = 0
smallest = 0


def answer_two():

    for number in df[df['Gold']>0]:
        if largest == 0 or number > largest:
            largest = largest + 1
            # df['Gold'].max()

    for number in df[df['Gold.1']>0]:
        if smallest == 0 or number < smallest:
            smallest = number
            #df['Gold.1'].min()

    return largest - smallest

    #return df.where(df['Gold'].max()- df['Gold.1'].min())











# which country won the most gold medals? 
#Which country has won the most gold medals in summer games?
#print df['Gold'].max()


#print df.where(df['Gold'] > 0) - df.where(df['Gold.1'] > 0).max()

#print df['Gold'] + df['Gold.1'].max()
#print
#What is the first country in df?
#print df.iloc[0:1]

#what country won the most gold medals in the summer games?

# print df['Gold']>0

#only_gold = df.where(df['Gold'] > 0)
#print only_gold.head()
#print only_gold['Gold'].count()

#print len(df[(df['Gold']>0) | df['Gold.1']>0])
#only_gold = df.where(df['Gold'])].idxmax()

# Which country won a Gold medal in the Winter (Gold.1) but never won a Gold in the Summer(Gold)?
# note the use of casting a positive equation to determine a '0' result.
#print df[(df['Gold.1']>0) & (df['Gold'] ==0)]

#Which country won the most gold medals?
#print df.loc(df['Gold'].max() + df['Gold.1'].max())

#d = abs(df.iloc[i]['Gold'] - df.iloc[i]['Gold.1'])

#df.iloc[0]



#CONSIDER WHAT CHRIS SAID: YOU'LL NEED TO ITERATE OVER THE LARGEST ITEM IN THE FOR LOOP UNTIL
#IT FINDS THE LARGEST NUMBER, WHICH WILL END THE FOR LOOP: THAT WILL FIND THE HIGHEST VALUE

#x = 0
#y = 1



#largest = 0

#for itervar in ['Gold']:
 #   if largest.int(0) is 0 or itervar > largest:
  #      largest = largest +1

#print largest()




#for items in x():
#   largest_so_far =
#   largest_so_far_index()
#   smallest_so_far =


#df['Gold'] + df['Gold.1'])=max()

#df.loc['United States (USA) [P] [Q] [R] [Z]', 'Combined total']
#next try to use the .iloc and .loc function with splices and arrays.
#BTW: You're on the right track. Don't worry about how fast you learn.

# biggest1_diff = df[df['Gold'].max()]
# biggest2_diff = df[df['Gold.1'].max()]
# biggest_diff = df['Gold.1'].max()
# biggest_diff = df['Gold'] - df['Gold.1']
# result_diff = biggest_diff.set_index['Gold']
# result_diff = biggest_diff.sort_index(ascending = 0)
# return biggest_diff.iloc[0]['ID']