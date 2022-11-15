from Module import * 
import pandas as pnd
import numpy as np

#WriteDataToFile()
#ReadDataFromFile()
#ShowData()


features=[3,19,10,15,14,12,9,8,11,12,11,12,13,11,14,16]

features_sorted =[3,8,9,10,11,11,11,12,12,12,13,14,14,15,16,19]

serie_pair=[11,12,13,14,15,16,17,18]       #=>for a test

serie_impaire=[11,12,13,14,15,16,17]  #for a test


array1 = np.array([1,2,3])
array2 = np.array([2,4,5])
# #after sort features[8]
# print(features_sorted[8])



# median=calculMediane(features)
# print("la mediane est...... : "+ str(median))
# print("\n\n")

GenerateData(10,30,10)
print("\n")
print("\n")
#cor=correlation(x,y)
#print(cor)
print("\n")
print("\n")
x = [1.23, 2.12, 3.34, 4.5]
 
y = [2.56, 2.89, 3.76, 3.95]
co=covariance(x,y)
print(co)
print("\n")
print("\n====ADDDDDDDDD")



