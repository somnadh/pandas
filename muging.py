import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

country=pd.read_csv('E:\\programms\\python programms\\Pandas\\factbook.csv',index_col=0) # which is used to read the csv files
country.to_html("edu.html") #covert csv file to html
df=country.head(5)
df=df.set_index(["Country"])
sd=df.reindex(columns=['Units Sold','Unit Price'])
db=sd.diff(axis=1)
df.plot(kind='bar') # it plots bar chart for top 5 rows
plt.show() # for displaying charts