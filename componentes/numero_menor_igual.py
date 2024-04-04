#5. Elaborar un algoritmo que permita ingresar 20 números y muestre todos los números menores e iguales a 25.
import random

def numeros_a_ingresar():
    while True:
        try:
            opcion = input('Si quieres digitar los valores a evaluar digita la tecla "S"; de lo contrario digita la tecla "N": ').upper();

            if(opcion == "S"):
                lista_numeros = [];
                j = 0
                while len(lista_numeros) < 20:
                    j += 1;
                    numero_ingresado = int(input(f'Digita el numero en la posicion {j} de la lista: '));
                    if numero_ingresado in lista_numeros:
                        print(f' el numero {numero_ingresado} en la posicion {j} ya esta en la lista. \n')
                        numero_ingresado = int(input(f'Por favor digita nuevamente el numero en la posicion {j} de la lista: '));
                        lista_numeros.append(numero_ingresado);
                        print(lista_numeros);
                    else:
                        lista_numeros.append(numero_ingresado);
                        print(lista_numeros);
                break

            elif(opcion == 'N'):
                lista_numeros_generados = [];
                lista_numeros_menores_25= [];

                while len(lista_numeros_generados) < 20:
                    numero_aleatorio = random.randint(0, 100);
                    if numero_aleatorio not in lista_numeros_generados:
                        lista_numeros_generados.append(numero_aleatorio);
                 
                for i in range(len(lista_numeros_generados)):                    
                    if(lista_numeros_generados[i] <= 25):
                            lista_numeros_menores_25.append(lista_numeros_generados[i]);
                    else:
                        lista_numeros_menores_25.append(None);

                lista_numeros_menores_25 = [x for x in lista_numeros_menores_25 if x is not None]
                
                print(f'\nLa lista de los numeros generados aleatoriamente es: {lista_numeros_generados}\n')                    
                print(f'Los numeros menores o iguales a 25 tomados de la anterior lista son:  {lista_numeros_menores_25}')
                break;
            
            else:
                raise ValueError('Opcion no válida. Por favor ingresa "S" o "N"')

        except ValueError as e:
            print(f'\n {e} \nEl valor ingresado es incorrecto')
    
    