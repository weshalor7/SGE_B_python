from cotxe import Cotxe
from colibri import Colibri

cotxe1 = Cotxe("Toyota", "Corolla", 2020, "Blau", 20000)
cotxe2 = Cotxe("Ford", "Focus", 2018, "Negre", 18000)
cotxe3 = Cotxe("BMW", "Serie 3", 2022, "Blanc", 35000)

colibri1 = Colibri("Rubí", "Petita", 3, 50, "Vermell")
colibri2 = Colibri("Anna", "Mitjana", 2, 45, "Verd")
colibri3 = Colibri("Albina", "Gran", 5, 40, "Groga")

print("Cotxe 1 - Marca:", cotxe1.get_marca())
print("Cotxe 2 - Model:", cotxe2.get_model())
print("Cotxe 3 - Any:", cotxe3.get_any())

print("Colibrí 1 - Espècie:", colibri1.get_espècie())
print("Colibrí 2 - Mida:", colibri2.get_mida())
print("Colibrí 3 - Edat:", colibri3.get_edat())
print("Colibrí 1 - Velocitat:", colibri1.get_velocitat())

cotxe1.set_color("Vermell")
cotxe2.set_preu(17000)

print("Cotxe 1 - Color modificat:", cotxe1.get_color())
print("Cotxe 2 - Preu modificat:", cotxe2.get_preu())

colibri1.set_color("Blau")
colibri2.set_velocitat(55)

print("Colibrí 1 - Color modificat:", colibri1.get_color())
print("Colibrí 2 - Velocitat modificada:", colibri2.get_velocitat())
