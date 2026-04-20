""" Primer examen parcial. Programación I. UTN. 
    
    Pisano Di Filippo Mateo Agustín """

"""INICIO"""

lista_herramientas = None  #variables para poder discriminar, más abajo, si la lista está llena o vacia.
lista_stock = None
ejecutando = True   #para despues poder salir del loop

while ejecutando:  #While para que el menú se repita hasta que la condición sea False

    #Menú de inicio:
    menu = input('''\nIngrese el número de la opción que desea realizar: 

1.Carga inicial de productos
2.Carga inicial de stock de cada producto
3.Inventario de productos
4.Productos en existencia
5.Reporte de agotados
6.Alta de nuevo producto
7.Actualización de stock (venta/ingreso)
8.Salir

''')

    match menu:  #entradas de menú

        case '1':
  
            while True: #que se repita hasta que sea False.
            
                if lista_herramientas == None:  #verificamos que el usuario no tenga ya una lista cargada.
                    carga_productos = input('''\nUsted está por cargar una lista de productos. 
¿Está seguro de querer continuar? s/n:
''').lower() #hacemos una confirmación previa por si el usuario se confundió de número

                    if carga_productos != 's' and carga_productos != 'n':  #validación.
                        print('\nDebe ingresar s o n')
                    else:
                        if carga_productos == 'n':  #importante, ya que es la validación negativa. Esto hace que vuelva al menú principal
                            break
                        if carga_productos == 's':
                            
                            while True: #Bucle para indicar el tamaño de la lista de herramientas.
                                cantidad_herramientas = input('\nIndique, en números enteros, qué cantidad de productos tendrá la lista: ')
                                #definición del tamaño de la lista. la lista comienza a existir.
                                if not cantidad_herramientas.isdigit():  #validación de la cantidad.
                                    print('\nDebe indicar un número entero positivo.')
                                else:
                                    cantidad_herramientas = int(cantidad_herramientas)
                                    if cantidad_herramientas == 0:    
                                        print('\nLa cantidad de productos debe ser mayor a 0.')
                                    else:
                                        lista_herramientas = [0] * cantidad_herramientas  #definimos la lista (le damos un tamaño)
                                        break
                        #ingresamos herramientas a la lista. con un bucle for, teniendo en cuenta el largo de la lista.
                        for i in range(len(lista_herramientas)):
                            while True:    
                                producto = input(f'\nIngrese el producto {i+1}: ').title()
                                if not producto.strip():   #verificamos que no esté vacia la entrada
                                    print('\nInválido. Intente nuevamente.')
                                elif producto in lista_herramientas: #verificamos que el producto no esté ya en la lista
                                    print('\nEse producto ya está cargado.')
                                else:
                                    lista_herramientas[i] = producto #cargamos producto en la lista
                                    break
                        break  #importante para romper el while de más arriba
                else:
                    print('\nUsted ya tiene una lista de productos cargada.')
                    break
              
        case '2':
            
            if lista_herramientas == None:  #verificamos de que la lista exista
                print('''\nDebe crear la lista de productos primero.
Vuelva y seleccione 1 en el menú.''')
            elif lista_stock == None:   #verificamos que la lista stock no exista previamente.
            
                lista_stock = [0] * len(lista_herramientas) #definimos el tamaño de la lista de productos
                
                for i in range (len(lista_herramientas)):  #Bucle for para agregar a la lista_stock
                     while True:
                        stock = input(f'\nIngrese la cantidad de unidades de "{lista_herramientas[i]}": ')
                        if not stock.isdigit(): #validamos que stock sea un numero entero positivo.
                            print('\nNo es válido. Ingrese un número entero positivo')
                        else:
                            stock = int(stock)
                            lista_stock[i] = stock
                            break
            else:
               print('\nLa lista con el stock ya está cargada.')  #si ya existe, salimos.
                
        case '3':
            
            if lista_herramientas == None: #verificamos que exista la lista de herramientas
                print('''\nHace falta definir los productos antes. 
Vuelva al menú y seleccione la opción 1.''')
            elif lista_stock == None:  #verificamos que exista la lista de stock
                print('''\nHace falta definir la cantidad de unidades de cada producto.
Vuelva al menú y seleccione la opción 2.''')
            else:
                for i in range(len(lista_herramientas)):
                    print(f'"{lista_herramientas[i]}": {lista_stock[i]}') #ciclo for para que muestre todo el inventario con el producto con el stock

        case '4':
            
            if lista_herramientas == None: #verificamos que exista la lista de herramientas
                print('''\nHace falta definir los productos antes. 
Vuelva al menú y seleccione la opción 1.''')
            elif lista_stock == None:  #verificamos que exista la lista de stock
                print('''\nHace falta definir la cantidad de unidades de cada producto.
Vuelva al menú y seleccione la opción 2.''')

            else:
                while True:
                    producto_encontrar = input('\nIndique qué producto desea ver: ').title()
                    
                    #validaciones de el producto que queremos encontrar
                    if not producto_encontrar.strip():  #vemos que no haya espacios
                        print('\nInvalido, intente nuevamente.')
                    elif not producto_encontrar in lista_herramientas:  #vemos que el producto esté en la lista
                        print('\nEse producto no se encuentra en la lista de herramientas.')
                    else:
                        posicion = lista_herramientas.index(producto_encontrar)  #index sirve para saber en que posición está el producto
                        print(f'\n"{lista_herramientas[posicion]}": {lista_stock[posicion]}')  #dado que el producto está en el mismo indice que las unidades, usamos la misma variable
                        break
        
        case '5':
            
            if lista_herramientas == None: #verificamos que exista la lista de herramientas
                print('''\nHace falta definir los productos antes. 
Vuelva al menú y seleccione la opción 1.''')
            elif lista_stock == None:  #verificamos que exista la lista de stock
                print('''\nHace falta definir la cantidad de unidades de cada producto.
Vuelva al menú y seleccione la opción 2.''')
            else:
                agotados = False  #asumimos que no hay agotados 
                for i in range(len(lista_herramientas)):  #hacemos un for para buscar los productos agotados y los imprimimos
                    if lista_stock[i] == 0:
                        print(f'\n"{lista_herramientas[i]}" está agotado.')
                        agotados = True
                if not agotados:
                    print('\nHay stock en todos los productos.')  #en el caso de que no haya productos agotados, lo indicamos.

        case '6':
            
            if lista_herramientas == None: #verificamos que exista la lista de herramientas
                print('''\nHace falta definir los productos antes. 
Vuelva al menú y seleccione la opción 1.''')
            elif lista_stock == None:  #verificamos que exista la lista de stock
                print('''\nHace falta definir la cantidad de unidades de cada producto.
Vuelva al menú y seleccione la opción 2.''')
            else:
                carga_nuevo_producto = input('''\nUsted está por cargar un producto nuevo.
¿Está seguro de querer continuar? s/n:
''').lower() #hacemos una confirmación previa por si el usuario se confundió de número en el menú

                if carga_nuevo_producto != 's' and carga_nuevo_producto != 'n':  #validación.
                        print('\nDebe ingresar s o n')
                else:
                    while True:
                    
                        if carga_nuevo_producto == 'n':  #importante, ya que es la validación negativa. Esto hace que vuelva al menú principal
                            break
                        elif carga_nuevo_producto == 's':
                            
                            nuevo_producto = input('Ingrese el nuevo producto: ').title() #Ingresamos un nuevo producto
                            if not nuevo_producto.strip():
                                print('\nInválido, nombre vacio.')
                            elif nuevo_producto in lista_herramientas:
                                print('\nEste producto ya está cargado.')
                            else:
                                nuevo_stock = input(f'\nIngrese la cantidad de unidades de "{nuevo_producto}": ')
                                if not nuevo_stock.isdigit() or int(nuevo_stock) < 0:
                                    print('\nNo es válido. Ingrese un número entero positivo.')
                                else:
                                    lista_herramientas.append(nuevo_producto)       
                                    lista_stock.append(int(nuevo_stock))  # sincronizamos lista_stock
                                    print('El producto se agregó correctamente')           
                        break #para salir del bucle de carga de producto.           
                      
        case '7':

            if lista_herramientas == None: #verificamos que exista la lista de herramientas
                print('''\nHace falta definir los productos antes. 
Vuelva al menú y seleccione la opción 1.''')
            elif lista_stock == None:  #verificamos que exista la lista de stock
                print('''\nHace falta definir la cantidad de unidades de cada producto.
Vuelva al menú y seleccione la opción 2.''')
            else:
                carga_nuevo_stock = input('''\nUsted está por modificar el stock de la lista de productos. 
¿Está seguro de querer continuar? s/n:
''').lower() #hacemos una confirmación previa por si el usuario se confundió de número en el menú

                if carga_nuevo_stock != 's' and carga_nuevo_stock != 'n':  #validación.
                        print('\nDebe ingresar s o n')
                else:
                    mini_menu = True
                    
                    while mini_menu:
                        if carga_nuevo_stock == 'n':  #importante, ya que es la validación negativa. Esto hace que vuelva al menú principal
                            break
                        elif carga_nuevo_stock == 's':
                            while True:   #hacemos un pequeño menu de venta/ingreso, utilizamos match case.
                                opcion_stock = input('''\nElija la opción correspondiente:  
1.Venta
2.Ingreso
3.Salir
''')
                                match opcion_stock:

                                    case '1':
                                        
                                        while True:
                                        
                                            producto_vendido = input('\nIndique el producto: ').title()
                                            
                                            if not producto_vendido.strip():
                                                print('\nInvalido, intente nuevamente.') #aseguramos que haya entrada
                                            elif producto_vendido not in lista_herramientas: #vemos que el producto esté en la lista
                                                print('\nEse producto no se encuentra en la lista de herramientas.')
                                                break
                                            else:
                                                posicion_venta = lista_herramientas.index(producto_vendido) #definimos la posicion del producto/stock
                                                
                                                if lista_stock[posicion_venta] <= 0:   #verificamos que el producto tenga stock
                                                    print('\nNo hay stock en este producto.')
                                                    break
                                                else:
                                                    if lista_stock[posicion_venta] > 0:
                                                        cantidad_vendida = input('''\nIngrese la cantidad de productos vendidos.
Si desea salir, escriba 0:
''') #una opcion por si el usuario se equivocó.
                                                        if not cantidad_vendida.isdigit():
                                                            print('\nDebe ingresar un número entero positivo.')
                                                        else:
                                                            cantidad_vendida = int(cantidad_vendida)
                                                            if cantidad_vendida == 0:
                                                                break
                                                            elif cantidad_vendida > lista_stock[posicion_venta]:
                                                                print('\nLa cantidad vendida no puede ser mayor que el stock original del producto.')
                                                                break
                                                            else:
                                                                lista_stock[posicion_venta] -= cantidad_vendida
                                                                print('\nStock actualizado')
                                                                break        
                                    case '2':
                                        while True:
                                            producto_ingresar = input('\nIndique el producto: ').title()
                                            if not producto_ingresar.strip():
                                                print('\nInvalido, intente nuevamente.') #aseguramos que haya entrada
                                            elif producto_ingresar not in lista_herramientas: #vemos que el producto esté en la lista
                                                print('\nEse producto no se encuentra en la lista de herramientas.')
                                                break
                                            else:
                                                posicion_ingreso = lista_herramientas.index(producto_ingresar) #definimos la posicion del prodcuto/stock
                                                cantidad_ingresada = input('''\nIndique la cantidad de unidades a ingresar. 
Si desea salir, escriba 0: 
''')   #ponemos una salida opcional en el caso de error por parte del usuario.
                                                if not cantidad_ingresada.isdigit():
                                                    print('\nInválido. Ingrese un número entero positivo.')
                                                else:
                                                    cantidad_ingresada = int(cantidad_ingresada)
                                                    if cantidad_ingresada == 0:
                                                        break
                                                    else:
                                                        lista_stock[posicion_ingreso] += cantidad_ingresada
                                                        print('\nStock actualizado')
                                                        break
                                    case '3':
                                        mini_menu = False  #salida rapida del mini_menu
                                        break
                                    case _:
                                        print('No es una opción válida.')
        
        case '8': #finalización del programa.

            while True:
                
                salir_programa = input('''\nUsted está por salir del programa. 
¿Está seguro de querer continuar? s/n:
''').lower()
                if salir_programa == 's':    #Validaciones por si el usuario se equivoco de numero en el menú
                    print('\nPrograma finalizado.')
                    ejecutando = False
                    break
                elif salir_programa == 'n':
                    break
                else:
                    print('\nNo es una entrada válida.')

        case _: #todo lo que no corresponda dentro del menú.
            print('''\nNo corresponde a una entrada válida. 
Debe ingresar un número dentro del rango del menú (1 a 8)\n''')