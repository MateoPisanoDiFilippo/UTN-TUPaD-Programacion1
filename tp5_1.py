while True:

    ejercicio = input('''
\nIndique qué número de ejercicio quiere visualizar. 
Utilice números del 1 al 13:\n''').lower()

    
 
    while not ejercicio.isdigit():
        ejercicio = input('''\nNo es un caracter válido.
Debe indicar un número del 1 al 13:\n''').lower()

   
    ejercicio = int(ejercicio)

    match ejercicio:

        
        case 1:
            
            import random

            lista_notas = [0] * 10 #lista vacia


            for i in range (10): 
                 notas_a = random.randint(0,10) #notas de manera aleatoria
                 if lista_notas [i] == 0:
                    lista_notas[i] = notas_a
                            

            for i, notas in enumerate(lista_notas, start=1):
                print(f"Nota {i}: {notas}") #output de la lista completa.
            
            promedio = sum(lista_notas) / len(lista_notas) #calculamos el promdeio
            list_menor_mayor = sorted(lista_notas) #hago una lista nueva, ordenada de menor a mayor. se que el indice 0 va a ser la menor nota y el indice 9 la mas grande.

            print(f'El promedio de notas es: {promedio}')
            print(f'''La nota más alta es: {list_menor_mayor[9]}
La nota más baja es: {list_menor_mayor[0]}''')

        
        case 2:

            lista_productos = [] #lista vacia

            for i in range (1, 6): #para que agreguen los productos
                while True:
                    producto = input(f'Indique el producto {i}: ').capitalize()

                    if not producto.isalpha():   #validación
                        print('No es una entrada válida.')
                    else:
                        lista_productos.append(producto) #añado el producto válidado a la lista
                        break

            lista_productos_2 = sorted(lista_productos) #creo una nueva lista ordenada.

            for i, producto in enumerate(lista_productos_2):
                print(producto) #output de la lista completa ordenada.


            while True:
                
                print()

                if lista_productos_2 != []:  #si no hay mas elementos en la lista, ya no pida elimnar más.
                    producto_remover = input('''Indique qué elemento desea remover.
Para terminar escriba 0: 
''').capitalize()   #input para remover un producto.
                
                    if producto_remover == '0':
                        break
                    elif producto_remover in lista_productos_2:
                            lista_productos_2.remove(producto_remover)
                    else:
                        print('\nEse producto no se encuentra en la lista.')
                    for i, producto in enumerate(lista_productos_2):
                        print(producto)
                else:
                    print('\nNo hay mas elementos en la lista.')
                    break

        
        case 3:

            import random

            lista_pares = []  #creo listas vacias
            lista_impares = []

            while len(lista_pares) < 15:
                numero = random.randint(1,100)    # hago ciclo while para que los numeros al azar se agreguen a la listas correspondientes.
                if numero % 2 == 0:
                    lista_pares.append(numero)
                                                 
            while len(lista_impares) < 15:
                numero = random.randint(1,100)
                if numero % 2 != 0:
                    lista_impares.append(numero)
            
            print('''
Los números pares son:''')
            for i, pares in enumerate(lista_pares):
                print(pares, end=' ')

            print('''
\nLos números impares son:''')
            for i, impares in enumerate(lista_impares):
                print(impares, end=' ')
                
            
        case 4:

            datos = [1,3,5,3,7,1,9,5,3]  #lista original
            datos_2 = []                #nueva lista vacia

            for numero in datos:    #verificación de que el numero no este repetido
                if numero not in datos_2:  #agregamos así el  numero si ya no estaá en nuestra lista nueva.
                    datos_2.append(numero)
            
            for i, dato in enumerate(datos_2):
                print(dato, end=' ')
            


        case 5:
            
            estudiantes = []

            for i in range (8): #ingreso de los estudiantes por parte del usuario
                 while True:
                    
                    nombre = input(f'Ingrese el nombre del estudiante {i+1}: ').title()
                    if not nombre.replace(' ','').isalpha():  # validación de nombre con apellido
                        print('No es válido.')     
                    else:
                        estudiantes.append(nombre)
                        break
            while True:
                
                eliminar_agregar = input('''Menú de opciones: (indique con el número correspondiente)
1. Agregar estudiante
2. Quitar estudiante
3. Mostrar lista
4. Salir
''')
                if not eliminar_agregar.isdigit():
                    eliminar_agregar = print('''No es una entrada válida. 
Indique el número correspondiente: ''')
                
                eliminar_agregar = int(eliminar_agregar)

                if eliminar_agregar == 1:
                    agregar = input('Indique el nombre que quiere agregar:\n').title()
                    if not agregar.replace(' ','').isalpha():
                        print('No es válido.')
                    else:
                        estudiantes.append(agregar)
                    
                elif eliminar_agregar == 2:
                    eliminar = input('Indique que estudiante quiere eliminar:\n').title()
                    if not eliminar.replace(' ', '').isalpha():
                        print('No es válido.')
                    if eliminar not in estudiantes:
                        print('Ese nombre no está en la lista.')
                    else:
                        estudiantes.remove(eliminar)
                
                elif eliminar_agregar == 3:
                    for i, nombres in enumerate(estudiantes):
                        print(f'Estudiantes {i+1}: {nombres}.')
      
                elif eliminar_agregar == 4:
                    print('Programa finalizado')
                    break
                
                else:
                    print('No es válido.')
                
                
        case 6:
            
            lista_rotar = []

            for i in range (1, 8): #ingreso con validación
                 while True:
                    numero = input(f'Ingrese el {i}º número: ')
                    if not numero.isdigit():
                        print('No es válido. Ingrese un número entero')
                    else:
                        lista_rotar.append(numero)
                        break
            
            print('Lista original:')                #mostramos lista original
            for i, n in enumerate(lista_rotar):
                        print(n, end=' ')
            
            ultimo = lista_rotar[-1] # variable que contiene el último numero de la lista

            lista_rotar = [ultimo] + lista_rotar[:-1] # modificamos la lista con esa nueva información
            
            print('\nLista hacia la derecha:')  # mostramos lista modificada
            for i, n in enumerate(lista_rotar):
                        print(n, end=' ')

        case 7:

            import random

            temperatura_semanal = [
                [0]*2,
                [0]*2,
                [0]*2,
                [0]*2,
                [0]*2,
                [0]*2,
                [0]*2
            ]
                             
                                                    
            for j in range(7):                   # asigno de manera aleatoria los números en la matriz.
                minimas = random.randint(3, 8)
                maximas = random.randint(10, 25)   # asignamos una temperatura templada, cercana a la temperaturas posibles en otoño.
                if temperatura_semanal[j][0] == 0:
                    temperatura_semanal[j][0] = minimas
                if temperatura_semanal[j][1] == 0:
                    temperatura_semanal[j][1] = maximas

            for fila in range(len(temperatura_semanal)):
                print(f'Temperaturas día {fila + 1}:')         #imprimimos las temperaturas para ver que no hayan quedado mal.
                for columna in range(len(temperatura_semanal[0])):
                    print(f'|{temperatura_semanal[fila][columna]}|', end=' ')
                print()
            

            tmin = 0
            tmax = 0

            for sublista in temperatura_semanal:
                tmin += sublista[0]    #sumamos las temperaturas minimas (en el indice 0)
                tmax += sublista[1]    #sumamos las temperaturas maximas (indice 1)
            
            promedio_minimas = tmin / 7   #prmediamos
            promedio_maximas = tmax / 7   

            
            print(f'\nEl promedio de temperaturas mínimas son: {promedio_minimas}.')
            print(f'\nEl promedio de temperaturas máximas son: {promedio_maximas}.')

            #calculo la amplitud termica:

            mayor_amplitud = 0
            dia = 0

            for i in range(len(temperatura_semanal)):
                amplitud = temperatura_semanal[i][1] - temperatura_semanal[i][0]

                if amplitud > mayor_amplitud:
                    mayor_amplitud = amplitud
                    dia = i + 1

            print(f'\nEl día con mayor amplitud termica es el día {dia}.')


        case 8:
            
            import random

            est_mat = [
                [0] * 3,   #cada sublista es un estudiante y cada indice la nota de una de las materias
                [0] * 3,
                [0] * 3,   
                [0] * 3,
                [0] * 3
            ]
 
            for i in range (len(est_mat[0])): # asigno de manera aleatoria los números en la matriz.
                for j in range(len(est_mat)):   #i será lo que son los indices dentro de las sublistas y j las sublistas.
                    notas = random.randint(0, 10)   
                    if est_mat[j][i] == 0:
                        est_mat[j][i] = notas
            
            
            for fila in range(len(est_mat)):
                print(f'Notas estudiante {fila + 1}:')   #imprimimos las notas de los estudiantes (para hacer una revisión a mano de los promedios)
                for columna in range(len(est_mat[0])):
                    print(f'Materia {columna + 1} : |{est_mat[fila][columna]}|', end=' ')
                print()
            
            
            
            #calculo del promedio de cada estudiante:
            for i in range(len(est_mat)):
                promedio_estudiante = sum(est_mat[i]) / len(est_mat[i])
                print(f'El promedio de estudiane {i+1} es: {promedio_estudiante:.2f}')

            #calculo del promedio por materia:

            materia1 = 0   # Defino las variables a 0 para despues sumar cada indice correspondiente de cada sublista
            materia2 = 0
            materia3 = 0

            for est in est_mat:
                materia1 += est[0]    #est va a ser cada estudiante (las sublistas). 
                materia2 += est[1]    #a cada materia le sumo el indice (nota) correspondiente de cada sublista (estudiante)
                materia3 += est[2]

            promedio1 = materia1 / len(est_mat)   #hago los promedios
            promedio2 = materia2 / len(est_mat)
            promedio3 = materia3 / len(est_mat)

            print(f'\nEl promedio total de la materia 1 es: {promedio1}')
            print(f'El promedio total de la materia 2 es: {promedio2}')
            print(f'El promedio total de la materia 3 es: {promedio3}')
            
        case 9:     #este ejercicio se me hizo muy dificil. Es probable que me hayan quedado bugs de los que no me enteré. 
                    
            
            juego_terminado = False
   
            print('\nJUGUEMOS AL TA-TE-TI.\n')
     
            #Definimos el tablero (matriz)
            
            tateti = [
                    ['-','-','-'],
                    ['-','-','-'],
                    ['-','-','-']
                ]

            while not juego_terminado:
                
                    #Turno jugador x:
                
                while True:


                    print('\nTurno del jugador x.\n')

                    for f in range(len(tateti)):
                        for c in range(len(tateti[0])):
                            print(tateti[f][c], end=' ')
                        print()

                    fila = input('\nElije la fila. 1, 2 o 3: ')   #pedimos la fila y la validamos
                    
                    if not fila.isdigit():       #validación para que sea un entero
                        print('Inválido')
                        continue
                    
                    fila = int(fila)
                    
                    if fila < 1 or fila > 3:   #validamos que este en el rango que queremos.
                        print('Debe ser un número del 1 al 3')
                        continue

                    columna = input('Elije la columna. 1, 2 o 3: ')  #pedimos la columna y la validamos

                    if not columna.isdigit():
                        print('Inválido')
                        continue
                    
                    columna = int(columna)
                    
                    if columna < 1 or columna > 3:
                        print('Debe ser un número del 1 al 3')
                        continue

                    if tateti[fila-1][columna-1] == '-':    #verificación de espacios ocupados
                        tateti[fila-1][columna-1] = 'x'
                        break
                    else:
                        print('Ese espacio está ocupado.')
                        continue
        
                #definimos si gano x     
                
                gano = False  
                
                for fil in range(len(tateti[0])):
                    if tateti[fil][0] == tateti[fil][1] == tateti[fil][2] == 'x':   #horizontales (las filas)
                        gano = True
                    if tateti[0][fil] == tateti[1][fil] == tateti[2][fil] == 'x':   #Verticales
                        gano = True
                        
                if tateti[0][0] == tateti[1][1] == tateti[2][2] == 'x':   #diagonal descendente
                    gano = True

                if tateti[2][0] == tateti[1][1] == tateti[0][2] == 'x':   #diagonal ascendente
                    gano = True
                    
                if gano:                                   #en el caso de ganar (gano = True) le pedimos que imprima el tablero más el ha ganado y que termine el juego
                    for f in range(len(tateti)):
                        for c in range(len(tateti[0])):
                            print(tateti[f][c], end=' ')
                        print()
                    print('Ha ganado X.')
                    break
                        
                        
                #si estan todas las casillas llenas.
                
                lleno = True

                for fila_tablero in tateti:  #recorremos todo la matriz(el tablero) e identificamos si hay o no un espacio 'vacio'.
                    if '-' in fila_tablero:
                        lleno = False       #en el caso de haber un espacio 'vacio' le cambio el estado de lleno = True por lleno = False

                if lleno:                                  #le decimos que los si los espacios estan llenos (True), imprima el tablero y que termine eljuego
                    
                    for f in range(len(tateti)):           #f es por filas, c es por columnas
                        for c in range(len(tateti)):
                            print(tateti[f][c], end=' ')
                        print()
                    print('No hay más lugar.')
                    break

                #turno de o
                
                while True:               

                    print('\nTurno del jugador o.\n')

                    for f in range(len(tateti)):
                        for c in range(len(tateti[0])):    #imprime el tablero
                            print(tateti[f][c], end=' ')
                        print()

                    fila = input('\nElije la fila. 1, 2 o 3: ')   #pedimos la fila y la validamos
                    
                    if not fila.isdigit():    #validación de input
                        print('Inválido')
                        continue
                    
                    fila = int(fila)
                    
                    if fila < 1 or fila > 3:
                        print('Debe ser un número del 1 al 3')
                        continue

                    columna = input('Elije la columna. 1, 2 o 3: ')  #pedimos la columna y la validamos

                    if not columna.isdigit():
                        print('Inválido')
                        continue
                    
                    columna = int(columna)
                    
                    if columna < 1 or columna > 3:
                        print('Debe ser un número del 1 al 3')
                        continue
                    
                    if tateti[fila-1][columna-1] == '-':
                        tateti[fila-1][columna-1] = 'o'
                        break
                    else:
                        print('Ese espacio está ocupado.')
                        continue              

                #definimos como ganaría o:
                
                gano = False  
                
                for fil in range(len(tateti[0])):
                    if tateti[fil][0] == tateti[fil][1] == tateti[fil][2] == 'o':   #horizontales (las filas)
                        gano = True
                        
                    if tateti[0][fil] == tateti[1][fil] == tateti[2][fil] == 'o':   #Verticales
                        gano = True
                        
                if tateti[0][0] == tateti[1][1] == tateti[2][2] == 'o':   #diagonal descendente
                    gano = True

                if tateti[2][0] == tateti[1][1] == tateti[0][2] == 'o':   #diagonal ascendente
                    gano = True
                    
                if gano:
                    for f in range(len(tateti)):
                        for c in range(len(tateti[0])):
                            print(tateti[f][c], end=' ')
                        print()
                    print('Ha ganado O.')
                    break


                #si estan todas las casillas llenas.   repetimos lo que hicimos más arriba
                
                lleno = True

                for fila_tablero in tateti:  
                    if '-' in fila_tablero:
                        lleno = False

                if lleno:                                  
                    for f in range(len(tateti)):           
                        for c in range(len(tateti)):
                            print(tateti[f][c], end=' ')
                        print()
                    print('Empate.')
                    break
                
        case 10:
            
            import random
            
            productos_dias = [         #dias van a ser las columnas (7), los productos las filas(4)
                [0] * 7,
                [0] * 7,
                [0] * 7,
                [0] * 7               
            ]

            for i in range (len(productos_dias[0])): #ccon esta estructura asignamos de manera aleatoria los números en la matriz.
                for j in range(len(productos_dias)):   #i será lo que son los indices dentro de las sublistas y j las sublistas.
                    producto = random.randint(0, 200)   #puse de 0 a 200 para que haya un límite claro en el total de las ventas màximas y minimas.
                    if productos_dias[j][i] == 0:
                        productos_dias[j][i] = producto
                
            #Venta de producto por día: (mostrar como quedó la matriz despues del random.randint)
            
            for fila in range(len(productos_dias)):
                print(f'producto nº {fila + 1}:')   
                for columna in range(len(productos_dias[0])):
                    print(f'Día {columna + 1 }:|{productos_dias[fila][columna]}| unidades.', end=f' ')
                print()

            #total de unidades vendidas por cada producto (la suma de cada uno por cada día de la semana.)
           
            producto_mayor = float('-inf')
            
            for p in range(len(productos_dias)):   #un bucle for. Recorre la matriz y así no tenemos que repetir 4 veces la misma operación a mano.
                total_producto = sum(productos_dias[p])
                if total_producto > producto_mayor:          #para saber que total es mayor (esto va a ser necesario para saber cual es el producto más vendido)
                    producto_mayor = total_producto
                print(f'El total de unidades vendidas del producto nº {p + 1} son: {total_producto}')
                
            #día con mayores ventas totales:
            
            dia_mayor = float('-inf')
            dia = None
            
            print()
            
            for d in range (len(productos_dias[0])):    #recorro la matriz y sumo cada uno de los días.
                suma = 0
                for pr in range(len(productos_dias)):
                    suma += productos_dias[pr][d]
                
                print(f'Día {d+1} suma: {suma}')     #muestro la suma en cada día (lo utilicé como debug, lo dejé para que ustedes puedan controlar si el día con mayor ventas está bien)

                if suma > dia_mayor:     #identifico cual es la suma más grande.
                    dia_mayor = suma
                    dia = d              #identifico a que indice (d) corresponde ese día con más ventas
            
            print(f'\nLa mayor cantidad de ventas, con {dia_mayor} unidades, se encuentra en el día: {dia+1}.')        

            #producto más vendido en la semana
            
            for m in range(4):
                if sum(productos_dias[m]) == producto_mayor:
                    producto_mas_vendido = m + 1
            
            print(f'\nEl producto más vendido semanalmente es el nº {producto_mas_vendido}')
                

        case 11:
            
            #Lista con 10 nombres:
                
            estudiantes = [
                'Zulema', 'Tulio', 'Filomena', 'Teodorica', 'Ataulfo', 
                'Transfiguracion', 'Rodrigo', 'Amparo', 'Justiniano', 'Belisario'
                ]

            
            while True:       #bucle para repetir el programa

                print('\nLista de estudiantes:')

                for i in range(len(estudiantes)):
                    print(f'.{estudiantes[i]}')
        
                
                nombre_buscar = input('''\nIngrese el nombre del estudiante.      
Para terminar el programa escriba 'salir':
''').title()
 
                if not nombre_buscar.isalpha():        #validación sencilla de nombre
                    print('\nNo es válido.\n')

                elif nombre_buscar == 'Salir':       #salir del bicle
                    print('\nHasta luego.')
                    break

                elif nombre_buscar not in estudiantes:               #ver si el nombre está en la lista
                    print('\nEse nombre no se encuentra en la lista.\n')

                elif nombre_buscar in estudiantes:                 #de estarlo:
                    print(f'''\nEse nombre se encuentra en el indice: {estudiantes.index(nombre_buscar)}.
Pero se encuentra en la posición: {(estudiantes.index(nombre_buscar)) + 1}''')     #salida diciendo el indice + la posición real.
                    

        case 12:

            numeros_lista = []

            for i in range (1, 9): #ingreso con validación
                 while True:
                    numero = input(f'Ingrese el {i}º número: ')
                    if not numero.isdigit():
                        print('No es válido. Ingrese un número entero')
                    else:
                        numeros_lista.append(numero)
                        break

            numeros_menor_mayor = sorted(numeros_lista) # lista nueva de menor a mayor

            numeros_mayor_menor = sorted(numeros_lista, reverse = True) #lista nueva de mayor a menor

      
            print('Lista original:')                #mostramos lista original
            for i, n in enumerate(numeros_lista):
                        print(n, end=' ')

            print('\nLista de menor a mayor:')                #mostramos lista ordenada menor a mayor
            for j, n1 in enumerate(numeros_menor_mayor):
                        print(n1, end=' ')
            
            print('\nLista de menor a mayor:')                #mostramos lista ordenada mayor a menor
            for k, n2 in enumerate(numeros_mayor_menor):
                        print(n2, end=' ')

        case 13:

            puntajes = [
                450, 1200, 875, 990, 300, 1500, 640
            ]

            ranking = sorted(puntajes, reverse = True)

            print(f'''\nEl puntaje más alto es: {ranking[0]}.
El puntaje más bajo es : {ranking[-1]}.''')
            
            
            print('\nRanking:')                
            for i, n in enumerate(ranking):
                print()
                print(f'El puesto nº {i + 1} con: {n} puntos' , end='')

            print(f'''
\nEl puntaje {ranking[2]} se encuentra en el puesto º {ranking.index(990) + 1}.''')

        case _:
            print('\nNo es válido.')