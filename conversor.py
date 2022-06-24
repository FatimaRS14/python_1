#Programacion modular 
def convesor(pesos, valor_dolar):
     #inicia el bloque de codigo para ejecutar las opciones 
    pesos = input ("Cuanto dinero tienes?: ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    #Print es para imprimir el contenido en la pantalla
    print("Tienes $" + dolares + " dolares")

menu = """
Bienvenido al conversol de monedas💰

1- Pesos colombianos
2- Pesos argentinos
3- Pesos Mexicanos

Elige una opcion: """

opcion = int(input(menu))

if opcion == 1:
    convesor("colombianos" , 3875)

elif opcion ==2:
     convesor("argentinos" , 124.09)
   
elif opcion ==3:
   convesor("mexicanos" , 20.20)

else:
    print('Por favor ingresa una opcion valida')


