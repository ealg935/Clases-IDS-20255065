correo = input()


## buscar evaluar true/false

#instancias de ejemplo
 # aportillo@esen.edu.sv
 # alvin.portillo@gmail.com
 
condicion_1 = correo.count('@')==1
posicion_arroba = correo.index('@')
condicion_2_1 = posicion_arroba>=3    #se usa index para localizar el @#
condicion_2_2 = (len(correo)-posicion_arroba) > 4
condicion_3 = correo.count('.') >= 1
condicion_4 = correo.count(' ') == 0 
condicion_5_1 = correo [0] != '.'
condicion_5_2 = correo [-1] != '.'
print(condicion_1 and condicion_2_1 and condicion_2_2 and condicion_3 and condicion_4 and condicion_5_1 and condicion_5_2)


#pregunta 2#

cadena = input()
print(cadena.lower().count('z'))

#pregunta 3#

