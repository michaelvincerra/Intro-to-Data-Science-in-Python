# you must remove the first column 
# excluding sumlev=40

import pandas as pd
import numpy as np

census_df = pd.read_csv('census.csv')


def answer_seven():
    df7 = census_df[census_df['SUMLEV'] == 50].set_index(['STNAME','CTYNAME']).ix[:,['POPESTIMATE2010','POPESTIMATE2011','POPESTIMATE2012','POPESTIMATE2013','POPESTIMATE2014','POPESTIMATE2015']].stack()
    df8 = df7.max(level=['STNAME','CTYNAME']) - df7.min(level=['STNAME','CTYNAME'])
    return df8.idxmax()[1]

print answer_seven()


#df = df[df['SUMLEV'] == 50]
#	def answer_seven():
#		census2=census_df.set_index(['CTYNAME'])
#		census3=census2.loc[:,['POPESTIMATE2010','POPESTIMATE2011','POPESTIMATE2012','POPESTIMATE2013','POPESTIMATE2014','POPESTIMATE2015']]
#		changes=[]
#
#		for index, row in census3.iterrows():
#		    change=max(row)-min(row)
#		    	if int(change)>int(max(changes)): changestate=index
#		    except: changestate=index        changes.append(change)
#	return changestate