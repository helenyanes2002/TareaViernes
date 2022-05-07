#Codificar un programa que permita recibir el nombre, edad, país y tiempo(minutos)) 
# de la ultima prueba de crono individual de varios ciclistas del tour de Francia, 
# al final el software estará en la capacidad de indicar cual fue el ciclista con 
# el mejor tiempo y mostrar todos sus datos


class Ciclista:
     __nombre = None
     __edad = None
     __pais = None 
     __tiempo = None

     @property
     def nombre(self):
         return self.__nombre

     @property
     def edad(self):
       return self.__edad

     @property
     def pais(self):
         return self.__pais

     @property
     def tiempo(self):
       return self.__tiempo
  

     @nombre.setter
     def nombre(self,nombre):
          self.__nombre=nombre
     
     @edad.setter
     def edad(self,edad):
         if(edad < 0):
             return False
         else:
            self.__edad=edad
    
     @pais.setter
     def pais(self,pais):
         self.__pais=pais
 
     @tiempo.setter
     def tiempo(self,tiempo):
         if(tiempo < 0):
             return False
         else:
            self.__tiempo=tiempo
       
