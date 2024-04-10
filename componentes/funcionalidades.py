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

lista_algoritmos = [
    tiempo_x_km,precios_dolares,calcular_capital,
    calcular_hora,calcular_promedio_nota,conversor_temperatura,
    numero_menor_igual,tabla_multiplicar,calcular_el_producto_desde_1_hasta_n,
    consumo_restaurante
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

menu_algoritmos = ['Tiempo por kilometro',
                   'Conversión de dolares a pesos',
                   'Calcular el capital a un tipo de interes',
                   'Calcular la hora en el siguiente segundo',
                   'Calcular la nota promedio',
                   'Conversor de temperatura',
                   'Numeros menores o iguales a 25',
                   'Tabla de multiplicar de un numero digitado',
                   'Calcular el factorial de un numero N',
                   'Calcular el consumo de un cliente en un restaurante'                   
                ];

# Funcion para elegir opciones de las bebidas.
def menu_pedidos(pedidos):
    opcion_elegida = {};

    for categoria, items in menu.items():
        for item, precio in items.items():
            if(pedidos ==item):
                opcion_elegida[item] = precio;
                return opcion_elegida;
            
    print(f'La opción {pedidos} no se encuentra en el menú')

#funcion para elegir las opciones del menú algoritmos
def menu_opciones():
    opcion = 0;

    print('\n😎😎😎😎 Menú de algoritmos disponibles 😎😎😎😎\n')

    for i in range(10):
        print(f'{i + 1}). {menu_algoritmos[i]} ')
    return;

