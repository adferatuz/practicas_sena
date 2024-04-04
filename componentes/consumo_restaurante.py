# 7. Hacer un programa que registre el consumo realizado por los clientes de un restaurante, si el consumo de
# cada cliente excede 50000 se hará un descuento del 20%. Se debe mostrar el pago de cada cliente y el total
# de todos los pagos.

from funcionalidades import menu, menu_pedidos;

def cuenta_cobro():
    while True:
        try:            

            #Declaracion de variables
            lista_clientes = {};
            pedido_x_cliente= {};
            descuento = 0.20;
            pago_x_cliente = 0;
            cantidad_clientes = int(input('Cuantos clientes van a hacer pedido?: '));
            contador = 1;

            #Ciclo para hacer pedidos
            while (contador <= cantidad_clientes):
                print(f'\nCliente numero {contador}: \n')
                print(f'\n***********MENÚ************\n\n',
                      '********CATEGORIA********\n')
                
                #Ciclo para Mostrar las categorias del menú.
                i = 0;
                for categoria, items in menu.items():
                    i +=1;
                    print(f'👌 ===> {i}). Menú de {categoria}:\n');
                
                #Manejo de errores para elegir la opcion del menú
                while True:
                    try:

                        opcion = int(input('\nQue categoria del menú desea elegir; La opcion (1), (2) o (3): '))

                        #Mostrar la categoria del menú elegido.
                        j = 0;
                        for categoria, items in menu.items():
                            #Menú de jugos.
                            if(opcion == 1 and j == 0):
                                print(f'\n****MENÚ DE {categoria.upper()}****\n')
                                for item, precio in items.items():
                                    print(f'  ===> {item}: {precio}')
                                
                            #Menú de Comidas rapidas.
                            if(opcion == 2 and j == 1):
                                print(f'\n****MENÚ DE {categoria.upper()}****\n')
                                for item, precio in items.items():
                                    print(f' - {item}: {precio}')

                            #Menú de postres.
                            if(opcion == 3 and j == 2):
                                print(f'\n****MENÚ DE {categoria.upper()}****\n')
                                for item, precio in items.items():
                                    print(f' - {item}: {precio}')

                            j+=1
                        
                        opcion = str(input('\nDigite el nombre del producto a elegir: ')).title();
                    
                        pedido_x_cliente = menu_pedidos(opcion);
                        print(pedido_x_cliente)


                    except ValueError as error:
                        print(f'\n{error}\nEl valor ingresado es incorrecto.')

                contador +=1
            break;
                

        except ValueError as e:
            print(f'\n{e}\nEl valor ingresado no es correcto.')
    return;

cuenta_cobro();