# Agenda of this programme is convert the below dictionary to data frame

import pandas
website={"day":[1,2,3,4,5,6],"visitors":[258,458,785,147,258,126],"downloads":[74,256,785,123,741,369]}
dataframe=pandas.DataFrame(website)
print(dataframe)
# Output:
#
#    day  visitors  downloads
# 0    1       258         74
# 1    2       458        256
# 2    3       785        785
# 3    4       147        123
# 4    5       258        741
# 5    6       126        369
#
# if we are not provide index it take default value as index also we can set our one of the column for that refere below example

dataframe.set_index("day",inplace=True)  #to set index as one column if u want to print
print(dataframe)

# output:
#  here i set day as index have a look following Output
#
#  visitors  downloads
# day
# 1         258         74
# 2         458        256
# 3         785        785
# 4         147        123
# 5         258        741
# 6         126        369
