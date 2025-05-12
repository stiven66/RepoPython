print("""BIENVENIDO.
Gestiona tus notas y categoriza tus calificaciones.
1. -Puedes verificar si una nota la aprobaste o reprobaste.
2. -Puedes ingresar un listado de calificaciones separado por comas.
3. -Puedes ingresar un listado de calificaciones para saber tu promedio.
4. -Puedes ingresar una nota y verificar cuantas de tus notas son mayores a esta.
5. -En base a tu lista de notas, puedes ingresar otra calificacion para saber si tienes una nota igual y el programa te dice cuantas veces sacaste esa nota.

1.""")
while True:
    try:
        Calificacion_aprobada=input("Ingrese una calificacion(0 a 100) para saber si aprobaste: ")  #Ciclo mientras con un try para que me tire error en
        if Calificacion_aprobada.isnumeric():                                                     #consola cuando el usuario digite letras, numeros negativos
            if 0 <= int(Calificacion_aprobada) < 50:                                            #y mayores a 100 y se repita hasta que el usuario digite una nota
                print("Reprobo la nota. Estudia para la recuperacion!")                       #en un rango de 0 a 100 para determinar si esta de 50 a 100 aprueba
                break                                                                       #si no reprueba y si cumple algunas de las 2 condiciones hace un break
            elif int(Calificacion_aprobada) > 49 and int(Calificacion_aprobada) <= 100:    #y se sale del ciclo si no va ser infinito hasta que ingrese un numero de
                print("Aprobo la nota. Eres un excelente estudiante, las estas rompiendo!")#0 a 100.
                break
            elif int(Calificacion_aprobada) < 0:
                print("Su calificacion no esta en el rango adecuado.")                     #Recordemos que .isnumeric() valida caracter por caracter si toda
                continue                                                                   #la cadena de texto es numerico. Esta es una funcion.
            else:
                print("Su calificacion no esta en el rango adecuado.")
                continue
        else:
            print("Error! Digite un dato adecuado.")
    except ValueError:
        print("Error")
print("")
print("2.")
notasseparaporcoma=input("Ingrese nota por nota separandola con una coma sin espacio: ")#
listdenotasseparadoporcomas=notasseparaporcoma.split(",")
print(listdenotasseparadoporcomas)
print(" ")
print("3.")
NCal=int(input("Ingres el numero de calificaciones a gestionar: "))
Calificaciones=[]                                       
totalNotas=0                                         
for i in range (NCal):          #Ciclo for repite el bucle NCal: Porque si son 3 calificaciones llena la lista con tres datos en cada repeticion va llenando la posicion de mi lista calificaciones[] con su nota correspondiente.                         
    while True:         #El ciclo while lo integramos en el for para validar con el try except; hasta que no de el numero entre el rango de 0 a 100 se repite infinitamente.                                    
        try:                                           
            DatoCal=input("Ingresa tu calificacion.")
            if DatoCal.isnumeric():                     #Con la funcion isnumeric() valida si caracter por caracter de la variable DatoCal es numerico(solo verifica en cadenas de texto).
                DatoCal=float(DatoCal)              #Como verificamos una cadena de texto que sean numericos con .isnumeric() en esta linea lo convertimos en float para hacer la operacion relacional en la siguiente linea.          
                if 0 < DatoCal < 50:
                    Calificaciones.append(DatoCal)              #Como ya sabemos que en la variable DatoCal ay un numero de 0 a 49 ese dato se lo llevamos a la lista Calificaciones[]
                    print("Reprobo esta nota.")
                    break                       # Si se cumple esta condicion se sale del while y pasa a la segunda repeticion del bucle for para eso usamos el break.
                elif DatoCal >= 50 and DatoCal < 101:
                    Calificaciones.append(DatoCal)           #Para llenar la lista se debe aplicar la funcion .append()
                    print("Aprobo esta nota.")
                    break                   #Si no cumple la primera condicion pero cumple esta segunda condicion se sale con el break y continua el siguiente bucle del for
                else:
                    print("Nota incorrecta")
            else:
                print("Vuelve a digitar nota!") 
        except ValueError:           #Recordemos que el try nos devuelve al ciclo si no cumple las condiciones hasta que en una repeticion ingrese el dato adecuado que se requiere.
            print("Vuelve a ingresar una calificacion en el rango de 0 a 100.")
    totalNotas=totalNotas+Calificaciones[i]    #Cuando se mete el dato correcto por medio del while despues de verificar errores con el try except pasa hacer la suma y en la siguiente linea
    promedio=totalNotas/NCal                   #el promedio nota por nota a medida que se va haciendo el for y a medida que va ingresando nota por nota.
print(" ")  
print(totalNotas)
print(promedio)
print(Calificaciones)
print(" ")
print("4.")
while True:                 #Este ciclo con try except hace la misma funcion: evalua que este en un rango de 0 a 100 y que arroje error sin se ingresa letras numeros negativos o mayores a 100.
    try:
        NotaComparar=int(input(f"Ingrese una calificacion especifica para compararla con las {NCal} notas para decir cuantas son mayores a la ingresada:"))
        if 0 <= NotaComparar <= 100:
            break
        else:
            print("ERROR!")
    except ValueError:
        print("Debe ser de un rango de 0 a 100.")
cantidadnummayor=0          #Esta variable hace el papel de acomulador para contar cuantas notas son mayores a un valor especifico que se ingrese en la linea 70 NotaComparar
cont=0                  #Esta variable hace el papel de contador para ir recorriendo el ciclo hasta el numero de calificaciones en el siguiente ciclo while
while cont < NCal:
        if Calificaciones[cont] > NotaComparar:  #A medida que recorre el ciclo compara cada nota de la lista(Calificaciones[]) con NotaComparar
            print(f"La nota {cont} de la lista es mayor a {NotaComparar}.")
            cantidadnummayor=cantidadnummayor+1     #Si la primera nota de mi lista es mayor a la nota especifica a comparar se suma 0 = 0 + 1 es igual a 1 por que se cumplio la condicion.
            cont=cont+1         #Se hace el contador para pasar el siguiente bucle
            continue
        elif NotaComparar == Calificaciones[cont]:    #Si la nota de la lista es igual no se ejecuta el acomulador.
            cont=cont+1        #Recordar que se hace el contador si no se repite infinitamente.
            continue     #El continue es como el break pero no lo saca si no que continua el siguiente ciclo.
        else:
            cont=cont+1    #Si no cumple ninguna de las primeras condiciones igual se hace el acomulador y pasa a evaluar la segunda poscicion de mi lista y asi sucesivamente.
            continue

if cont == 0:
    print("La nota a comparar que acabo de ingresar es mayor a 100 o menor a 0 a su listado de calificaciones.")
elif cantidadnummayor > 0:
    print(f"Tenemos {cantidadnummayor} nota/s mayores a la nota ingresada({NotaComparar}).")
print(" ")
print("5.")
verifica=True   #Variable vuleano
contprecalificaciones=0         #Contador para saber cuantas veces aparece la misma nota que acabo de ingresar
PresenciaCal=int(input("Elegi una nota para identificar cuantas veces aparece en tu listado de calificaciones: "))
for i in range(NCal):
    if PresenciaCal == Calificaciones[i]:      #Si es igual la nota ingresada a la nota de la lista se cuenta con el contador en la siguiente linea.
        contprecalificaciones=contprecalificaciones+1
        continue
    elif PresenciaCal < 0 and PresenciaCal > 100:     #Si no esta en el rango de 0 a 100 se sale por que esta digitando mal la nota y el vuleano cambia a falso
        verifica=False
        break
    else:
        continue

if verifica == False:
    print("No se pudo identifacar ninguna nota ya que la nota no esta en el rango de 0 a 100 y es un error.")
else: 
    print(f"El numero de veces que aparece la calificacion {PresenciaCal} en tus notas son: {contprecalificaciones} veces.")
#En este ultimo if imprime que es un error, si no imprime cuantas veces aparece la misma nota ingresada por consola.