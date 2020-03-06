import pandas as pd;



print("hello");


df=pd.read_csv('olympics.csv', index_col=0, skiprows=1)


# print(df.head);



for index, series in df.iterrows():
	print(index);

