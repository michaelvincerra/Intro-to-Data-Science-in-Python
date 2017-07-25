import pandas as pd
print
print "How to Query DataFrames"
print

print "olympics.csv "
print

df = pd.read_csv('olympics.csv')
#print df.head()
print

#print "HOW IT WORKS: df = pd.read_csv('olympics.csv', index_col=0, skiprows=1)"

df = pd.read_csv('olympics.csv', index_col=0, skiprows=1)
#print df.head()

print
#print df.columns

for col in df.columns:
    if col[:2] == '01':
        df.rename(columns={col: 'Gold' + col[4:]}, inplace=True)
    if col[:2] == '02':
        df.rename(columns={col: 'Silver' + col[4:]}, inplace=True)
    if col[:2] == '03':
        df.rename(columns={col: 'Bronze' + col[4:]}, inplace=True)
    if col[:1] == 'No':
        df.rename(columns={col: '#' + col[1:]}, inplace=True)



print df

# RESTART WITH QUERYING A DATAFRAME
print "df[Gold] > 0 to show countries that won AT LEAST 1 gold medal"
print
print df["Gold"] > 0
print

print
#only_gold = only_gold.dropna()
#print only_gold.head()

only_gold = df[df['Gold']>0]
print only_gold.head()
print
print "The output of TWO BOOLEAN MASKS compared with operators is ANOTHER SINGLE BOOLEAN MASK"
print "len(df[(df['Gold']>0) | df['Gold.1']>0])"
print "PURPOSE: Identify countries who have received AT LEAST 1 GOLD in the summer olympics ('Gold) AND winter olympics (Gold.1)"
print len(df[(df["Gold"]>=1) | df["Gold.1"]>=1])
print
print "Are there any countries that have only won a gold in WINTER olympics and never in SUMMER olympics?"
print "NOTE: Work from center outward; then use '&' to chain df's together: "
print "df[(df['Gold.1']>0) & (df['Gold'] == 0)]"
print
print df[(df['Gold.1']>0) & (df['Gold'] == 0)]
print
print
print
print "QUIZ PRACTICE"
print
print

print "only_gold_summ = df.where(df['Gold']>=1).count()"
print

#gold_compare = df.where(df['Gold']>=1) / only_gold_wint = df.where(df["Gold.1"]>=1)


#print gold_compare




#print df[(df['Gold']>0) & (df['Gold'] == 0)]


