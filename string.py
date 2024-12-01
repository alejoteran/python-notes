name = "Daniel"
last_name = "Teran"
full_name = name + " " + last_name

print("primer nombre ", name)
print("Primer apellido ", last_name)
print("Nombre completo ", full_name)


# Quotes

quote = "I'm Daniel"
print(quote)

quote2 = 'she said "Hello" '
print(quote2)


# Formats

template = "My nombre es " + name + " y mi apellido es " + last_name
print("Version 1: ", template)

template = "Hola mi nombre es {} y mi apellido es {}".format(name, last_name)
print("Version 2: ", template)

template = f"Hola, mi nombre es {name} y mi apellido {last_name}"
print("Version 3: ", template)


edad = input("Ingrese su edad\n")
template = f"Hola, mi nombre es {name} {last_name} y tengo {edad} años"
print("Version 4: ", template)