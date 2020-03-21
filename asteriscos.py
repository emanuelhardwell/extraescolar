


def triangle(x):
    for i in range (0,x,1):
        for j in range (0,i+1,1):
            print("*",end="")
        print("")
    print("\n")


    for i in range (x,0,-1):
        for j in range (0,i,1):
            print("*",end="")
        print("")
    print("\n")


    for i in range (0,x,1):
        for j in range (0,i+1,1):
            print("*",end="")
        print("")
    for i in range (x,0,-1):
        for j in range (0,i,1):
            print("*",end="")
        print("")
    print("\n")


    for i in range (1,x+1):
        for j in range (1,x+1):
            print("*",end="")
        print("")
    print("\n")

x= int (input("Adds a number: "))
triangle(x)


