# you must remove the first column
import pandas as pd

print "US POPULATION at County level."
print
df = pd.read_csv('census.csv')
print df.head()
print
print "Show me the unique values for SUMLEV"
#print df['SUMLEV'].unique()
print
print "Get rid of SUM at the State Level but KEEP COUNTY data."
df = df[df['SUMLEV'] == 50]
print df.head()

columns_to_keep = ['STNAME', 'CTYNAME', 'BIRTHS2010', 'BIRTHS2011', 'BIRTHS2012', 'BIRTHS2013', 'BIRTHS2014', 'BIRTHS2015', 'POPESTIMATE2010',
					'POPESTIMATE2011', 'POPESTIMATE2012', 'POPESTIMATE2013', 'POPESTIMATE2014', 'POPESTIMATE2015']

# EQUIVALENT STATEMENT: Make the new DATAFRAME THIS!!

print
print "Reduce DATASET to population estimates and number of births "
print
df = df[columns_to_keep]
print df.head()

print "Create a DUAL INDEX with State and County Name."
df = df.set_index(['STNAME', 'CTYNAME',])
print df.head()

print "Show population estimates for the state of Michigan."
print
print "MULTI-INDEX requires that two values are used to query:"
print
print "print df.loc['Michigan', 'Washtenaw County']. Remember: 'loc' is used to reference the iloc/index"
print
print df.loc['Michigan', 'Washtenaw County']

print
print "Compare Washetnaw County and Wayne County"
print
print "NOTE: State and County are passed as TUPLES, so ( ) are used INSIDE the DATAFRAME"
print
print "df.loc[ (['Michigan', 'Washtenaw County'], ['Michigan', 'Wayne'] )]"
print df.loc[[('Michigan', 'Washtenaw County'), ('Michigan', 'Wayne County')]]
print

"""
def answer_six():
	census2=census_df.set_index(['STNAME'])
	states=set(census2.index)    
	
	dict1={}   
	
	for i in states:        
		state=census2.loc[i]['CENSUS2010POP'].order(ascending=False)        
	
	try: 
		dict1[int(state.iloc[0]+state.iloc[1]+state.iloc[2])]=i        
	except: 
		dict1[int(state.iloc[0]+state.iloc[1])]=i
		nbcounties=sorted(dict1.keys(),reverse=True)  popstate=[]
s
	for i in nbcounties[0:3]:popstate.append(dict1[i])
	return popstate        
	
	
	
	
# you must remove the first column 	
	def answer_seven():    
		census2=census_df.set_index(['CTYNAME'])    
		census3=census2.loc[:,['POPESTIMATE2010','POPESTIMATE2011','POPESTIMATE2012','POPESTIMATE2013','POPESTIMATE2014','POPESTIMATE2015']]    
		changes=[]    
		
		for index, row in census3.iterrows(): 
		    change=max(row)-min(row)        
		    try:  
		    	if int(change)>int(max(changes)): changestate=index        
		    except: changestate=index        changes.append(change)    
	return changestate
"""
