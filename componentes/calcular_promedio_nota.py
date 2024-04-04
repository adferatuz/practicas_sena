# 3. Escribir el algoritmo que permite calcular la nota correspondiente al primer parcial de “análisis” para un
# estudiante cualquiera. Se debe considerar que hay dos talleres y un quiz, que en conjunto valen un 30% de
# la nota y el resto (70%) corresponde a la nota del examen parcial.

def promedio_notas ():
    while True:
        try:
            nota_taller_1 = float(input('Digite la nota del primer taller: '))
            nota_taller_2 = float(input('Digite la nota del segundo taller: '))
            nota_quiz = float(input('Digite la nota del quiz: '))
            nota_examen_parcial = float(input('Digite la nota del examen parcial: '))

            procentaje_talleres_quiz = 0.30
            porcentaje_examen_parcial = 0.70

            contribucion_talleres_quiz = (nota_taller_1 + nota_taller_2 +nota_quiz) * procentaje_talleres_quiz
            contribucion_examen_parcial = (nota_examen_parcial * porcentaje_examen_parcial)

            promedio_nota = contribucion_talleres_quiz + contribucion_examen_parcial

            print(f'La nota correspondiente al primer parcial de analisis es de {promedio_nota:.2f}')
            break;

        except ValueError as e:
            print(e)
    
