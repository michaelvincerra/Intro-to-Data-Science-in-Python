
#names_ids = df.index.str.split('\s\(') # split the index by '('

#df.index = names_ids.str[0] # the [0] element is the country name (new index)
#df['ID'] = names_ids.str[1].str[:3] # the [1] element is the abbreviation or ID (take first 3 characters from that)

#df = df.drop('Totals')




#03.26.17 - previous answer

#def answer_one():
#    only_gold = df[df['Gold']>0]
#    only_gold = only_gold.set_index('Gold')
#    only_gold = only_gold.sort_index(ascending = 0)
#    return only_gold.iloc[0]['ID']
#answer_one()




#def answer_zero():
#	most_gold = df.where(df['Gold'])>0
#	return df.loc['Summer']

#print answer_zero

#print answer_zero()


#def answer_zero():
#	most_gold = df.where(df['Gold']>0)
#	return df.loc['Gold']


#print answer_zero, df.head()


#only_gold = df.where(df['Gold'] >0)

#most_gold = df.where(df['Gold']>0)

#print most_gold