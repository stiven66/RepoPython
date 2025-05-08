#numero1 = input("Ingrese numero a sumar: ")
#numero2 = input("Ingrese segundo numero a sumar: ")
#resultado = numero1 + numero2
#print(f"La suma de sus numeros ingresados equivale a: {resultado}")

# numero1 = input("Ingrese numero: ")

# if numero1 % 2 == 0:
   
#    print("El numero es par.")
# else:
#    print("El numero es impar.")

def resultadopromedio(nombre,nota1,nota2,nota3):
    promedio=(nota1+nota2+nota3)/3
    return nombre,promedio

Numestudiantes=int(input("Digite el numero de estudiantes al que les va promediar sus notas"))

for i in range(Numestudiantes):
   def informacionestudiante():
      nombre=input("Ingrese el nombre:")
      nota1=int(input("Ingrese la primera nota: "))
      nota2=int(input("Ingrese la segunda nota: "))
      nota3=int(input("Ingrese la tercera nota: "))
      return nombre,nota1,nota2,nota3
   datosestudiante=informacionestudiante()
   resulttado=resultadopromedio(datosestudiante[0],datosestudiante[1],datosestudiante[2],datosestudiante[3])

   if resulttado[1] >= 3:
      print(f"El estudiante {resulttado[0]} obtuvo un promedio de {resulttado[1]} y aprobo. Felicitaciones!")
   elif resulttado[1] < 3:
      print(f"El estudiante {resulttado[0]} obtuvo un promedio de {resulttado[1]} y reprobo.")
    