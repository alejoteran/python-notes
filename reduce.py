import functools

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = functools.reduce(lambda counter, item: counter + item, numbers)

print(result)


mayor = functools.reduce(lambda counter, item: item if item > counter else counter, numbers)
print(mayor)