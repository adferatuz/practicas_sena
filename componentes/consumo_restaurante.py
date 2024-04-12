# 7. Hacer un programa que registre el consumo realizado por los clientes de un restaurante, si el consumo de
# cada cliente excede 50000 se hará un descuento del 20%. Se debe mostrar el pago de cada cliente y el total
# de todos los pagos.

from componentes import funcionalidades;

def cuenta_cobro():

    #Declaracion de variables
    lista_clientes = {};
    pedido_x_cliente= [];
    descuento = 0.20;
    pago_x_cliente = 0;

    while True:
        try: 

            cantidad_clientes = int(input('Cuantos clientes van a hacer pedido?: '));
            break;
        
        except ValueError as e:
            print(f'\n{e}\nEl valor ingresado no es correcto.')

    #Ciclo para hacer pedidos
    contador = 1;
    while (contador <= cantidad_clientes):

        print(f'\nCliente numero {contador}: \n');

        #imprimimos las categorias del menú de pedidos
        funcionalidades.categoria_menu();
        
        #Manejo de errores para elegir la opcion del menú
        while True:
            try:
                #elecion de la categoria del menú
                opcion_categoria = int(input('\nQue categoria del menú desea elegir; La opcion (1), (2) o (3): '))
                break;
            
            except ValueError as error:
                print(f'\n{error}\nEl valor ingresado es incorrecto.')

        #Funcion que muestra las categorias del menú 
        funcionalidades.items_categoria_menu(opcion_categoria);
        
        #opcion del producto a elegir
        opcion_item_categoria = str(input('\nDigite el nombre del producto a elegir: ')).title();

        #llamada a la funcion para elegir pedido
        pedido_x_cliente.append(funcionalidades.menu_pedidos(opcion_item_categoria));
        if(pedido_x_cliente == True):
            print(pedido_x_cliente );

        while True:
            try:

                #opcion para agregar mas consumo a la cuenta
                agregar_pedido = input("si deseas agregar algo mas al pedido digita la tecla 's' de lo contrario digita la tecla 'n'; cual es tu elección?: ").upper();
            
                if(agregar_pedido == 'S' ):

                    #imprimimos las categorias del menú de pedidos
                    funcionalidades.categoria_menu();

                    #Manejo de errores para elegir la opcion del menú
                    while True:
                        try:

                            #elecion de la categoria del menú
                            opcion_categoria = int(input('\nQue categoria del menú desea elegir; La opcion (1), (2) o (3): '))
                            break;
                        
                        except ValueError as error:
                            print(f'\n{error}\nEl valor ingresado es incorrecto.')
                    
                    #Funcion que muestra las categorias del menú 
                    funcionalidades.items_categoria_menu(opcion_categoria);

                    #opcion del producto a elegir
                    opcion_item_categoria = str(input('\nDigite el nombre del producto a elegir: ')).title();

                    #llamada a la funcion para elegir pedido
                    pedido_x_cliente.append(funcionalidades.menu_pedidos(opcion_item_categoria));
                    print(pedido_x_cliente);

                elif(agregar_pedido == 'N'):
                    cliente = f'Cliente # {str(contador)}';

                    #Agregar pedido total al cliente
                    lista_clientes[cliente] = pedido_x_cliente;
                    print(f'\nRegistro del consumo de clientes =   {lista_clientes}\n');
                    pedido_x_cliente = [];
                    break;
                
                else:
                    print('el caracter digitado es incorrecto; por favor escriba nuevamente que opción desea realizar.')


            except ValueError as e:
                print(f'{e}\n El valor ingresado es incorrecto.')
            
        contador +=1
              
    return;

