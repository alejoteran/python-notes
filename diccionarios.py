my_dict = {
    "name" : "Daniel",
    "last_name" : "Teran",
    "age" : 19 
}
print(my_dict)

print(len(my_dict))

print(my_dict["name"])
print(my_dict.get("last_name"))
print(my_dict.get("age"))
print(my_dict.get("valor"))

print("name" in my_dict)
print("valor" in my_dict)

person = {
    "nombre" : "Daniel",
    "apellido" : "Teran",
    "lenguajes" : ["C++", "Java", "Python"],
    "edad" : 20
}

print(person)

person["nombre"] = "Alejandro"
person["edad"] += 10
person["lenguajes"].append("C")
person["lenguajes"].append("JavaScript")
person["lenguajes"][0].lower()
person["apellido"] = person["apellido"].lower()

print(person)

del person["apellido"]
person.pop("nombre")

print(person)

print("items")
print(person.items())

print("keys")
print(person.keys())

print("values")
print(person.values())

person["red"] = "linked"
print(person)