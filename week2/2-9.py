import pandas as pd

df = pd.read_csv('log.csv')

# DUAL index, time, user, must be entailed in [] brackets!!
df = df.set_index(['time', 'user'])
df = df.sort_index()


print df

