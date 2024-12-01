set_countries = {"col", "mex", "bol"}

size = len(set_countries)
print(size)

print("col" in set_countries)
print("per" in set_countries)


#add

set_countries.add("peru")
print(set_countries)
set_countries.add("peru")
print(set_countries)


#update

set_countries.update({"ar", "eq", "peru"})
print(set_countries)


#remove

set_countries.remove("col")
print(set_countries)
set_countries.remove("ar")
print(set_countries)

#con discard no explota si no lo encuentra
set_countries.discard("arg")
print(set_countries)

set_countries.clear()
print(set_countries)