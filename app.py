#imortacion del modulo funcionalidades
from componentes import funcionalidades;

#ciclo infinito con manejo de errores
while True:
    try:
        #mensaje de bienvenida a la aplicacion
        print('Bienvenido al taller aplicando funciones y procedimientos en la solución de algoritmos.\n');

        #variable para evaluar opcion
        opcion = input('\nSi deseas acceder al menú de opciones de los diferentes algoritmos, digita la tecla "s", de lo contrario al oprimir cualquier otra tecla saldra del programa: ').upper();
        break;

    except ValueError as e:
        print(f"{e}\n El valor ingresado es incorrecto.");

#Evaluacion de la variable opcion
if(opcion == "S"):

    #funcion para desplegar el menú de algoritmos
    funcionalidades.menu_opciones();
    
    #ciclo para manejar errores
    while True:
        try:
            #variable para evaluar la desicion del usuario
            opcion = int(input('\nDigita la opcion que deseas ejecutar: '));

            #se evalúa la condición de la variable opción
            if(opcion >= 1 and opcion < 11):

                #ciclo para recorrer la lista de algoritmos
                for i in range(len(funcionalidades.lista_algoritmos)):

                    #se evalúa la condición para elegir el algoritmo a usar       
                    if(opcion == (i+1)):

                        #imprimir or consola la eleccion del algoritmo a usar
                        print(f'\nla opcion que elegiste es:\n\n{i+1}). {funcionalidades.menu_algoritmos[i].upper()}\n');

                        #funcion donde se almacena la lista de algoritmos 
                        funcionalidades.lista_algoritmos[i](); 
                        break;                      
            else:

                #Imresión de un mensaje de error al ingresar un valor invalido
                print('\nEl numero no se encuentra en la lista de algoritmos disponibles.\n',
                    );
        
        #Manejo de excepción
        except ValueError as e:
            print(f"{e}\n El valor ingresado es incorrecto."); 
        
        #Ciclo infinito con manejo de excepción
        while True:
            try:

                #Amacenamiento de la opción que el usuario elige
                opcion = input("\nSi desea hacer uso de alguna otra funcion del menú, digite la tecla ('s'); de lo contario digite la tecla ('n'): ").upper();
                break;

            #Manejo de excepción
            except ValueError as e:
                print(f"{e}\n El valor ingresado es incorrecto.");
        
        #Evaluamoa si la opción del usuario es continuar en el rograma
        if(opcion == 'S'):
            #Desplegamos nuevamente la lista de opciones del menú
            funcionalidades.menu_opciones();
            continue;

        #Terminamos el rograma en caso de que el usuario asi lo deseé
        else:
            print("\nGracias por usar el programa. Hasta la proxima\n")
            break;
   
else:
    #Fin del pprograma
    print("\nHasta la proxima!!");
