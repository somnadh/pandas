import pandas
website={"day":[1,2,3,4,5,6],"visitors":[258,458,785,147,258,126],"downloads":[74,256,785,123,741,369]}
dataframe=pandas.DataFrame(website)
print(dataframe)

dataframe=dataframe.rename(columns={"visitors":"users"})

print("======After changing==========")

print(dataframe)

# Output
#     day  visitors  downloads
# 0    1       258         74
# 1    2       458        256
# 2    3       785        785
# 3    4       147        123
# 4    5       258        741
# 5    6       126        369
# ======After changing==========
# Here i changed visitors into users
#    day  users  downloads
# 0    1    258         74
# 1    2    458        256
# 2    3    785        785
# 3    4    147        123
# 4    5    258        741
# 5    6    126        369
