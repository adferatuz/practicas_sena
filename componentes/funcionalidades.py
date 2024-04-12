#Importación de modulos
from componentes import tiempo_x_km;
from componentes import conversor_temperatura;
from componentes import calcular_promedio_nota;
from componentes import calcular_capital;
from componentes import numero_menor_igual;
from componentes import precios_dolares;
from componentes import tabla_multiplicar;
from componentes import calcular_hora;
from componentes import consumo_restaurante;
from componentes import calcular_el_producto_desde_1_hasta_n;

#Lista de funciones algoritmicas
lista_algoritmos = [
    tiempo_x_km.calcular_tiempo,precios_dolares.calcular_precios,calcular_capital.calcular_capital_interes,
    calcular_hora.calcular_hora,calcular_promedio_nota.promedio_notas,conversor_temperatura.conversor_temperatura,
    numero_menor_igual.numeros_a_ingresar,tabla_multiplicar.tabla_multiplicar,calcular_el_producto_desde_1_hasta_n.calcular_el_producto_hasta_n,
    consumo_restaurante.cuenta_cobro
                     ]

#Diccionario Menú
menu = {
    'jugos' : {'Fresa' : 5000, 
                'Mora' : 5000, 
                'Maracuya' : 7000,
                'Lulo' : 4000, 
                'Guayaba' : 4000, 
                'Limonada' : 4000
            },
    'comidas rapidas' : {'Perro Caliente' : 10000, 
                            'Hamburguesa' : 10000, 
                            'Patacon Relleno' : 12000
                            },
    'postres':{'Tiramisu' : 7000, 
                'Tres Leches' : 6000, 
                'Arroz Con Leche' : 4000 }  
};

#Lista de opciones de  menú de algoritmos
menu_algoritmos = ['Tiempo por kilometro.',
                   'Conversión de dolares a pesos.',
                   'Calcular el capital a un tipo de interes.',
                   'Calcular la hora en el siguiente segundo.',
                   'Calcular la nota promedio.',
                   'Conversor de temperatura.',
                   'Numeros menores o iguales a 25.',
                   'Tabla de multiplicar de un numero digitado.',
                   'Calcular el factorial de un numero N.',
                   'Calcular el consumo de un cliente en un restaurante.'                   
                ];

# Funcion para elegir opciones de las bebidas.
def menu_pedidos(pedidos):
    opcion_elegida = {};

    for categoria, items in menu.items():
        for item, precio in items.items():
            if(pedidos ==item):
                opcion_elegida[item] = precio;
                return opcion_elegida;
            
    print(f'La opción {pedidos} no se encuentra en el menú');

#categorias del menú de pedidos
def categoria_menu():
    
    print(f'\n***********MENÚ************\n\n',
            '********CATEGORIA********\n')
    
    #Ciclo para Mostrar las categorias del menú.
    i = 0;
    for categoria, items in menu.items():
        i +=1;
        print(f'👌 ===> {i}). Menú de {categoria}:\n');

#lista de items de cada categoria del menú pedidos
def items_categoria_menu(opcion):
    
    #Mostrar la categoria del menú elegido.
    j = 0;
    for categoria, items in menu.items():
        #Menú de jugos.
        if(opcion == 1 and j == 0):
            print(f'\n****MENÚ DE {categoria.upper()}****\n')
            for item, precio in items.items():
                print(f'  ===> {item}: {precio}')
            
            
        #Menú de Comidas rapidas.
        elif(opcion == 2 and j == 1):
            print(f'\n****MENÚ DE {categoria.upper()}****\n')
            for item, precio in items.items():
                print(f' - {item}: {precio}')
            

        #Menú de postres.
        elif(opcion == 3 and j == 2):
            print(f'\n****MENÚ DE {categoria.upper()}****\n')
            for item, precio in items.items():
                print(f' - {item}: {precio}')
            
            
        elif(opcion > 3):
            print('La opcion digitada no esta en la lista de la categoria; por favor digita nuevamente la opcion a elegir. ');
                        
        j+=1
        
        


#funcion para elegir las opciones del menú algoritmos
def menu_opciones():
    opcion = 0;

    print('\n😎😎😎😎 Menú de algoritmos disponibles 😎😎😎😎\n')

    for i in range(10):
        print(f'{i + 1}). {menu_algoritmos[i].upper()} ')
    return;



