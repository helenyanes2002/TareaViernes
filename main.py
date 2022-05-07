
from Controller import Controller
ciclista = Controller()


nombre=input("ingrese nombre: ")
edad=int(input("ingrese edad: "))
pais=input("ingrese pais: ")
tiempo=int(input("ingrese tiempo: "))
opcion = input("desea agregar otro ciclista? s/n:")
ciclista.ingresar(nombre,edad,pais, tiempo)  


while(opcion == 's'):
    nombre=input("ingrese nombre: ")
    edad=int(input("ingrese edad: "))
    pais=input("ingrese pais: ")
    tiempo=int(input("ingrese tiempo: "))
    opcion = input("desea agregar otro ciclista? s/n: ")
    ciclista.ingresar(nombre,edad,pais, tiempo)  

    

print(ciclista.all())