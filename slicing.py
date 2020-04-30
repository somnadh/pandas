import pandas
website={"day":[1,2,3,4,5,6],"visitors":[258,458,785,147,258,126],"downloads":[74,256,785,123,741,369]}
dataframe=pandas.DataFrame(website)#to convet dictionary into a dataframe
print(dataframe)



print("=========================SLICING=============================")

print("first two lines")
print(dataframe.head(2))

print("Last 2 lines")
print(dataframe.tail(2))

print("==========================End===============================")


# output:
#
#     day  visitors  downloads
# 0    1       258         74
# 1    2       458        256
# 2    3       785        785
# 3    4       147        123
# 4    5       258        741
# 5    6       126        369
# =========================SLICING=============================
# first two lines
#     day  visitors  downloads
# 0    1       258         74
# 1    2       458        256
# Last 2 lines
#    day  visitors  downloads
# 4    5       258        741
# 5    6       126        369
# ==========================End===============================
