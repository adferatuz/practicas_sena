#9. Dado N, escribir el producto desde 1 hasta N.
import math

def calcular_el_producto_hasta_n():
    while True:
        try:
            #definir las variables 
            N = int(input("ingresar el valor del numero factorial: "))
            
            producto = 1
            
            for i in range(N):
                producto = producto * (i+1)
                print (producto)
            
            opcion = input("Si deseas continuar digita la letra s").upper()

            while True:
                try:
                   if (opcion == "S"):
                       print("ingresa un numero nuevamente")
                       calcular_el_producto_hasta_n()
                       break; 
                   else: 
                       print("Gracias por usar el programa, regresa pronto")
                       break; 
                

                except ValueError as e:
                    print(f"error {e} el valor ingresado es incorrecto")
            break; 
                
                    
        

        except ValueError as e:
            print(f"error {e} el valor ingresado es incorrecto, intenta nuevamente")
                            



