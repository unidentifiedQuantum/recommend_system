import pandas as pd
import numpy as np 

df = pd.read_csv('recommend_datas.csv')

got = ''
print(df.to_string(index=False))
done = False

while not done:
	name = 'Apple' #input('Search something from the table: ').title()
	if name not in df.values:
		print('Please select items from the table')
	else:
		for column in df:
			if df[column].str.contains(name).sum() > 0:
				got = column
				
				

		print()

		print("Relevant searches:- \n", df[got].to_string(index=False))
		done = True



