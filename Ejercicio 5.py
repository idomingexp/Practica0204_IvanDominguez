d = {}
n = input("introduce palabra:traducción separándolos por comas:")
for x in n.split(","):
    if x != "terminar":
        a, b = x.split(":")
        d[a] = b
f = input("Introduce una frase en castellano:")
for x in f.split(" "):
    if x in d:
        print(d[x], end=" ")
    else:
        print(x, end=" ")
input()
