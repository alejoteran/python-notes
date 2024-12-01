import random

countries = ["Estonia", "Finland", "Sweden", "Denmark", "Norway", "Iceland"]
populations = {}

populations = {country: random.randint(1, 100) for country in countries}
print(populations)

big_countries = {country : population for (country, population) in populations.items() if population > 10}
print(big_countries)


text = "In 1984 there"
vocals = { c : c.upper() for c in text if c in "aeiouAEIOU"}
print(vocals)   

vocals_v2 = { i : text[i] for i in range(len(text)) if text[i].isalpha() }
print(vocals_v2)

frequencies = {c : text.count(c) for c in text if c in "aeiouAEIOU"}
print(frequencies)