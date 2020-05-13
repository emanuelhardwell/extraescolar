
#ejemplo de entrada =     6  12  28  -1
#Ejemplo de salida =    6= 1+2+3    12 no es perfecto   28=1+2+4+7+14

numVeces = int(input("Ingrese la cantidad de numeros que desea comprobar? "))
esMalo = False
salida = " = 1"
while numVeces>0 :
    num = int(input("No ingrese numeros menor o igual a 0!"))
    if num==0 :
        print("No ingrese numeros menor o igual a 0!")
    elif num<0 :
        numVeces = 0
        print("Ciclo finalizado ... intentelo de nuevo!")    
    elif num>0 :
        numPerfecto = 0
        for i in range(1, num) :
            if (num%i == 0) :
                numPerfecto += i
                if i > 1 : salida += " + " + str(i)         
        if numPerfecto==num :
            print(str(num) + " Si es un numero perfecto!")
            print(str(num) + salida)
            
        else:
            print(str(num) + " No es un numero perfecto!")
    numVeces -= 1          
