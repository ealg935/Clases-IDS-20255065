'''# set #

mi_gato = {'pelusa', 3, 'simpatico'} # [Nombre, edad, caracteristica]
print(type(mi_gato)) 

'''
'''#Diccionarios #
mi_gato = {
    'nombre': 'pelusa', 
    'edad': 3, 
    'personalidad': 'simpatico'}
abys_cat= {
    'personalidad': 'simpatico',
    'nombre': 'pelusa',
    'edad': 3}

copia = mi_gato == abys_cat
print(copia)


birthdays= {
    'Alice': 'Apr 1',
    'Bob': 'Dec 12',
    'Carol': 'Mar 4'
}

birthdays['Carol'] = 'Abr 21'
birthdays['Fer'] = 'Mar 3'
print(birthdays['Alice'])

del birthdays['Bob']
print(birthdays)
'''
semana = {}
semana['uno'] = 'Lunes'
semana['dos'] = 'Martes'
semana['tres'] = 'Miercoles'
semana['cuatro'] = 'Jueves'
semana['cinco'] = 'Viernes'
semana['seis'] = 'Sabado'
semana['siete'] = 'Domingo'
for i in semana.keys():
    print(i)

'''print(semana)'''