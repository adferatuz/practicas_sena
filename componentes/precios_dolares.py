#6. Hacer un programa que sume 5 precios de camisas (en dólares) y que luego muestre el total de la venta en pesos.
    
def calcular_precios():

    while True:
        try:

            numero_prendas = (int(input('Digite el numero de prendas a evaluar: ')))
            lista_prendas_valor = {};
            tipo_prenda = '';
            precio_prenda = 0;
            valor_compra = 0;
            dolar_cop = 3857

            for i in range(numero_prendas):
                tipo_prenda = str(input('\nDigite por favor el nombre de la prenda: '))
                precio_prenda  = float(input(f'\nDigite por favor el precio de la prenda ({tipo_prenda}) en dólares: '));
                lista_prendas_valor[tipo_prenda] = precio_prenda;
                valor_compra += precio_prenda ;

            valor_compra = float(valor_compra * dolar_cop);
            print(f'\nEl precio total de la compra en pesos colombianos fue de: ${valor_compra:.2f} pesos.\n');
            break;
        
        except ValueError as e:
            print(f'\n{e} \nEl valor introducido es incorrecto. ')
