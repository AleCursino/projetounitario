from src.models.ice_cream_stand import IceCreamStand
from src.models.restaurant import Restaurant

#restaurante = Restaurant("Dagente", "Comida Nordestina")

sabores = ["Chocolate", "Creme", "Doce de leite", "Leite ninho"]
sorveteria1 = IceCreamStand("Felizvete", "Sorvetes artesanais", sabores)
#sorv2 = IceCreamStand("Felizvete", "Sorvetes artesanais", [])

print(sorveteria1.flavors_available())

print(sorveteria1.add_flavor("Maracujá"))
print(sorveteria1.flavors_available())

#sorv2.flavors_available()

"""
sorveteria1.find_flavor("Creme")
sorv2.flavors_available()
sorveteria1.find_flavor("Manga")

sorv2.find_flavor("Maracujá")


sorveteria1.add_flavor("Banana")
sorv2.add_flavor("Uva")

sorv2.flavors_available()
"""


"""
resultado = restaurante.describe_restaurant()

#print(resultado)


print(restaurante.open)
print(restaurante.open_restaurant())
print(restaurante.open)
print(restaurante.open_restaurant())
print(restaurante.open)

print(restaurante.close_restaurant())
print(restaurante.open)
print(restaurante.close_restaurant())

print(restaurante.open_restaurant())

print(restaurante.set_number_served(25))

print(restaurante.describe_restaurant())

print(restaurante.number_served)

#print(restaurante.close_restaurant())

print(restaurante.increment_number_served(25))

print(restaurante.describe_restaurant())

print(restaurante.number_served)

print(restaurante.valid_num_costumers(0))
"""


