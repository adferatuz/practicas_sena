'''Realizar un algoritmo que muestre por pantalla la tabla de multiplicar decreciente de cualquier número,
    ingresado entre el 1 y el 10.'''
def tabla_multiplicar():
    while True:
        # Se inicia un bucle while que se ejecutará indefinidamente hasta que se ingrese un número válido.
        try: 
            # Se intenta convertir la entrada del usuario a un valor válido
            numero = float(input('Ingrese el número que quiere multiplicar: '))
            for i in range(10):
                # Se recorre un bucle for desde 0 hasta 10
                multiplicacion = numero*(10 - i)
                print(f'{numero} x {10 - i} = {multiplicacion:.1f}')
            
            opcion = input('Si desea ejecutar de nuevo el código presiona la tecla s: ').upper()
            
            while True:
                try:
                    if opcion == 'S':
                        tabla_multiplicar()
                        break
                    else:
                        print('Gracias por usar el programa. ')
                        break
                except ValueError:
                    print(f'formato inválido. Por favor intrucle la opción otra vez: ')
            
            break
            # Se sale del bucle while después de imprimir los números correctamente.  
        except ValueError:
            # Se maneja la excepción si el usuario ingresa un valor no válido
            print (f'Dato inválido. Por favor, introduce un número en el formato correcto.')
            # Se continúa con la iteración del bucle while si se captura una excepción.
tabla_multiplicar()
    