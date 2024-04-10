from componentes import funcionalidades;

while True:
    try:
        print('Bienvenido al taller aplicando funciones y procedimientos en la solución de algoritmos.\n');

        opcion = input('\nSi deseas acceder al menú de opciones de los diferentes algoritmos, digita la tecla "s", de lo contrario digita la tecla "n": ').upper();
        break;

    except ValueError as e:
        print(f"{e}\n El valor ingresado es incorrecto.")

if(opcion == "S"):
    funcionalidades.menu_opciones();

    while True:
        try:
            opcion2 = int(input('\nDigita la opcion que deseas ejecutar: '));
            if(opcion2 >= 1 and opcion2 < 11):
                break;        
            else:
                print('\nEl numero no se encuentra en la lista de algoritmos disponibles.\n',
                      )

        except ValueError as e:
            print(f"{e}\n El valor ingresado es incorrecto.")

    for i in range(len(funcionalidades.lista_algoritmos)):       
        if(opcion2 == (i+1)):
            print('si entro y voy bien')
            break    
else:
    print("\nHasta la proxima!!")
