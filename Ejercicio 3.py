p = {"Pan": 1.40, "Huevos": 2.30, "Cebolla": 0.85, "Aceite": 4.35}
n = input("Dime un producto:")
c = float(input("Dime la cantidad:"))
if n.title() in p:
    print("El artículo cuesta:", p[n.title()] * c, "€")
else:
    print("El artículo no esta en stock")
input()