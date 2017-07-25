# coding: utf-8
import pandas as pd
#/usr/bin/python
#-*- coding: latin-1 -*-
#import os, sys

#import sys  
#reload(sys) 



# class got file from https://en.wikipedia.org/wiki/All-time_Olympic_Games_medal_table
# and it's renamed it as 'olympics.csv'

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


# INTRO_DS_CLASS
#    names_ids = df.index.str.split('\s\(')  # split the index by '('
#    df.index = names_ids.str[0]  # the [0] element is the country name (new index)
#    df['ID'] = names_ids.str[1].str[:3]  # the [1] element is the abbreviation or ID (take first 3 characters from that)
#    df = df.drop('Totals')
# INTRO_DS_CLASS

#def answer_zero():
#	most_gold = df.where(df['Gold'])>0
#	return df.loc['Summer']
#print answer_zero, df.head()

#print answer_zero()


#def answer_zero():
#	most_gold = df.where(df['Gold']>0) 
#	return df.loc['Gold']


#print answer_zero, df.head()


#only_gold = df.where(df['Gold'] >0)
		
def answer_zero():
	for item in df:
		item = df.iloc[:1]
	return 	df.iloc[:1] 

print answer_zero()




#most_gold = df.where(df['Gold']=max())

#print most_gold()