'''8. Diseñar un algoritmo que permita ingresar la hora, minutos y segundos, y que calcule la hora en el siguiente
    segundo ("0<= H <=23", "0<= M <=59" "0<= S<=59").'''

# LLamar a las librerias que se va a usar 
from datetime import datetime,timedelta

#Validación de los datos ingresados en esete caso hora 
def calcular_hora():
    #Bucle para solicitar al usuario que ingrese la hora hasta que se proporcione una hora válida
    while True:
        # Intenta convertir la cadena de hora en un objeto datetime utilizando el formato especificado
        try: 
            hora = input('ingrese la hora en el formato (%H:%M:%S): ')
            tiempo = datetime.strptime(hora,'%H:%M:%S')
            print(f'Hora Valida: {tiempo.strftime("%H:%M:%S")}')      
            
            break
            
        except ValueError:
            print(f'Hora inválida. Por favor, introduce la hora en el formato correcto.')
    
    # Suma un segundo al objeto datetime utilizando el módulo timedelta
    suma = tiempo + timedelta(seconds=1)
    # Formatea el resultado de la suma para que solo muestre las partes de la hora, los minutos y los segundos
    resultado = suma.strftime('%H:%M:%S')
    print(f'La hora que ingreso, más un segundo es: {resultado}')

    opcion = input('Si desea ejecutar de nuevo el código presiona la tecla s: ').upper()
            
    while True:
        try:
            if opcion == 'S':
                calcular_hora()
                break
            else:
                break
        except ValueError:
            print(f'formato inválido. Por favor intrucle la opción otra vez: ')
calcular_hora()
    




    
