# Basic statstic operations
from statistics import median,mode,variance,mean

print(median([7,8,2,2])) #4.5
print(mode([12,2,2,2]))  #2
print(variance([12,2,2,2])) #25.0
print(mean([12,2,2])) # 5.333333333333333
print()
print("====================One Way=======================")
print()
import statistics as s
print(s.median([7,8,2,2]))
print(s.mode([12,2,2,2]))
print(s.variance([12,2,2,2]))
print(s.mean([12,2,2]))