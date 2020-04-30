# merging is applicable for common data
import pandas
website1=pandas.DataFrame({"day":[1,2,3,4,5,6],"visitors":[258,458,785,147,258,126],"downloads":[74,256,785,123,741,369]},index =[2001,2002,2003,2004,2005,2006])
# print(website1)
website2=pandas.DataFrame({"day":[1,2,3,7,9,10],"visitors":[258,458,785,188,248,158],"downloads":[74,256,785,123,741,369]},index =[2007,2008,2009,2010,2011,2012])
# print(website2)
d=pandas.merge(website2,website1,on="day") # here we get day as common remaing all colums displays for both tables
print(d)

# output:
# day  visitors_x  downloads_x  visitors_y  downloads_y
# 0    1         258           74         258           74
# 1    2         458          256         458          256
# 2    3         785          785         785          785
# ==============================================================================
import pandas as pd
df1=pd.DataFrame({"HPI":[80,90,70,60],"Int_rate":[2,1,2,3],"IND_GDP":[50,45,458,67]},
                 index=[2001,2002,2003,2004])

df2=pd.DataFrame({"HPI":[80,90,70,60],"Int_rate":[2,1,2,3],"IND_GDP":[50,45,45,671]},
                 index=[2005,2006,2007,2008])

mer=pd.merge(df1,df2) #  it gives only common values of both tables

print(mer)

# output:
#    HPI  Int_rate  IND_GDP
# 0   80         2       50
# 1   90         1       45