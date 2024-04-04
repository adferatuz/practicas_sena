#  4. Un capital C está situado a un tipo de interés R anual ¿al término de cuántos años se doblará?
import math


def calcular_capital_interes():
    while True:
        try:
            capital_inicial = float(input('Ingrese por favor el valor del capital inicial: '));
            interes_anual = float(input('Ingrese por favor el porcentaje de la tasa de interes anual: '));
        
            capital_final = capital_inicial * 2;
            tasa_interes_compuesto = interes_anual / 100;
        
            tiempo = math.log(2) / math.log(1 + tasa_interes_compuesto);
            tiempo_en_años = int(tiempo);
            tiempo_en_meses = int((tiempo - tiempo_en_años) * 12);
        
            print(f'Para que el capital inicial llegue a ser el doble, el cual será de ${capital_final:.2f}, se llevará un tiempo estimado de {tiempo_en_años} años y {tiempo_en_meses} meses')
            break;
        
        except ValueError as e:
            print('\n',e, '\n \nHubo un error al ingresar los datos solicitados, por favor intentelo nuevamente.\n')

