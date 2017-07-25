import pandas as pd



census_df = pd.read_csv('census.csv')



def answer_eight():
    # NOTE: DataFrame, f8, must be the same in all instances.

    f8 = census_df[(census_df['POPESTIMATE2015'] > census_df['POPESTIMATE2014']) & ((census_df['REGION'] == 1) | (census_df['REGION'] == 2))]
    f8 = f8[f8['CTYNAME'].str.startswith('Washington')]
    return f8.ix[:,['STNAME', 'CTYNAME']]

print answer_eight()


#df['STNAME'] = df.index
#df = df.set_index('STNAME')
#df = df.reset_index()

#df = df[df['SUMLEV'] == 50]


#columns_to_keep = ['STNAME',
#                   'CTYNAME',
#                  'BIRTHS2010',
#                   'BIRTHS2011',
#                   'BIRTHS2012',
#                  'BIRTHS2013',
#                   'BIRTHS2014',
#                   'BIRTHS2015',
#                   'POPESTIMATE2010',
#                   'POPESTIMATE2011',
#                   'POPESTIMATE2012',
#                   'POPESTIMATE2013',
#                   'POPESTIMATE2014',
#                   'POPESTIMATE2015']
#df = df[columns_to_keep]


