rivers = {
    "egypt"     : "nile",
    "china"     : "Yangtze Kiang",
    "mauritius" : "grse",
    "england"   : "danube"
}

for country, river in rivers.items():
    print("The {} runs through {}".format(river, country))

print()

for river in rivers.values():
    print(river)

print()

for country in rivers.keys():
    print(country)