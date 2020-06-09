from member import Member
from repository import Repository


class MemberService():

    def crearPersona(self):
        print("\n----Agregar persona----")
        name = input('Ingrese un nombre: ')
        surname = input('Ingrese un apellido: ')
        age = int(input('Ingrese una edad: '))
        phone = int(input('Ingrese un telefono: '))
        return Member(name, surname, age, phone)

    def add_person(self, member=None):
        if member is None:
            member.crearPersona()
        memberKey = -1
        for clave in Repository.membersList:
            memberKey = clave
        memberKey = memberKey + 1
        Repository.membersList[memberKey] = member.__dict__

    def update_person(self, legajo):
        num = 1
        while num != 0:
            num2 = 1
            if num2 == 1:
                print("-----Modificando-----")

                name = input('Introduzca el nuevo nombre: ')
                Repository.membersList[legajo]["_name"] = name
                print(Repository.membersList)

                surname = input('Introduzca un nuev apellido: ')
                Repository.membersList[legajo]["_surname"] = surname
                print(Repository.membersList)

                age = int(input('Introduzca una nueva edad: '))
                Repository.membersList[legajo]["_age"] = age
                print(Repository.membersList)

                phone = int(input('Introduzca un nuevo telefono: '))
                Repository.membersList[legajo]["_phone"] = phone
                print(Repository.membersList)

            terminar = str(input("Quiere volver a corregirlo: "))
            if terminar == "no":
                break
