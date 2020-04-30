import pandas as pd
df1=pd.DataFrame({"HPI":[80,90,70,60],"Int_rate":[2,1,2,3],"IND_GDP":[50,45,45,67]},
                 index=[2001,2002,2003,2004])

df2=pd.DataFrame({"gpi":[80,90,70,60],"Int":[2,1,2,3],"GDP":[50,45,45,67]},
                 index=[2001,2003,2004,2008])


print(df1.join(df2)) # all values in df1 and matched index values in df2 if the index is not present in df2 then NaN will be displayed


# output:
#    HPI  Int_rate  IND_GDP   gpi  Int   GDP
# 2001   80         2       50  80.0  2.0  50.0
# 2002   90         1       45   NaN  NaN   NaN
# 2003   70         2       45  90.0  1.0  45.0
# 2004   60         3       67  70.0  2.0  45.0
print()
print("==================================================================================")
print()
print(df2.join(df1)) # all values in df2 and matched index values in df1 if the index is not present in df1 then NaN will be displayed

#
# output:
# gpi  Int  GDP   HPI  Int_rate  IND_GDP
# 2001   80    2   50  80.0       2.0     50.0
# 2003   90    1   45  70.0       2.0     45.0
# 2004   70    2   45  60.0       3.0     67.0
# 2008   60    3   67   NaN       NaN      NaN

