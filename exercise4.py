

#ejemplo de entrada =     3  1  3  5
#Ejemplo de salida =    1  4  16

numVeces = int(input("¿Ingrese la cantidad de numeros que desea comprobar? "))
while numVeces>0 :
    num = int(input("Ingres3 un numero mayor o cero: "))
    if num>0 :
        opcion1 = (num*num) + num + 2
        opcion1 = int(opcion1/2)
        print("Total de regiones: " + str(opcion1))
    else:
        print("No ingrese numeros menor o igual a 0!")
    numVeces -= 1    
