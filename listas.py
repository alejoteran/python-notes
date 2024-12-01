numbers = [1, 2, 3 , 4, 5, 6, 7, 8, 9, 10]
print(numbers)
print(type(numbers))

print(numbers[:5])
print(numbers[5:])
print(numbers[::2])

print(numbers)
numbers.append(11)
print(numbers)

numbers.insert(0, "hola")
print(numbers)

task = ["Todo 1", "Todo 2", "Todo 3"]
print(task)

newList = numbers + task
print(newList)

print(newList.index("Todo 2"))

newList.remove("Todo 1")
print(newList)

newList.pop()
print(newList)

newList.pop(0)
print(newList)

newList.reverse()
print(newList)

numeros = [2, 8, 3, 6, 2, 9]
numeros.sort()
print(numeros)

strings = ["Do", "Re", "Mi", "Fa", "Sol", "La", "Si"]
strings.sort()
print(strings)