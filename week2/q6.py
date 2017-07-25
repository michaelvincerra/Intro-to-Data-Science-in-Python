# you must remove the first column 
# excluding sumlev=40
import pandas as pd
import numpy as np

census_df = pd.read_csv('census.csv')


#df = df[df['SUMLEV'] == 50]

#def answer_six():
#	census2=census_df.set_index(['STNAME'])
# 	states=set(census2.index)
#	dict1={}
#	for i in states:
#		state=census2.loc[i]['CENSUS2010POP'].order(ascending=False)
#	try:
#		dict1[int(state.iloc[0]+state.iloc[1]+state.iloc[2])]=i
#	except:
#		dict1[int(state.iloc[0]+state.iloc[1])]=i
#		nbcounties=sorted(dict1.keys(),reverse=True)
#
#		popstate=[]
#		for i in nbcounties[0:3]:popstate.append(dict1[i])
#		return popstate


def answer_six():
    d6 = census_df[census_df['SUMLEV'] == 50].groupby('STNAME')['CENSUS2010POP'].apply(lambda x: x.nlargest(3).sum()).nlargest(3).index.values.tolist()
    return d6

print answer_six()

