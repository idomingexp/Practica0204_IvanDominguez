a = {}
b = ""
while b != "6":
    if b == "1":
        NIF = input("Dime el NIF del alumno:")
        n = input("Dime el nombre del alumno:")
        ap = input("dime los apellidos del alumno:")
        c = input("Dime el correo del alumno:")
        t = input("Dime el tlfno del alumno:")
        r = input("Dime si esta aprobado o no (T/F):")
        alumno = {"nombre": n, "apellidos": ap, "correo": c, "telefono": t, "aprobado": r}
        a[NIF] = alumno
    if b == "2":
        NIF = input("Dime el NIF del alumno:")
        if NIF in a:
            del a[NIF]
    if b == "3":
        NIF = input("Dime el NIF del alumno:")
        if NIF in a:
            print('NIF:', NIF)
            for x, y in a[NIF].items():
                print(x.title() + ':', y)
        else:
            print("No hay alumnos con ese NIF tio")
    if b =="4": 
        for x, y in a.items():
            print(x, y["nombre"])
    if b == "5":
        print("Alumnos aprobados:")
        for x, y in a.items():
            if y["aprobado"]:
                print(x, y["nombre"])
    b = input("1 para añadir alumno, 2 para eliminar, 3 para ver datos, 4 para ver NIF y nombre, 5 para ver aprobados y 6 salir:")
input()