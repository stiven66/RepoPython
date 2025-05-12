library=[{"Title":"Caballo de troya","author":"J.J. Benitez","Stok":10,"Gender":"Fiction","loans":0},
         {"Title":"El dia del relampago","author":"J.J. Benitez","Stok":25,"Gender":"Fiction","loans":25},
         {"Title":"El principito","author":"Antoine de saint","Stok":12,"Gender":"Children","loans":0},
         {"Title":"El cuento de los hermanos green","author":"Jacob Grimm","Stok":12,"Gender":"Children","loans":0},
         {"Title":"Sintergica","author":"Jacob Grinberg","Stok":9,"Gender":"Science","loans":0},
         {"Title":"El cerebro consciente","author":"Jacob Grinberg","Stok":27,"Gender":"Science","loans":0},
         {"Title":"Autobiografia Jhon D. R.","author":"Rockerfeller","Stok":12,"Gender":"Biography","loans":0},
         {"Title":"Hacia rutas salvajes","author":"Jon Krakauer","Stok":12,"Gender":"No-Fiction","loans":0}]

def add_book(Name_book,Author,Stok,Gender,Loans):
    New_book={"Title":Name_book,"author":Author,"Stok":Stok,"Gender":Gender,"loans":Loans}
    library.append(New_book)
    print("Se agrego exitosamente el libro a su inventario!")
    print(library)

def search_book(searching_book):
    bolean=False
    for book in library:
        if book.get("Title") == searching_book:
            print(f"Estos son los detalles del libro que buscas: {book}.")
            bolean=True
    if not bolean:
        print("The book not exist this in library")
            
def register_loans(Name_book_loans):
    for book in library:
        if book["Title"] == Name_book_loans and book["loans"] < book["Stok"]:
            
            sum_loans= lambda library: book["loans"]+1
            New_loans=sum_loans(library)
            book.update({"loans":New_loans})
            print(f"Loans= {New_loans}")
            print(book)
        elif book["Title"] == Name_book_loans and book["Stok"] == book["loans"]:
            print("Todas las copias de este libro estan prestadas.")
            
def Return_book(Book_return):
    for book in library:
        if book["Title"] == Book_return:
            res_return= lambda library: book["loans"]-1
            res_loans=res_return(library)
            book.update({"loans":res_loans})
            print(f"Se a devuelto correctamente el libro a su stok correspondiente {book}")
            
def delete(book_delete):
    vuleano=False
    for i , book in enumerate(library):
        
        if book.get("Title")==book_delete:
            if book["loans"] == 0:
                del library[i]
                print(library)
                vuleano=True
            elif book["loans"] > 0:
                print("Este libro no se puede eliminar por que hay prestamos en el momento.")
                vuleano=True
    if not vuleano:
        print("Este libro no existe!")
        
def search_gender(option_gender):
    match option_gender:
        case 1:
            for book in library:
                if book["Gender"] == "Fiction":
                    print(book)
        case 2:
            for book in library:
                if book["Gender"] == "Children":
                    print(book)
        case 3:
            for book in library:
                if book["Gender"] == "No-Fiction":
                    print(book)
        case 4:
            for book in library:
                if book["Gender"] == "Biography":
                    print(book)
        case 5:
            for book in library:
                if book["Gender"] == "Science":
                    print(book)

def total_books():
    result=0
    copytotal=0
    acu_instore=0
    total=0
    total_instore= lambda library: sum(total+book["Stok"] for book in library)
    acu_instore=total_instore(library)
    
    copytotal= lambda library: acu_instore- sum(book["loans"] for book in library)
    result=copytotal(library)
    print(f"Hay {result} copias disponibles en nuestra libreria!")
    print(f"Hay {acu_instore} copias en total en nuestro inventario de todos los libros.")
        
                    
    
# ///////////////////////////////////////////////////////////////////////////////////////////////////    
while True:
    print("""BIENVENIDO A LA LIBRERIA
      Elegia la opcion correspondiente a realizar:
      1. Agregar un libro al inventario.
      2. Buscar un libro.
      3. Registrar prestamos de libros.
      4. Registrar devolucion de un libro.
      5. Eliminar un libro de su inventario.
      6. Buscar libros por genero.
      7. Mostrar total de libros en inventario y cuantos libros ay disponibles en la biblioteca
      8. Salir del programa.""")
    option=int(input("Digite la opcion que desea realizar: "))
    match option:
        case 1:
            Name_book=input("Digite el titulo del libro nuevo: ")
            Author=input("Digite el nombre de su autor: ")
            Stok=int(input("Digite la cantidad de libros que hay para almacenar en la libreria: "))
            Gender=input("Digite el genero de este libro: ")
            Loans=int(input("Como es un libro nuevo inicialice en 0 los prestamos de este libro: "))
            add_book(Name_book,Author,Stok,Gender,Loans)
        case 2:
            searching_book=input("Digite el titulo del libro que desea buscar: ")
            search_book(searching_book)
        case 3:
            Name_book_loans=input("Digite el libro que se prestara: ")
            register_loans(Name_book_loans)
        case 4:
            Book_return=input("Digite el libro que va devolver el cliente: ")
            Return_book(Book_return)
        case 5:
            book_delete=input("Digite el nombre del libro que desea eliminar de su inventario: ")
            delete(book_delete)
        case 6:
            option_gender=int(input("Digite que clase de genero busca en los libros: (1)Ficcion (2)Niños (3)No ficcion (4)Biografia (5)Ciencia:"))
            search_gender(option_gender)
        case 7:
            total_books()
        case 8:
            break
            

    