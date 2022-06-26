def run():
    mi_diccionario ={
    'llave1': 1,
    'llave2': 2,
    'llave3': 3,
    }

    #print(mi_diccionario)
    #print(mi_diccionario['llave1'])
    #print(mi_diccionario['llave2'])
    #print(mi_diccionario['llave3'])

    vews_dramas ={
        'The Untamed': 30000,
        'f4 Thailand': 4560,
        'Leyend of Fei': 24567,



    }

    #print(vews_dramas['f4 Thailand'])
    #como recorrer el diccionario y que regrese los datos
    #for dramas in vews_dramas.keys():
        #print(dramas)
        #con esta forma de declarasion del metodo se imprimen los valores de las llaves 

    #for dramas in vews_dramas.values():
        #print(dramas)
# de este modo se imprimen los valores 
     #la palabra especial items sirve para 
    for dramas, vews in vews_dramas.items():
        print(dramas + ' tiene ' + str(vews) + ' vistas ')

if __name__ == '__main__':
    run()

