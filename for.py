'''
for element in range(5, 20):
    print(element)

'''

"""
my_list = [19,62,33,42,56,96,70,83,92,120]
for i in my_list:
    print(i)


my_tuple = ("Daniel", "Mariana", "Juan")
for i in my_tuple:
    print(i)


product = {
    'name' : 'camisa',
    'stock' : 100,
    'price' : 20
}

for i in product:
    print(i, " => ", product[i])


for key, value in product.items():
    print("Key = ", key)
    print("Value = ", value , "\n")


"""

people = [
    {
        "name" : "Daniel",
        "age" : 19
    },
    {
        "name" : "Mariana",
        "age" : 20
    },
    {
        "name" : "Alejandro",
        "age" : 21
    }
]

for person in people:
    print("Name => ", person["name"])