import pandas as pd

sports = pd.Series({'Archery': 'Bhutan',
          'Golf': 'Scotland',
          'Sumo': 'Japan',
          'Taekwondo': 'South Korea'})
          
music = pd.Series({'Jazz': 'USA',
          'Classical': 'Germany',
          'Opera': 'Italy',
          'Raj': 'India'})
          
          
print



df  = pd.DataFrame(['sports', 'music',], index=['Activity1', 'Activity2']) 
print df.head()


# It's not clear to me how the 'DROP' function works below. 
# df.drop('music')