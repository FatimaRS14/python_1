def palindromo(palabra):
    palabra = palabra.replace(' ', '')
    palabra = palabra.lower()
    palabra_invertida = palabra[:: -1]
    if palabra == palabra_invertida:
        return True
    else:
        return False



#funcion principal def/run-estandar
def run():
    palabra = input('Escribe una palabra: ')
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print('Es palindromo')
    else:
        print('No es palindromo')



#punto de entarada para correr el sistema como en java 
if __name__ == '__main__':
    run()

