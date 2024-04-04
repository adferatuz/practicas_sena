# 1. Un corredor de maratón (distancia 42,195 Km) ha recorrido la carrera en 2 horas 25 minutos. Se desea un
# algoritmo que calcule el tiempo medio en minutos por kilómetro.

#funcion para calcular el tiempo
def calcular_tiempo():
    while True:
        try:
            opcion = input('Si desea hacer calculos con valores ingresados por teclado digite "S", de lo contrario digite "N": ').upper()
            if(opcion == 'S'):
                distancia = float(input('Digite la distancia que se ah recorrido: '))
                tiempo_final = float(input('Digite el tiempo en horas que se ah tardado en recorrer esa distancia: '))
                tiempo_en_minutos = tiempo_final * 60
                tiempo_medio = (tiempo_en_minutos / distancia)
                minutos = int(tiempo_medio)
                segundos = int((tiempo_medio - minutos) *60)
                print(f'El tiempo medio por kilometro recorrido es de {minutos} minutos y {segundos} segundos')
                break;
            elif (opcion == 'N'):
                distancia = 42.195
                tiempo_final = 2.4167
                tiempo_en_minutos = tiempo_final * 60
                tiempo_medio = (tiempo_en_minutos / distancia)
                minutos = int(tiempo_medio)
                segundos = int((tiempo_medio - minutos) *60)
                print(f'El tiempo medio por kilometro recorrido es de {minutos} minutos y {segundos} segundos')
                break            
            else:
                raise ValueError('Opcion no válida. Por favor ingresa "S" o "N"')
        except ValueError:
            print('Error: Has digitado una opcion invalida.')