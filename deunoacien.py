for i in range(1,101):
    if i % 3 == 0 and not i % 5 == 0:#En la primera y segunda vuelta del ciclo imprime el 1 y el 2 ya en la tercera vuelta cumple la condicional de que el numero
        print("Fizz")                #3 es divisible por 3 e imprime Fizz.
        
    elif i % 5 == 0 and  i % 3 == 0:
        print("FizzBuzz")
    
    elif i % 5 == 0 and not i % 3 == 0:
        print("Buzz")
        
    else:
        print(i)



