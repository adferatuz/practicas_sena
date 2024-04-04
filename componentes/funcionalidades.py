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

# Funcion para elegir opciones de las bebidas.
def menu_pedidos(pedidos):
    opcion_elegida = {};

    for categoria, items in menu.items():
        for item, precio in items.items():
            if(pedidos ==item):
                opcion_elegida[item] = precio;
                return opcion_elegida;
            
    print(f'La opción {pedidos} no se encuentra en el menú')

