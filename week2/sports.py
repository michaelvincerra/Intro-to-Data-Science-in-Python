import pandas as pd

sports1 = pd.Series({'Archery': 'Bhutan',
          'Golf': 'Scotland',
          'Sumo': 'Japan',
          'Taekwondo': 'South Korea'})          


s = pd.Series(sports1)


#EX1


print 
print s.loc[:] 
print "[:] prints the whole table."
print
print "s.iloc[] searches by INDEX ROW (0, 1, 2) to find corresponding ITEM." 
print
print s.iloc[0]
print s.iloc[1]
print s.iloc[2]
print s.iloc[3]
print
print "s.loc[] searches by LABEL COL ('Name') to find corresponding ITEM." 
print
print s.loc['Archery']
print s.loc['Golf']
print s.loc['Sumo']
print s.loc['Taekwondo']




 
