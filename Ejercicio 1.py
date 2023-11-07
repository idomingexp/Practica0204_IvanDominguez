m = {"Euro":"€", "Dólar":"$", "Yen":"¥"}
n = input("Dime el nombre de una divisa:")
if n.title() in m:
    print (m.get(n))
else:
    print("La divisa no está guardada")
input()