def cities(country, *cities):
    print(country, cities)
    print("Type is ", type(cities))

cities("France")
cities("France", "Paris")
cities("France", "Paris", "Toulouse", "Bordeaux", "Lyon")
