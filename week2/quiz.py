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
		
#def answer_zero():
#	for item in df:
#		item = df.iloc[:1]
#	return 	df.iloc[:1] 


# find country whose "Combined total" is greater than 1000 Gold medals 	
#def argument_zero2():
#	for item in df:
#		item = df['Gold.2']>1000
#	return item


	
#def answer_zero1():
#	for item in df: 
#		item = df['Gold']
#print answer_zero1()
#most_gold = df.where(df['Gold']=max())

#argument_zero2()
#df.idxmax()