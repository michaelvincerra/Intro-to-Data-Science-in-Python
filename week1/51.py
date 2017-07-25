sales_record = {
'price' : 3.24, 
'num_items': 4, 
'person': 'Chris'}

sales_statement = '{} bought {} items at a price of {} each for a total of {}'

print(sales_statement.format(sales_record['person'],
							sales_record['num_items'],
							sales_record['price'],
							sales_record['num_items']*sales_record['price']))
							