from book import Book
from repository import Repository


class BookService():

    def crearBook(self):
        print("\n----Agregar persona----")
        name = input('Ingrese un nombre: ')
        authorName = input('Ingrese el autor: ')
        memberLegajo = int(input('Ingrese un legajo: '))
        return Book(name, authorName, memberLegajo)

    def add_book(self, book=None):
        if book is None:
            book.crearBook()
        bookKey = -1
        for clave in Repository.booksList:
            bookKey = clave
        bookKey = bookKey + 1
        Repository.booksList[bookKey] = book.__dict__

    def update_book(self, bookKey):
        num = 1
        while num != 0:
            num2 = 1
            if num2 == 1:
                print("-----Modificando libro-----")

                name = input('Introduzca el nuevo nombre: ')
                Repository.booksList[bookKey]["_name"] = name
                print(Repository.booksList)

                authorName = input('Introduzca el nuevo autor: ')
                Repository.booksList[bookKey]["_authorName"] = authorName
                print(Repository.booksList)

                memberLegajo = int(input('Introduzca un nueva legajo: '))
                Repository.booksList[bookKey]["_memberLegajo"] = memberLegajo
                print(Repository.booksList)
            terminar = str(input("Quiere volver a corregirlo: "))
            if terminar == "no":
                break
