import json
import random 
import time 
import string 

data = {}
p = 0.5
file = "test_data/data_v30.json"
v = 30

Matrix = [[0 for _ in range(v)] for _ in range(v)]

for i in range(1,v):
    for j in range(i):
	    if (random.random()<=p and i!=j): 
		    Matrix[i][j]=Matrix[j][i]=1

data["V"] = v    
data["Matrix"] = Matrix 

with open(file, "w") as outfile:
    json.dump(data, outfile)


    


