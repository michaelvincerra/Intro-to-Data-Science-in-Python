import pandas as pd
import numpy as np

census_df = pd.read_csv('census.csv')


# You should also be able to answer this question using idxmax() instead of groupby!!!

def answer_five():
    df5 = census_df.groupby('STNAME').count().sort_values(by='SUMLEV', ascending=False).iloc[0].name

    return df5


print answer_five()



