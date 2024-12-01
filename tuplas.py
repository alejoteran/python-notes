numbers = (1, 2, 3, 4, 5)
strings = ("Daniel", "Juan", "Mariana", "Daniel")

print(numbers)
print("0 => ", numbers[0])
print("-1 => ", numbers[-1])
print(strings)


print(strings.index("Juan"))
print(strings.count("Daniel"))


my_list = list(strings)
print(my_list)
print(type(my_list))

my_list[1] = "Carlos"
print(my_list)

my_tuple = tuple(my_list)
print(my_tuple)