#  Subclase de Perro para perros adultos, mayores de 8 años. Aplicamos herencia para dar un mensaje distinto pisando el método mostrar_info_perro.
class PerroAdulto():
    # Pisamos el método mostrar_info_perro.
    def mostrar_info_perro(self):
        print(f"{self.nombre} tiene {self.edad} años - Estado: {self.estado}")