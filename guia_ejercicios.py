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

if len(str(numero)[-1]) == float:
    impar_ant = numero - 1
else:
    impar_ant = numero - 2

print(par_post, impar_ant)

