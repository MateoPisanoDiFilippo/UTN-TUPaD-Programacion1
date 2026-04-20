'''Trabajo practico nº 7. "Estructuras de datos complejas".
Pisano Di Filippo Mateo Agustín. Comisión nº 8.'''

print('\nBienvenido al Trabajo Práctico nº 7 de Mateo.')



while True: #loop principal.

    menu = input('''\nIndique el ejercicio que desea ver (1 al 10) 
Si desea salir, escriba 0:
''') #pequeño menú con case para una mayor versatilidad a la hora de corrección del TP

    match menu:

        case '0':
            print('\nPrograma terminado. Gracias por participar.\n') #damos una opción de salida del programa.
            break

        case '1' | '2' | '3': #diccionario precios_frutas. Los 3 primeros ejercicios (ya que el 2 necesita la modificación del 1 y el 3 del 2)
                              #podria haber hecho una validación donde en el case 1 se complete el diccionario y, dependiendo de si está completo o no, pedir al usuario que regrese al punto 1, pero para este caso no lo vi conveniente.
            #ejercicio 1
            
            precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450} #diccionario
            
            print('\nEjercicio 1:\n')
            print(precios_frutas)  #hacemos un print primero del precios_frutas original para que el docente compare con el diccionario modificado          
            precios_frutas['Naranja'] = 1200  #modificamos el diccionario con nuevas key y values
            precios_frutas['Manzana'] = 1500
            precios_frutas['Pera'] = 2300
            print(precios_frutas) #imprimimos el diccionario ya modificado. El docente podrá comparar uno con otro.
            

            #ejercicio 2
            print('\nEjercicio 2:\n')
            
            precios_frutas['Banana'] = 1330  #modificamos los values
            precios_frutas['Manzana'] = 1700
            precios_frutas['Melón'] = 2800
            print(precios_frutas)

            #ejercicio 3
            print('\nEjercicio 3:\n')
            
            lista_frutas = list(precios_frutas) #creamos una lista con el diccionario y lo imprimimos.
            
            for i in range(len(lista_frutas)):
                print(lista_frutas[i], end=' ') #lo hacemos con for asi queda más presentable
            print()

        case '4':

            agenda_tel = {} #lista vacia

            
            print('Sea Bien venido a su agenda virtual. Podrá cargar hasta 5 números telefónicos.')

            #Primera parte:
            
            def pedir_contacto():  #función para ingresar y validar numero y agendado.
                
                persona = input('\nIngrese el nombre del contacto: ').title()
                while True:
                    numero = input('\nIngrese el teléfono del contacto, sin guiones y espacios: ').strip()
                    if not numero.isdigit():
                        print('\nDebe ingresar un número, evite guiones y espacios.')
                    else:
                        return persona, int(numero)
          
            persona_1, numero_1 = pedir_contacto()  #definimos  el key y el value
            persona_2, numero_2 = pedir_contacto()
            persona_3, numero_3 = pedir_contacto()
            persona_4, numero_4 = pedir_contacto()
            persona_5, numero_5 = pedir_contacto()

            agenda_tel [persona_1] = numero_1  #agregamos en el diccionario a cada uno.
            agenda_tel [persona_2] = numero_2
            agenda_tel [persona_3] = numero_3
            agenda_tel [persona_4] = numero_4
            agenda_tel [persona_5] = numero_5

            print(agenda_tel) #imprimimos la el diccionario para comprobar de que se hayan agendado.

            #segunda parte:

            while True:  #pequeño menú
                nombre_mostrar = input('''\nIndica el nombre de la persona agendada que deseas consultar. 
si deseas salir, escribe "salir":
''').title()
                if nombre_mostrar == 'Salir': #opción de salir
                    print('\nSaliendo')
                    break
                elif nombre_mostrar not in agenda_tel:  #nos fijamos que el nombre este en el diccionario
                    print('\nEse nombre no está en la agenda.')
                else:
                    print(agenda_tel[nombre_mostrar]) #mostramos el número en el caso de que esté.

        case '5': #ejercicio 5
            
            set_palabras = set()  #definimos un set vacio
            
            #primera parte: str a set

            frase = input('Escribe unas líneas para mí: ').lower() #ingreso de las palabras. .lower() para que cuente las palabras sin importar si las hemos puesto en mayuscula o minusciula.
            frase = frase.replace(',', '').replace('¿','').replace('?','').replace('¡','').replace('!','').replace('.','').replace(';','') #para eliminar los signos. debe de haber una manera más eficiente, pero esolo conozco esta.
            palabras = frase.split() #separamos las palabras (para que el set no se haga con las letras)
            set_palabras.update(palabras) #rellenamos el set.
            print(set_palabras)  #imprimimos el set.

            #segunda parte: diccionario con recuento.

            recuento = {} #diccionario

            for palabra in palabras: #ciclo for para recorrer las palabras previamente tratadas con .split()
                recuento[palabra] = recuento.get(palabra, 0) + 1 #evitamos el keyerror (en el caso de qie la paabra no esté)
                                                                    #sumamos 1 al recuento si existe.
            print(recuento)

        case '6': #Ejercicio 6:
            
            def alumno_notas(x): #hacemos una funcion para pedir nombre, notas y hacer las tuplas
                contador = 3
                while contador > 0:
                    
                    alumnos = input(f'\nIngresa el nombre del alumno: ').title()
                    
                    lista_notas = [] #vaciamos otra vez la lista
                    
                    for i in range(3): #for para pedir 3 notas y agregarlas a la lista.
                        while True:
                            notas = input(f'\nIngrese la {i + 1}º nota: ')
                            if not notas.isdigit:
                                print('Incorrecto, debe indicar números enteros.') #validamos que sea numero
                            else:
                                notas = int(notas) #transformamos a int
                            
                            if notas < 0 or notas > 10: #nos asercioramos de que este en el rango.
                               print('Incorrecto, debe ser un número entre el 0 y el 10') 
                            else:
                                lista_notas.append(notas) #agregamos notas a la lista
                                break
                        
                    tupla_notas = tuple(lista_notas) #transformamos esa lista y la combertimos en tupla
                    print(tupla_notas) #Esto es para controlar la tupla
                    diccionario_alumnos[alumnos] = tupla_notas #llenamos el diccionario
                    
                    contador -= 1 #le restamos al contador del while

                #aca termina la función (podria no haber usado función, pero lo hice por objetivos evaluativos)    

            diccionario_alumnos = {} #definimos el diccionario vacio
            lista_notas = [] #definimos la lista que más adelante nos servirá para hacer la tupla
                
            alumno_notas(1) #invocamos la fucion

            print(diccionario_alumnos) #imprimimos para ver que todo esté bien

            #recorremos el diccionario tal cual está explicado en los apuntes
            for clave, valor in diccionario_alumnos.items(): 
                print(f'\nPromedio de {clave} es {round(sum (valor) / 3, 2)}.') #hacemos los promedios y mostramos el de cada uno
                
        case '7':
            
            set_asistentes = set() #definimos set vacio
            asistencias = ['Ana', 'Luis', 'Ana', 'María', 'Luis', 'Pedro', 'Ana'] #lista dada de asistentes
            
            #Imprimimos en pantalla la lista.
            print('\nAsistencias totales:')
            for i in range(len(asistencias)):
                set_asistentes.add(asistencias[i]) #aprovechamos el for y llenamos el set
                print(asistencias[i], end ='||')
        
            print()
            
            print('\nAsistentes brutos:')

            for asistente in set_asistentes: #recorremos el set para extraer a los asistentes uno por uno 
                print(asistente)

            #estructura similar al ejercicio 5.
            conteo = {}

            for persona in asistencias:
                conteo[persona] = conteo.get(persona, 0) + 1

            print('\nVeces que asistió cada asistente:')
            for nombre, veces in conteo.items():
                print(f'{nombre}: {veces}')
            
              
        case '8':

            productos_stock = {} #diccionario vacio
            
            while True: #hacemos un menú
                menuproductos = input('''\nElija que acción desea realizar.
1.Agregar producto con su stock y cambiar stock de un producto
2.Consultar stock de un producto
3.Eliminar producto
4.Salir
''')        

                match menuproductos: #match case del menú
                    
                    case '1': #ingreso de producto y stock del mismo. en este menú tambien se puede agregar unidades a un stock existente.

                        while True:  #pequeña validacion y menu
                            
                            producto = input('''\nIngrese el nombre del producto.
Para salir indique 0: 
''').capitalize()
                            if producto == '0':
                                break
                            #-------------------------------------
                            # elif producto in productos_stock:
                            #     print('\nEste producto ya está en stock.')
                            # Este seria el condicional en el caso de que en esta opcion solo se puedan agregar productos
                            # pero decidí que aquí se puedan hacer varias acciones, por comodidad del usuario.
                            #--------------------------------------
                            else:
                                while True:
                                    stock = input('\nIndique la cantidad: ')
                                    if not stock.isdigit(): #validaciones .isdigit()
                                        print('\nInválido, ingrese un número entero positivo.')
                                    else:
                                        stock = int(stock)
                                        break
                                        
                                productos_stock[producto] = stock #agregamos producto y stock al diccionario
                                
                                for clave, valor in productos_stock.items(): #imprimimos para que lo vea cada vez
                                    print(f'{clave}:{valor}')
                    
                    case '2': #ver stock de un producto dado

                        if productos_stock == {}:
                            print('\nLista de productos vacia.')
                        else:
                            while True:
                                ver_producto = input('''\nIndique que producto desea ver. 
Para salir escriba 0: 
''').capitalize()
                                if ver_producto == '0':
                                    break
                                elif ver_producto not in productos_stock.keys():
                                    print('\nEse producto no está en la lista o está mal escrito.')
                                else:
                                    print(f'\n{ver_producto}: {productos_stock[ver_producto]} unidades')
                        
                    case '3': #Eliminar producto del diccionario. 
                              #como modificar stock ya se puede hacer desde el mismo menú que el de agregar producto y stock, 
                              #agregué esta opción por fines evaluativos.
                        
                        for clave, valor in productos_stock.items(): #imprimimos para que vea que productos tiene
                                    print(f'{clave}:{valor}')
                        
                        if productos_stock == {}:  #nos fijamos si la lista está ya cargada
                            print('\nLista de productos vacia.')
                        else:
                        
                            while True:
                            
                                producto_eliminar = input('''\nIngresa que producto desea eliminar.
Para salir escriba 0:
''').capitalize()
                                if producto_eliminar == '0':  #validaciones del menú interno
                                    break
                                elif producto_eliminar not in productos_stock.keys(): #vemos si el producto está cargado
                                    print('\nEse producto no está en la lista.')
                                else:
                                    selec = input(f'''\n¿Está seguro que desea eliminar {producto_eliminar}? 
Indique s/n:
''').lower()  #nos aseguramos si el usuario está seguro de remover el objeto
                                    if selec != 'n' and selec != 's': #validación 
                                        break
                                    elif selec == 'n':
                                        break
                                    else:
                                        del productos_stock[producto_eliminar] #eliminamos el producto
                                        print(f'\n{producto_eliminar} eliminado de la lista de productos.')
                    
                    case '4': #finalizamos programa
                        print('Programa terminado.')
                        break
                                
                    case _:
                        print('Invalido, ingrese una opción del 1 al 4.')
                    
        case '9': #agenda. Diccionario con tuplas

            agendado = {} #Diccionario vacio

            while True: #completamos la agenda (diccionario)
                
                lista_dia_hora = [] #lista vacia que nos permitirá crear las tuplas. Dentro del while así se reinicia

                #menú con cases
                menu_agenda_actividad= input('''\nIndique que accion desea realizar.
1.Agregar actividad (con día y hora)
2.Ver actividad según día y hora
3.Salir
''')
                match menu_agenda_actividad:
                    
                    case '1':
                        input_dia = input('''\nIndique el día
Para salir, indique 0:
''').capitalize()            
                        
                        if input_dia == '0': #opción de salida si el usuario se equivocó
                            print('\nAdios.')
                            break
                        else:
                            lista_dia_hora.append(input_dia) #agregamos el dia a la lista
                            input_hora = input('\nIndique la hora: ') #pedimos la hora
                            lista_dia_hora.append(input_hora) #la agregamos a la lista
                            tupla_dia_hora = tuple(lista_dia_hora) #agregamos a la puple
                            print(tupla_dia_hora) #imprimimos para corroborar de que esté bien
                            actividad = input('\nIndique la actividad: ').capitalize() #pedimos que actividad va a realizar
                            agendado[tupla_dia_hora] = actividad #agregamos todo al diccionario
                            

                        print(agendado) #imprimimos diccionario para ver que todo esté en orden.
                    
                    case '2':
                        
                        if agendado == {}: #corroboramos de que haya actividades cargadas
                            print('\nLa agenda está vacia.')
                        else:
                            while True:
                                
                                lista_consulta = [] #lista vacia que se vuelve a regenerar.
                                
                                consulta_dia = input('\nIndique el día, para salir indique 0:\n').capitalize()

                                if consulta_dia == '0': #Mecanismo de escape
                                    print('\nAdios.')
                                    break
                                else:
                                    #hacemos algo similar que en el punto 1:
                                    lista_consulta.append(consulta_dia)
                                    consulta_hora = input('\nIndique la hora exacta: ')
                                    lista_consulta.append(consulta_hora)
                                    tupla_consulta = tuple(lista_consulta)
                                    if tupla_consulta not in agendado: #chequeamos de que ese día y hora esten cargados
                                        print('\nEse día y hora no están agendados.')
                                    else:
                                        #consultamos en la agenda y mostramos por pantalla
                                        print(f'\nEse día a esa hora usted tiene agendado: {agendado[tupla_consulta]}')
                    case '3':
                        print('\nTerminado.')
                        break
                    case _:
                        print('Inválido, vuelve a intentarlo.')
                                        
                                    
        case '10':#invertir diccionario
            
            #definimos el diccionario original
            original = {"Argentina": 'Buenos Aires', 'Chile': 'Santiago', 'Paraguay':'Asunción'}

            #definimos el diccionario invertido vacio.
            invertido = {}
            
            #recorremos el original
            print('\nDiccionario original:')
            for clave, valor in original.items(): 
                print(f'{clave} : {valor}') #lo mostramos en pantalla de manera estética.
                invertido[valor] = clave  #llenamos el invertido cambiando key por value y value por key

            #recorremos el nuevo diccionario para mostrarlo por pantalla de manera estética.   
            print('\nDiccionario Invertido:') 
            for clave, valor in invertido.items():
                print(f'{clave} : {valor}') 
                                    
        case _: #controlamos que la entrada sea correcta.
            print('\nInválido, vuelva a intentarlo.') 