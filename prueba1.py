string = "abcdef"
m = 2
n = 1

turno = 1

stringAux = string[m:]
print(string[-1])
print(stringAux)
string2 = stringAux + string[:m]
print(string2)