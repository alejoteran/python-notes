'''
def myPrint(text):
    print(f"Hello {text*2}")


myPrint("daniel")


a = 10
b = 20

def add(a, b):
    return a + b

print(add(a, b))
'''
def find_volume(length = 1, width = 1, height = 1):
    return length * width * height, width, "hola"

result = find_volume(10, 20, 30)
print(result)

result = find_volume()
print(result)

result, width, text = find_volume(width=20)
print(result)
print(width)
print(text)