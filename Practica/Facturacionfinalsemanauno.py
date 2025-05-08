Nproducto = [] #Creamos lista para llenar el nombre de los productos.
Preciounitario= []#Lista para precios de cada producto.
precioFinal=0
descuento=0
pfdescuento=0
print("Bienvenido al sistema de facturacion; recuerde llenar los campos con los datos adecuados de lo contrario el sistema lanzara error!")
NameStore=input("Digite el nombre de la tienda: ")
Ncliente=input("Ingrese el nombre del cliente: ")
Email=input("Ingrese el correo del cliente: ")
Descuentoday = int(input("Ingrese el porcentaje para descuento el dia de hoy: "))
while True:                                                                  #Ciclo Mientras para verificar que cuando ingrese la cantidad de productos
    try:                                                                     #el dato sea numero con la funcion .isnumeric() que es la que verifica caracter por caracter,
        CantidadProductos = int(input("Ingrese la cantidad de productos: ")) #la variable cantidad la definimos como entero pero en la siguiente linea la convertimos en texto str
        if str(CantidadProductos).isnumeric() and CantidadProductos > 0:     #por que la funcion solo verifica en cadenas de texto. Si el dato no es
            break                                                            #numero lanza mensaje de error y vuelve y repite ciclo hasta que ingrese un valor mayor a 0
        else:                                                                #y dando el dato correcto se sale con el break.
            print("ERROR: La cantidad debe ser mayor a 0. Intenta de nuevo.")
    except ValueError:
        print("ERROR: Debes ingresar un número válido. Intenta de nuevo.")

for i in range(CantidadProductos):                                    #Ciclo for(para) para llenar las listas de productos y precios.
          while True:
             try:
                dato=input("Ingrese nombre del producto: ")    #Ciclo Mientras para que verifique que en la variable dato se almacene texo y no caracteres numericos con la
                if dato.isalpha():                             #funcion .isalpha(). Si cumple la condicion llenamos la lista Nproducto con lo que se almacena en dato llamando
                      Nproducto.append(dato)                  #la funcion .append() que es la que me llena la lista; Si la variable dato tiene solo un caracter numerico pasa
                      break                                    # a Valueerror y repite el ciclo hata que ingrese solo texto y haga el break.
                else:
                     print("¡Error! Por favor, ingrese solo texto.")
             except ValueError:
                   print("ERROR: Digite un texto")    
          while True:
                try:                                                     # Este ciclo es igual a la verificacion de cantidad de producto pero llenando la lista
                      datodos=input("Ingrese el precio del producto: ") #Preciounitario con la funcion append() llevandole lo que se almaceno en la variable datodos ingresado por consola.
                      if datodos.isnumeric() and int(datodos) > 0:    #NOTA: Las funciones que verifican numeros(.isnumeric()) o texto(.isalpha()) solo verifican si la variable es texto por eso en esta linea convertimos en int a datodos para poder al macenar el tipo de dato correcto en mi lista de precios.
                            Preciounitario.append(float(datodos))
                            break
                      else:
                            print("¡Error! Por favor, ingrese el precio.") #Si se ingresa texto muestra este mensaje y repite ciclo hasta darle numeros mayor a 0 y poder hacer el break.
                except ValueError:
                   print("ERROR: Digite un precio mayor a 0, no un texto.")
                            
          precioFinal = precioFinal + Preciounitario[i] #Se hace una variable de contador para ir sumando precio por precio cada vez que haga el ciclo for.
print(" ")
print(NameStore)
print()
print(f"Esta es la factura para el cliente: {Ncliente}")
print(" ")
for i in range(CantidadProductos):
      print(f"-{Nproducto[i]}:    ${Preciounitario[i]:.2f}") #Ciclo para imprimir cada producto ingresado con su respectivo precio.
      print("")
print(" ")
print(f"El precio total de sus productos comprados es de ${precioFinal:.2f}")
print(" ")
if 0 < Descuentoday < 100:     #Condicion para manejar el rango de descuento de 0 a 100 como lo pide el ejercicio; si por consola se ingresa un numero menor a 0 o mayor a 100, imprime el mensaje de que no hay descuento.
     descuento = precioFinal * (Descuentoday/100)
     pfdescuento = precioFinal - descuento
     print(f"Su descuento es del {Descuentoday}%.")
     print(f"Te ahorraste en esta compra ${descuento:.2f}")
     print(f"TOTAL A PAGAR: ${pfdescuento:.2f}")
else:
     print("No hay descuento el dia de hoy!")

print(f"Gracias por su compra {Ncliente}, le estaremos avisando de nuevos descuentos exclusivos a su correo {Email} premiando su fidelizacion con nosotros!")
