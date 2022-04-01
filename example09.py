#Encapsulacion: Es el proceso de mantener los datos y metodos juntos como una unidad
#Ventajas de la encapsulacion:
    #Las clases hacen que el codigo sea facil de cambiar y mantener
    #Las propiedades que se ocultaran se pueden especificar facilmente
    #Las clases o funciones externas pueden acceder a las propiedades de la clase

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_user(self):  #Display = mostar
        print("Use Name Is: ", self.name)
        print("User Age Is: ", self.age)
        
user1 = User("Jhon Doe", 35)

#Llamando al metodo de la clase
user1.display_user()

#Accediendo directamente a las variables
user1.name
user1.age
