# Clase que representa a un perro dentro del sistema.
class Perro:
    creador_ids_perros = 1
    # Constructor de la clase Perro.
    def __init__(self, nombre, raza, edad, sexo, tamaño, peso, estado_salud, vacunado, estado, temperamento):
        self.id = Perro.creador_ids_perros # asigna el valor actual de la variable creador_ids_perros
        Perro.creador_ids_perros += 1 # incrementa el contador para que el próximo perro tenga un id diferente y único
        self.nombre = nombre # nombre del perro.
        self.raza = raza # raza del perro.
        self.edad = edad # edad en años.
        self.sexo = sexo # sexo del perro.
        self.tamaño = tamaño # chico, mediano o grande.
        self.peso = peso # peso en kg.
        self.estado_salud = estado_salud # descripción de su estado de salud.
        self.vacunado = vacunado # booleano (True o False).
        self.estado = estado # 'disponible', 'reservado', 'adoptado'.
        self.temperamento = temperamento # carácter del perro (tranquilo, juguetón, etc.).

    # Método para cambiar el estado del perro ('disponible', 'reservado', 'adoptado').
    def cambiar_estado(self, nuevo_estado):
        self.estado = nuevo_estado

    # Método para mostrar información básica del perro.
    def mostrar_info_perro(self):
        print(f"{self.nombre} ({self.raza}) - Edad: {self.edad} años, Tamaño: {self.tamaño}, Estado: {self.estado}")