import numpy as np
import pandas as pd



df = pd.DataFrame({ "A": ['1','4','7'],
                    "B": ['2','5','8'],
                    "C": ['3','6','9']})

                           # NOTE: Inside DataFrame, you may alternatively specify: columns =['A', 'B', 'C'])

    #return df

print df
print
print "OBSERVE: idxmax() returns the INDEX POSITION of the highest value (NOT the value)."
print "Prefer use of idxmax() over argmax()"
print
print df['A'].idxmax()
print df['B'].argmax()
print df['C'].idxmax()
print
print "You may set index--df=df.set_index('C')--before idxmax(), if you need to sort by a new index."
print 'df=df.set_index(C)-- sets "C" as the new index.'
df1 = df.set_index('C')
print
print df1
print
print "Or, you may want to reset index ( df=df.reset_index()), before idxmax(), to sort by a new index."
print "Why? Because the idxmax() value that you seek is relative to an index 'label' in first column that you seek."
df=df.reset_index(drop=True)
#df=df.reset_index(drop=True)
# use above to drop the repeated index
print df
