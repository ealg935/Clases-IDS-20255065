#ejercicio 1#
'''numero = int(input())
if numero < 0:
    print('Negativo')
else:
    print('Positivo')'''
    
#ejercicio 2#

'''numero = int(input())
if (numero + 1) % 2 == 0:
    print(numero + 1)
else:
    print(numero + 2)

numero_impar = numero-1
if (numero_impar) % 2 != 0:
    print(numero_impar)
else:
    print(numero_impar - 1)
'''

#ejercicio 3#

'''c1 = float(input())
c2 = float(input())
c3 = float(input())
c4 = float(input())
c5 = float(input())
c6 = float(input())

promedio = (c1 + c2 + c3 + c4 + c5 + c6) / 6

if promedio > 9.5:
    print("Gana Premio :)")
else:
    print("No Gana Premio :(")'''
    

#ejercicio 4#

'''N = int(input())
cont7 = 0
cont5 = 0
for i in range(N):
    num = int(input())
    if num == 7:
        cont7 += 1
    elif num == 5:
        cont5 += 1
print(cont7, cont5)
'''
#ejercicio 5#

import sys

datos = sys.stdin.read().split()

ncombos = int(datos[0])
Pa = int(datos[1])
Pb = int(datos[2])
Pc = int(datos[3])

indice = 4
for i in range(ncombos):
    combo = datos[indice + i]
    contA = combo.count('A')
    contB = combo.count('B')
    contC = combo.count('C')

    daño_total = (contA * Pa) + (contB * Pb) + (contC * Pc)
    print(daño_total)

entrada = input().split()
ncombos = int(entrada[0])
Pa = int(entrada[1])
Pb = int(entrada[2])
Pc = int(entrada[3])

for i in range(ncombos):
    combo = input().strip()
    contA = combo.count('A') 
    contB = combo.count('B') 
    contC = combo.count('C') 

    daño_total = (contA * Pa) + (contB * Pb) + (contC * Pc)
    print(daño_total)


#ejercicio 6#
N = int(input())
for i in range(N):
    nombres = input().strip().split()
    for i in nombres:
        if len(i)<= 6:
            print('No vale la pena')
        elif len(i) >= 8:
            print('Si aguanto otro desarrollo de personaje')
        elif len(i) > 6 and len(i) < 8:
            print('Dios no creo aguantar esta vez')


#ejercicio 7#
x, y = map(int, input().split())
if x > y:
    print(x)
else: 
    print(y)

#ejercicio 8#
A = int(input())
edades = []

for i in range(A):
    edades.append(int(input()))

cont = 0
for edad in edades:
    if edad >= 15:
        cont += 1

print(cont)

#ejercicio 9#
entrada = input().strip()

if entrada == 'conectado':
    print('Ola Ivan')
else:
    print('Ol..')

#ejercicio 10#
N = int(input())
for _ in range(N):
    num = int(input())
    if num >= 3:
        print('Ok')
    else:
        print('No')