#  2. Realizar la conversión de una temperatura dada en grados Centígrados a grados Fahrenheit 
# (Fórmula: F = (9/5) C + 32).

def conversor_temperatura():
    while True:
        try:
            opcion = input('Si desea digitar los valores por teclado digite la tecla "S", de lo contrario digite la tecla "N"').upper();
        
            if(opcion == "S"):
                grados_celsius = float(input('Por favor digite los grados celsius a convertir: '));
                grados_fahrenheit = (9/5) * grados_celsius + 32;
                print(f'los {grados_celsius} grados centigrados son equivalentes a {grados_fahrenheit:.2f} grados fahrenheit');
                break;
            elif(opcion =='N'):
                print('Gracias por participar del programa.')
                break;
            else:
                raise ValueError('Opcion no válida. Por favor ingresa "S" o "N":  ')
            
        except ValueError as e:
            print(e);
