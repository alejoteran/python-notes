'''
dict = {}

for i in range(1,5):
    dict[i] = i * 2
print(dict)


dict_v2 = {i: i * 2 for i in range(1,5)}
print(dict_v2)

dict_v3 = {str(i): i for i in range(1,5) if i % 2 == 0}
print(dict_v3)


import random

countries = ["Estonia", "Finland", "Sweden", "Denmark", "Norway", "Iceland"]
populations = {}

populations = {country: random.randint(1, 100) for country in countries}
print(populations)

'''

names = ["jhon", "daniel", "sarah", "michael", "jane"]
ages = [10, 20, 30, 40, 50]

#print(list(zip(names, ages)))

dict = {name : age for (name, age) in zip(names, ages)}
print(dict)