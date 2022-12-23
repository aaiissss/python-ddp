# animals = ["Kucing", "Ayam", "Sapi"]

# # rest / spred Operator

# newAnimal = "Guguk"

# animals = [*animals, newAnimal]

# print (animals)

def getDataAnimals(*animals):
    for animal in animals:
        print (animal)

getDataAnimals("Kucing", "Ayam", "Sapi", "Guguk")