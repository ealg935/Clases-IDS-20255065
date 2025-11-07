#dui)
def dui_validacion():
    dui = input("Digite su DUI:")
    cantidad_condicion = 0
    if len(dui) == 10:
        cantidad_condicion += 1
    if dui.find("-") == 1:
        cantidad_condicion += 1
    antes, despues = dui.split("-")
    if len(despues)== 1:
        cantidad_condicion += 1
    
    print(f"Cumple {cantidad_condicion} condiciones")
        
    

    

dui_validacion()