#Costos de los articulos producidos = enero 1.25, febrero 1.38, Marzo 1.14#
"""Enero = int(input("Digite las cantidades de Enero: "))
Febrero = int(input("Digite las cantidades de Febrero: "))
Marzo = int(input("Digite las cantidades de Marzo: "))


Costo = Enero*1.25+Febrero*1.38+Marzo*1.14
print(Costo)
print(f"Las cantidades de enero, febrero y marzo son {Enero}, {Febrero} y {Marzo} con un costo de ${Costo}")"""

#ejercicio 2#
"""Dias = ["Lunes", "Martes","Miercoles","Jueves","Viernes",]
lu = int(input("Lunes: "))
Dias[0]=lu

ma= int(input("Martes: "))
Dias[1]=ma

mie= int(input("Miercoles: "))
Dias[2]=mie

jue= int(input("Jueves: "))
Dias[3]=jue

Vie= int(input("Viernes: "))
Dias[4]=Vie

print(Dias)"""

#ejercicio 4 Se usa tupla cuando no quieres que cambien los resultados#

"""alumnos = ("Diego", "Fran", "Calvito", "Aby", "Medranito", "Alvin", "Gene")
ninio = int(input("Ingrese el orden del niño que desea saber (1-7): "))
print(f"El alumno que ingreso como numero {ninio} es {alumnos[ninio-1]}")"""

#ejercicio5#
Nombre = input("Cual es tu nombre: ")
Apellido = input("Cual es tu apellido: ")
Respuesta= int(input("¿Quieres propuesta 1 o propuesta 2? "))
if Respuesta == 1 : print(f"{Nombre.lower()}.{Apellido.lower()}""@ISND.com")
elif Respuesta == 2 : print(f"{(Nombre[0].lower())}{Apellido.lower()}""@ISND.com")


#EJERCICIO 6#
"""Salario =input("Cual es tu salario? ")
print(Salario[0]== "$")
print(Salario.count("$")==1)
"""
#Ejercicio 7#

Contraseña = "DFGUPCCBJKAJ"
print(Contraseña [0::3])
