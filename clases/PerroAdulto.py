# Importo la clase padre "Perro" para que se puedan usar sus atributos y métodos.
from clases.Perro import Perro
#  Subclase de Perro para perros adultos, mayores de 8 años. Aplicamos herencia para dar un mensaje distinto pisando el método mostrar_info_perro.
class PerroAdulto(Perro):
    # Pisamos el método mostrar_info_perro.
    def mostrar_info_perro(self):
        print(f"{self.nombre} (ID: {self.id}), es un {self.raza} y tiene {self.edad} años - Estado: {self.estado}")