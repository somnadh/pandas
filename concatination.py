import pandas as pd
df1=pd.DataFrame({"HPI":[80,90,70,60],"Int_rate":[2,1,2,3],"IND_GDP":[50,45,45,67]},
                 index=[2001,2002,2003,2004])

df2=pd.DataFrame({"HPI":[80,90,70,60],"Int_rate":[2,1,2,3],"IND_GDP":[50,45,45,67]},
                 index=[2005,2006,2007,2008])

print(pd.concat([df1,df2]))  #concatination of two frames


# output:
#
#       HPI  Int_rate  IND_GDP
# 2001   80         2       50
# 2002   90         1       45
# 2003   70         2       45
# 2004   60         3       67
# 2005   80         2       50
# 2006   90         1       45
# 2007   70         2       45
# 2008   60         3       67

print(pd.concat([df1,df1]))

# Output:
#
# concatinate two frames bliendly  even if the index is same
#        HPI  Int_rate  IND_GDP
# 2001   80         2       50
# 2002   90         1       45
# 2003   70         2       45
# 2004   60         3       67
# 2001   80         2       50
# 2002   90         1       45
# 2003   70         2       45
# 2004   60         3       67


