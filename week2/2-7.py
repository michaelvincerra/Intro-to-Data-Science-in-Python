import pandas as pd
print
print "How to INDEX DataFrames"
print

print "olympics.csv "
print

df = pd.read_csv('olympics.csv')
print df.head()
print

#print "HOW IT WORKS: df = pd.read_csv('olympics.csv', index_col=0, skiprows=1)"
print
df = pd.read_csv('olympics.csv', index_col=0, skiprows=1)

for col in df.columns:
    if col[:2] == '01':
        df.rename(columns={col: 'Gold' + col[4:]}, inplace=True)
    if col[:2] == '02':
        df.rename(columns={col: 'Silver' + col[4:]}, inplace=True)
    if col[:2] == '03':
        df.rename(columns={col: 'Bronze' + col[4:]}, inplace=True)
    if col[:1] == 'No':
        df.rename(columns={col: '#' + col[1:]}, inplace=True)

#df = pd.read_csv('olympics.csv', index_col=0, skiprows=1)
#print df.head()

print "Index by the number of GOLD medals won at Summer Games."
print
print "See use of df.index to set a NEW index"
print "df['country'] = df.index"
print "df = df.set_index('Gold'"
df['country'] = df.index
df = df.set_index('Gold')
print df.head()


print
print "You can RESET previous INDEX 'Gold', by creating a NEW 0 INDEX column."
print " df =df.reset_index()"
print
df =df.reset_index()
print df.head()

