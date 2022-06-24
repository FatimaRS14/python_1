menu="""
Bienvenido al conversol de monedas💰

1- Pesos colombianos
2- Pesos argentinos
3- Pesos Mexicanos

Elige una opcion"""

opcion = input(menu)

if opcion == 1:
    #inicia el bloque de codigo para ejecutar las opciones 
    pesos = input ("Cuanto dinero tienes?: ")
    pesos = float(pesos)
    valor_dolar = 3.910 
    dolares = pesos / valor_dolar
    dolares = str(dolares)
    #Print es para imprimir el contenido en la pantalla
    print("Tienes $" + dolares + "dolares")

elif opcion ==2:
    pesos = input ("Cuanto dinero tienes?: ")
    pesos = float(pesos)
    valor_dolar = 124.09 
    dolares = pesos / valor_dolar
    dolares = str(dolares)
    #Print es para imprimir el contenido en la pantalla
    print("Tienes $" + dolares + "dolares")
elif opcion ==3:
    pesos = input ("Cuanto dinero tienes?: ")
    pesos = float(pesos)
    valor_dolar = 20.20 
    dolares = pesos / valor_dolar
    dolares = str(dolares)
    #Print es para imprimir el contenido en la pantalla
    print("Tienes $" + dolares + "dolares")
else:
    print('Porfavir ungresa una opcion valida')


