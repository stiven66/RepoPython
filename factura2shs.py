Nproducto = []
Preciounitario= []
precioFinal=0
descuento=0
pfdescuento=0
Ncliente=input("Ingrese el nombre del cliente: ")
while True:
    try:
        CantidadProductos = int(input("Ingrese la cantidad de productos: "))
        if CantidadProductos > 0:
            break  # Si el número es mayor a 0, sale del ciclo
        else:
            print("ERROR: La cantidad debe ser mayor a 0. Intenta de nuevo.")
    except ValueError:
        print("ERROR: Debes ingresar un número válido. Intenta de nuevo.")

for i in range(CantidadProductos):
          while True:
             try:
                dato=input("Ingrese nombre del producto: ")
                if dato.isalpha():
                      Nproducto.append(dato)
                      break
                else:
                     print("¡Error! Por favor, ingrese solo texto.")
             except ValueError:
                   print("ERROR: Digite un texto")    
   
          while True:
                try:
                      datodos=input("Ingrese el precio del producto: ")
                      if datodos.isnumeric():
                            Preciounitario.append(float(datodos))
                            break
                      else:
                            print("¡Error! Por favor, ingrese el precio.")
                except ValueError:
                   print("ERROR: Digite un precio, no un texto")
                            
          precioFinal = precioFinal + Preciounitario[i]

print(f"Esta es la factura para el cliente: {Ncliente}")

for i in range(CantidadProductos):
      print(f"-{Nproducto[i]}:    ${Preciounitario[i]}")


print(f"El precio total de sus productos comprados es ${precioFinal}")

if CantidadProductos >= 3:
            descuento = precioFinal * (30/100)
            print("Su descuento es del 30%  por comprar 3 o mas productos en nuestra tienda.")
            print(f"Te ahorraste en esta compra ${descuento}")
            pfdescuento = precioFinal - descuento
            print(f"Total a pagar: ${pfdescuento}")
else:
                print("Total a pagar: $" , precioFinal)
    






# Preciounitario=int(input("ingrese el precio del producto: 

# porcentajedescuento=float(0.30)