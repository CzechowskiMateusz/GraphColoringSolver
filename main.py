import json
import random 
import time 
import string 
import os

from codes.write_graphs import *
from codes.greedy_algorithm import *
from codes.random_algorithm import *
from codes.full_algorithm import *
from codes.metaheuristic import *

# JSON files - First one for reading data, rest for saving
file_open = './test_data/data_v15.json'
res_greedy = './result_data/data_v15_greedy.json'
res_ran = './result_data/data_v15_random.json'
res_genetic = './result_data/data_v15_genetic.json'
#res_full = './result_data/data_v8_full.json'

file = open(file_open)
data = json.load(file)

#==========================
#=         Greedy         =
#==========================

print("Greedy Solution")
save = {}
start = time.time()
Greedy(data["Matrix"], data['V'], save)
clrs = save["ChromaticNum"]
end = time.time()
print("Solution: ", save)
print("Time: ", end-start)

with open(res_greedy, "w") as outfile:
    json.dump(save, outfile)

#==========================
#=         Random         =
#==========================

print("Random Greedy Solution")
save = {}
start = time.time()
Random(data["Matrix"], data['V'], save)
end = time.time()
print("Solution: ", save)
print("Time: ", end-start)

with open(res_ran, "w") as outfile:
    json.dump(save, outfile)

#==========================
#=         Fuller         =
#==========================
print("Brute Force Solution - Full Showcase")
save = {}
start = time.time()
#Full(data["Matrix"], data['V']*2, save)
end = time.time()
print("Solution: ", save)
print("Time: ", end-start)

#with open(res_full, "w") as outfile:
#    json.dump(save, outfile)

#==========================
#=        Genetic         =
#==========================
print("Metaheurisitc - Genetic Solution")
save = {}

# Metaheuristic data:
population = 2
generations = 100
mutation = 0.1

start = time.time()
Genetic(data["Matrix"], data["V"], clrs, population, generations, mutation, save)
end = time.time()
print("Solution: ", save)
print("Time: ", end-start)

with open(res_genetic, "w") as outfile:
    json.dump(save, outfile)


GraphMaker(data["Matrix"])