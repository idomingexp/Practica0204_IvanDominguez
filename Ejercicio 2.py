n = input("Dime tu nombre:")
e = input("Dime tu edad:")
d = input("Dime tu dirección:")
t = input("Dime tu teléfono:")
datos = {"nombre": n, "edad": e, "dirección": d, "teléfono": t}
print(datos["nombre"], "tienes", datos["edad"], "años, vives en", datos["dirección"], "y tu tlfno es", datos["teléfono"])
input()