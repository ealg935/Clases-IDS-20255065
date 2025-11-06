#enumerate = tira 2 listas de valores 
surnames = {'Rivest', 'Shamir', 'Adleman'}
for position, surnames in enumerate(surnames, start= 1): 
    print(position, surnames)

#izq key derecha value 
people = ['Nick', 'Rick', 'Roger', 'Syd']
ages = [23,24,23,21]
for p, a in zip(people, ages):
    print(p,a)
    
    