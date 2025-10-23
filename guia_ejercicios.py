#ejercicio 1#
'''numero = int(input())
if numero < 0:
    print('Negativo')
else:
    print('Positivo')'''
    
#ejercicio 2#

numero = int(input())
if (numero + 1) % 2 == 0:
    par_post = numero + 1
else: 
    par_post = numero + 2

if numero % 3 == 0:
    impar_ant = numero - 1
else:
    impar_ant = numero -1

print(par_post)
print(impar_ant)
