# here you can view the data as well as graph
import pandas
import matplotlib.pyplot as plt
from matplotlib import style
style.use("fivethirtyeight")
website={"day":[1,2,3,4,5,6],"visitors":[258,458,785,147,258,126],"downloads":[74,256,785,123,741,369]}
dataframe=pandas.DataFrame(website)
print(dataframe)
dataframe.set_index("day",inplace=True)  #to set index as one column if u want to print
print(dataframe)

n=input("give below inputs for Graph \n 1.for Line chart \n 2. for bar chart \n Any key to exit")
if n=='1':

    dataframe.plot(kind="line")
    plt.show()
elif n=='2':
    dataframe.plot(kind="bar")
    plt.show()
else:
    exit()
#
# Output:
#    day  visitors  downloads
# 0    1       258         74
# 1    2       458        256
# 2    3       785        785
# 3    4       147        123
# 4    5       258        741
# 5    6       126        369
#      visitors  downloads
# day
# 1         258         74
# 2         458        256
# 3         785        785
# 4         147        123
# 5         258        741
# 6         126        369
# give below inputs for Graph
#  1.for Line chart
#  2. for bar chart
#  Any key to exit x # here i gave x as input so it just terminated u can give options if u want a graph
#
# Process finished with exit code 0

