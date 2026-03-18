#TP integrador – Repetitivas- Condicionales y Secuenciales.

while True:

    ejercicio = input('Ingrese el número de ejercicio que quiere ver, para finalizar escriba "salir":\n').lower()

    if ejercicio == 'salir':
        print('Programa finalizado, que tenga buena vida.')
        break

    match ejercicio:

# ejercicio 1: Caja de quiosco
    
        case '1':
            
            nombre_cliente = input('Hola, ¿cuál es tu nombre?:\n').capitalize()

            while nombre_cliente == '':
                nombre_cliente = input('Debe ingresar un nombre:\n')

            cant_productos = input('Ingrese la cantidad de productos a comprar:\n')

            while not cant_productos.isdigit() or int(cant_productos) <= 0:
                cantidad = input("Por favor, ingrese un número entero positivo:\n")

            cant_productos = int(cant_productos)

            total_descuento = 0
            total_no_descuento = 0


            for i in range(1, cant_productos + 1):
                precio = input(f'Producto {i}, precio: $ ')
   
                while not precio.isdigit():
                    precio = input(f'''No es correcto. Ingrese un número válido: 
Producto {i}, precio: $ ''')
                
                precio = int(precio)
                
                descuento = input(f'Producto {i} tiene descuento? (S/N): ').upper()
                
                while descuento != 'S' and descuento != 'N':
                    descuento = input('Entrada equivocada. Debe indicar S/N: ').upper()

                if descuento == 'S':
                    precio_final = precio - (precio * 0.1)
                else:
                    precio_final = precio
                    
                total_descuento += precio
                total_no_descuento += precio_final
                
            ahorro = total_no_descuento - total_descuento
                
            promedio = total_descuento / cant_productos  

            print(f'''Cliente: {nombre_cliente}
Cantidad de productos: {cant_productos}
Total sin descuento: ${total_no_descuento}
total con descuento: ${total_descuento:.2f}
Ahorro total ${ahorro:.2f}
Promedio por producto: {promedio:.2f}''')



#ejercicio 2: “Acceso al Campus y Menú Seguro”

        case '2':

            usuario_correcto = 'alumno'
            clave_correcta = 'python123'            
            
            print('Ingrese Usuario y Clave. Tiene 3 intentos.\n')
            
            usuario = input(f'Usuario: ')
            clave = input(f'Clave: ')
            
            intentos = 2
            
            while usuario != usuario_correcto or clave != clave_correcta:
                               
                print(f'''
Error: credenciales inválidas
Ahora tiene {intentos} intentos.
''')
                
                usuario = input('Usuario: ')
                clave = input('Clave: ')
                                
                if intentos == 0:
                    print('No le quedan más intentos.\nCuenta bloqueada.')
                    break
                
                intentos -= 1
            
            else:
                
                print('\nAcceso concedido.\n')

                while True:
                    menu = input('''1. Ver estado de inscripción.
2. Cambiar clave
3. Mensaje
4. Salir
\n''')
                    while not menu.isdigit():
                        menu = input('No es válido. Debe ingresar un numero entre el 1 y el 4: ')

                    menu = int(menu)
                    
                    if menu == 1:
                        print('Inscripto.\n')
                    
                    elif menu == 2:
                        clave_nueva = input('Ingrese una nueva clave: ')
                        confirmacion = input('Confirme la nueva clave: ')

                        if len(clave_nueva) < 6:
                            print('Error, la nueva clave tiene que tener al menos 6 caracteres.')
                        elif clave_nueva != confirmacion:
                            print('La nueva clave y la confirmación no se corresponden.')
                        else:
                            print('Cambio de clave exitosa.')
                            clave = clave_nueva
                    
                    elif menu == 3:
                        print('No hay mayor consuelo que pensar que el universo no tiene sentido.\n')

                    elif menu == 4:
                        break

                    else:
                        print('Error: opción fuera de rango.\n')


#ejercicio 3: “Agenda de Turnos con Nombres (sin listas)”

        case '3':

            lunes1 = ''
            lunes2 = ''
            lunes3 = ''
            lunes4 = ''
            martes1 = ''
            martes2 = ''
            martes3 = ''
            


            nombre = input('Indique su nombre: ').capitalize()

            while not nombre.isalpha():
                nombre = input('''No utilice números en su nombre.
Indique su nombre nuevamente: ''').capitalize()

            while True:
                menu = input('''1. Reservar turno
2. Cancelar turno (por nombre)
3. Ver agenda del día
4. Ver resumen general
5. Cerrar sistema
\n''')
                while not menu.isdigit():
                        menu = input('No es válido. Debe ingresar un numero entre el 1 y el 5: ')

                menu =int(menu)

                if menu == 1:
                    dia = input('''Escoje el día.
1. Lunes
2. Martes
\n''')
                    while not dia.isdigit():
                        dia = input('No es válido. Debe ingresar el 1 (Lunes) o el 2 (Martes): ')
                    
                    dia = int(dia)

                    nombre_paciente = input('Indique el nombre del paciente:\n').capitalize()

                    while not nombre_paciente.isalpha():
                        nombre_paciente = input('Solo ingrese el nombre, sin números:\n').capitalize()
                    
                    if dia == 1:
                        if nombre_paciente == lunes1 or nombre_paciente == lunes2 or nombre_paciente == lunes3 or nombre_paciente == lunes4:
                            print(f'El paciente {nombre_paciente} ya tiene turno para ese día.')
                        else:
                            if lunes1 == '':
                                lunes1 = nombre_paciente
                                print(f'{lunes1} tiene turno el día lunes.')
                            elif lunes2 == '':
                                lunes2 = nombre_paciente
                                print(f'{lunes2} tiene turno el día lunes.')
                            elif lunes3 == '':
                                lunes3 = nombre_paciente
                                print(f'{lunes3} tiene turno el día lunes.')
                            elif lunes4 == '':
                                lunes4 = nombre_paciente
                                print(f'{lunes4} tiene turno el día lunes.')
                            else:
                                print('No hay turnos disponibles para el día Lunes.')
                    elif dia == 2:
                        if nombre_paciente == martes1 or nombre_paciente == martes2 or nombre_paciente == martes3:
                            print(f'El paciente {nombre_paciente} ya tiene turno para ese día.')
                        else:
                            if martes1 == '':
                                martes1 = nombre_paciente
                                print(f'{martes1} tiene turno el día Martes.')
                            elif martes2 == '':
                                martes2 = nombre_paciente
                                print(f'{martes2} tiene turno el día Martes.')
                            elif martes3 == '':
                                martes3 = nombre_paciente
                                print(f'{martes3} tiene turno el día Martes.')
                            else:
                                print('No hay turnos disponibles para el día Martes.')
                           

                if menu == 2:

                    dia_cancelar = input('''Elija el día.
1.Lunes
2.Martes
\n''')    
                    while not dia_cancelar.isdigit():
                        dia_cancelar = input('Ingrese el 1 (Lunes) o el 2 (Martes): ')
                    
                    dia_cancelar = int(dia_cancelar)

                    if dia_cancelar == 1:
                        nombre_cancelado = input('Indique el nombre del paciente: ').capitalize()

                        while not nombre_cancelado.isalpha:
                            nombre_cancelado = input('Solo ingrese el nombre, sin números:\n').capitalize()
                        
                        if lunes1 == nombre_cancelado:
                            lunes1 = ''
                            print('Turno cancelado.')
                        elif  lunes2 == nombre_cancelado:
                            lunes2 = ''
                            print('Turno cancelado.')
                        elif  lunes3 == nombre_cancelado:
                            lunes3 = ''
                            print('Turno cancelado.')
                        elif  lunes4 == nombre_cancelado:
                            lunes4 = ''
                            print('Turno cancelado.')
                        else:
                            print('Ese paciente no tiene turno ese día.')
                        
                    elif  dia_cancelar == 2:
                        nombre_cancelado = input('Indique el nombre del paciente: ').capitalize()

                        while not nombre_cancelado.isalpha:
                            nombre_cancelado = input('Solo ingrese el nombre, sin números:\n').capitalize()

                        if martes1 == nombre_cancelado:
                            martes1 = ''
                            print('Turno cancelado.')
                        elif  martes2 == nombre_cancelado:
                            martes2 = ''
                            print('Turno cancelado.')
                        elif  martes3 == nombre_cancelado:
                            martes3 = ''
                            print('Turno cancelado.')
                        else:
                            print('Ese paciente no tiene turno ese día.')
                        

                if menu == 3:

                    selec = input('''Seleccione que día quiere ver:
1.Lunes
2.Martes
\n''')
                    
                    while not selec.isdigit():
                        selec = input('No es válido. Debe ingresar el 1 (Lunes) o el 2 (Martes): ')
                    
                    selec = int(selec)

                    if selec == 1:
                        if lunes1 == '':
                            print('Turno 1: Libre')
                        else:
                            print(f'Turno 1: {lunes1}')

                        if lunes2 == '':
                            print('Turno 2: Libre')
                        else:
                            print(f'Turno 2: {lunes2}')

                        if lunes3 == '':
                            print('Turno 3: Libre')
                        else:
                            print(f'Turno 3: {lunes3}')

                        if lunes4 == '':
                            print('Turno 4: Libre')
                        else:
                            print(f'Turno 4: {lunes4}')
                    
                    if selec == 2:
                        if martes1 == '':
                            print('Turno 1: Libre')
                        else:
                            print(f'Turno 1: {martes1}')

                        if martes2 == '':
                            print('Turno 2: Libre')
                        else:
                            print(f'Turno 2: {martes2}')

                        if martes3 == '':
                            print('Turno 3: Libre')
                        else:
                            print(f'Turno 3: {martes3}')
                         
                if menu == 4:    

                    ocupados_lunes = 0
                    
                    if lunes1 != '':
                        ocupados_lunes += 1
                    if lunes2 != '':
                        ocupados_lunes += 1
                    if lunes3 != '':
                        ocupados_lunes += 1
                    if lunes4 != '':
                        ocupados_lunes += 1

                    libres_lunes = 4 - ocupados_lunes
                    

                    ocupados_martes = 0
                    if martes1 != '':
                        ocupados_martes += 1
                    if martes2 != '':
                        ocupados_martes += 1
                    if martes3 != '':
                        ocupados_martes += 1

                    libres_martes = 3 - ocupados_martes

                    
                    print("\nRESUMEN GENERAL.")
                    print(f"Lunes ocupados: {ocupados_lunes}Lunes libres: {libres_lunes}")
                    print(f"Martes ocupados: {ocupados_martes} Martes libres: {libres_martes}")

                   
                    if ocupados_lunes > ocupados_martes:
                        print("Día con más turnos: Lunes")
                    elif ocupados_martes > ocupados_lunes:
                        print("Día con más turnos: Martes")
                    else:
                        print("Hay empate en cantidad de turnos")
                
                if menu == 5:
                    break            
                        
#Ejercicio 4 — “Escape Room: La Bóveda”
        
        case '4':

            energia = 100
            tiempo = 12
            cerraduras_abiertas = 0
            alarma = False
            codigo_parcial = ""
            spam = 0
            nombre = input('¿Cómo te llamas, agente?\n')

            while not nombre.isalpha:
                nombre = input('''Tu nombre no puede tener otros caracteres que no sean letras.
Intentalo nuevamente:\n''')

            while True:
 
                if spam == 3:
                    alarma = True
                    print('''Ya es el tercer intento en forzar la cerradura. 
La alarma se activo.''')

                if cerraduras_abiertas == 3:
                    print('Felicitaciones, usted ha abierto la boveda.')
                    break

                if alarma == True and tiempo <=3 and cerraduras_abiertas < 3:
                    print(f'La alarma está sonando y su tiempo es {tiempo}, muy poco. Usted ha perdido.')
                    break
                
                if tiempo == 0:
                    print('Se quedó sin tiempo.')
                    break
                if energia <= 0:
                    print('Su energía está agotada. Usted pierde.')
                    break
                
                menu = input('''Elija su acción (utilice los números)
1. Forzar cerradura
2. Hackear panel
3. Descansar\n''')
                while not menu.isdigit():
                    menu = input('Error. Debe ingresar un número del 1 al 3: ')
                
                menu = int(menu)
  
                if menu == 1:
      
                    if energia > 20 and tiempo > 2:
                        selec = input('''Usted a seleccionado "Forzar cerradura".
Esta acción le costará -20 energía y -2 tiempo. 
¿Desea realizarla? (S/N): ''').lower()
     
                        if selec == 's':
                            
                            spam += 1
               
                            if spam < 3:
                                if energia < 40:
                                    import random
                                    alarm = input('''Su energía está muy baja.
¡Hay riesgo de alarma!
Elige un número entre el 1 y el 3: ''')
                                
                                    while not alarm.isdigit():
                                        alarm = input('Error, debe ingresar un número entre el 1 y el 3: ')
                                    
                                    alarm = int(alarm)
                                    
                                    if alarm == random.randint(1,3): #Selección azarosa, para que el participante no prediga que pueda pasar
                                    
                                        alarma = True

                                        print('La alarma está sonando.')

                                    elif alarm < 1 or alarm > 3:
                                        print('No es una entrada válida. Debe elegir entre el 1 y el 3.')
                                    else:
                                        print('Ha abierto una cerradura.')
                                        cerraduras_abiertas += 1
                                        energia -= 20
                                        tiempo -= 2
                                
                                else:
                                    print('Cerradura forzada con exito.')
                                    cerraduras_abiertas += 1
                                    energia -= 20
                                    tiempo -= 2    
                           
                    elif tiempo < 2:
                        print('No tiene el tiempo esta acción.')
                    else:
                        print('No tiene energía suficiente para esta acción')            
     
                elif menu == 2:
                    
                    if energia < 10 or tiempo < 3:
                        print('No tiene los recursos suficientes para esta acción.')
                        print(f'Su energía actual es {energia}. El tiempo restante es {tiempo}')
                    
                    select = input('''Usted ha elegido "Hackear panel". 
Esta acción le consumirá -10 energíay -3 tiempo
Desea continuar? S/N: ''').lower() 

                    if select == 's':
                        
                        import time
                        
                        for i in range(1,5):
                            codigo_parcial += 'A'
                            print(f'Hackeando...paso {i}')
                            print(codigo_parcial)
                            time.sleep(2)  
                        
                        if len(codigo_parcial) == 8:
                            cerraduras_abiertas +=1
                            print('Bien hecho. Has abierto una cerradura.')
                        
                        energia -= 10
                        tiempo -= 3
                        
                elif menu == 3:
                    if alarma == True:
                        print('No puede descansar mientras suena la alarma. Esto le costara 10 de energía')
                        energia -= 10
                    elif energia == 100:
                        print('Su energía está completa, no puede descansar. Siga trabajando.')
                    if tiempo < 1:
                        print('No tiene tiempo suficiente para descansar.')
                    else:
                        descanso = input('''Usted seleccionó "descansar". 
Se le agregará 15 de energía, pero le cotara 1 de tiempo.
¿está seguro de esta acción? S/N: ''').lower()

                        if descanso == 's':
                            energia += 15
                            tiempo -=1
                            print(f'Su energía actual es {energia}. El tiempo restante es {tiempo}')


#ejercicio 5: “Escape Room:"La Arena del Gladiador" 

        case '5':

            nombre_gladiador = input('¿Cuál es su nombre gladiador?\n').strip()

            import random

            while True:
                
                if not nombre_gladiador.isalpha():
                    print('Ese no es un nombre para un gladiador, solo se aceptan letras.')
                    
                    nombre_gladiador = input('Dime otra vez su nombre, gladiador.\n')    
                    continue
                else:
                    
                    vida_gladiador = 100 
                    vida_enemigo =  100 
                    pociones_vida = 3 
                    danio_base = 15
                    turno_gladiador = True 
                    

                    while 0 < vida_gladiador and 0 < vida_enemigo:

                        if turno_gladiador == True:
                            print('Es tu turno de actuar.')
                            
                            print(f'Tu nivel de vida actual es {vida_gladiador} puntos.')
                            print(f'El nivel de vida de tu enemigo es de {vida_enemigo} puntos.')
                            
                            opcion = input('''Elije una de las opciones:
1. Ataque Pesado
2. Ráfaga Veloz
3. Curar\n''')

                            if not opcion.isdigit():
                                print('No es una opción válida. Debes elegir un número.')
                                
                                opcion = input('''Elije una de las opciones:
1. Ataque Pesado
2. Ráfaga Veloz
3. Curar\n''')
                            
                            else:
                                match opcion:
                                        
                                        case '1':
                                            print('Has hecho un "ataque pesado".')
                                            if vida_enemigo <= 20:
                                                vida_enemigo -= (danio_base * 1.5)
                                            else:
                                                vida_enemigo -= danio_base
                                            
                                            print(f'El nivel de vida de tu enemigo bajó a {vida_enemigo} puntos.')
                                            
                                        case '2':
                                            print('Has atacado con una "Rafaga veloz".')
                                            for i in range(3):
                                                golpe = random.randint(0, 7)
                                                
                                                if golpe == 0:
                                                    print('Has fallado el golpe.')
                                                else:
                                                    print(f".Golpe conectado por {golpe} de daño")
                                                    vida_enemigo -= golpe
                                                    print(f'El nivel de vida de tu enemigo ahora es de {vida_enemigo}')
                                            
                                        case '3':
                                            print('Has decidido tomar una poción')
                                            if pociones_vida > 0:
                                                if vida_gladiador >= 100:
                                                    print('No puedes tomar una poción, tu vida está al máximo.')
                                                    
                                                elif vida_gladiador > 70:
                                                    vida_gladiador = 100
                                                    print(f'Tus puntos de vida ahora son {vida_gladiador}')
                                                else:
                                                    vida_gladiador += 30
                                                    print(f'Tus puntos de vida ahora son {vida_gladiador}')
                                            else:
                                                print('No te quedan pociones de vida.')
                                    
                                        case _:
                                            print('No es una opción válida')

                                turno_gladiador = False

                        else:

                            print('Ahora es el turno del contrincante')

                            for j in range(3):
                                golpe_enemigo = random.randint(0,5)

                                if golpe_enemigo == 0:
                                    print('El enemigo ha fallado el golpe.')
                                else:
                                    vida_gladiador -= golpe_enemigo
                                    print(f'El contrincante te ha hecho {golpe_enemigo} puntos de daño.')
                                    print(f'Tu vida ahora es de {vida_gladiador} puntos.')
                            
                            turno_gladiador = True

                    else:
                        if vida_gladiador > 0:
                            print(f"¡VICTORIA! {nombre_gladiador} has ganado la batalla.")
                        elif vida_gladiador <= 0:
                            print( "DERROTA. Has caído en combate.")

                        break

        case _:
            print('No es un valor correspondiente.')
            