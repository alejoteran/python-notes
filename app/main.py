import mod

countries, population = mod.get_population()

for i in range(0, len(countries)):
    print(countries[i], population[i])