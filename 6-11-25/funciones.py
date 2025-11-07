#funciones#

'''def saludar():
    Nombre = input('Ingrese su nombre: ')
    Apellido = input('Ingrese su apellido: ')
    Nombre_completo = f'{Nombre.title()}{Apellido.title()}'
    print(f'Hola {Nombre_completo}')
    
saludar()   '''

def saludar_con_param(nombre, apellido):          #parametro#
    print(f'Hola {nombre.title()} {apellido.title()}')


saludar_con_param('Fer','Calvo')            #argumento#
saludar_con_param('Franco','Rosales')


def describir_mascota(animal, nombre_animal):
    print(f'Tengo un {animal.title()}, y su nombre es {nombre_animal.title()}')
    
describir_mascota('Perro','Firulais')