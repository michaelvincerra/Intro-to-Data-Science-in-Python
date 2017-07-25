import pandas as pd

products_df = pd.DataFrame([{'Product_ID':'4109', 'Price':'5.0','Product':'Sushi Roll'},
                            {'Product_ID':'1412', 'Price': '0.5','Product':'Egg'},
                            {'Product_ID':'8931', 'Price':'1.5','Product':'Bagel'}])

products_df = products_df.set_index('Product_ID')

invoices_df = pd.DataFrame([{'Customer':'Ali','Product_ID':'4109','Quantity':1},
                        {'Customer':'Eric', 'Product_ID':'1412','Quantity':12},
                        {'Customer':'Ande', 'Product_ID':'8931','Quantity':6},
                        {'Customer':'Same', 'Product_ID':'4109','Quantity': 2}])

invoices_df=invoices_df.set_index()

#answer = pd.merge(products_df, invoices_df, how='left', left_on ='Product_ID', right_on = 'Product_ID')
     #pd.merge(staff_df, student_df, how='left', left_on='Name', right_on='Name')
#print answer

# RESTART PROBLEM SOLVING: SEE 2 SET_INDEX COMMANDS ABOVE

print (pd.merge(products_df, invoices_df, left_index=True, right_on='Product_ID'))
