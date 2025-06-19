# Clase que representa a un usuario que desea adoptar un perro.
class UsuarioAdoptante:
    creador_ids_usuarios = 1
    # Constructor del usuario adoptante.
    def __init__(self, nombre, apellido, dni, email, sexo="indistinto", raza="indistinto", edad="indistinto", tamaño="indistinto"):
        self.id = UsuarioAdoptante.creador_ids_usuarios # asigna el valor actual de la variable creador_ids_usuarios
        UsuarioAdoptante.creador_ids_usuarios += 1 # incrementa el contador para que el próximo usuario tenga un id diferente y único
        self.nombre = nombre # nombre del usuario.
        self.apellido = apellido # nombre del usuario.
        self.dni = dni # DNI del usuario.
        self.email = email # email del usuario.
        # Preferencias agrupadas en un solo atributo tipo diccionario
        self.preferencias = {
            "sexo": sexo, # sexo preferido del perro a adoptar.
            "raza": raza, # raza preferida del perro a adoptar.
            "edad": edad, # edad preferida del perro a adoptar.
            "tamaño": tamaño # tamaño preferido del perro a adoptar.
        }
        self.historial_adopciones = [] # Lista de perros adoptados

    # Método para modificar datos del usuario y/o sus preferencias
    def modificar_datos(self, nombre, apellido, dni, email, sexo, raza, edad, tamaño):
        if nombre: self.nombre = nombre
        if apellido: self.apellido = apellido
        if dni: self.dni = dni
        if email: self.email = email
        if sexo: self.preferencias["sexo"] = sexo
        if raza: self.preferencias["raza"] = raza
        if edad: self.preferencias["edad"] = edad
        if tamaño: self.preferencias["tamaño"] = tamaño

    # Método para ver la lista de perros adoptados por el usuario.
    def ver_historial(self):
        if not self.historial_adopciones:
            print(f"{self.nombre} {self.apellido} aún no ha adoptado ningún perro.")
        else:
            print(f" Historial de adopciones de {self.nombre} {self.apellido}:")
            for perro in self.historial_adopciones:
                perro.mostrar_info_perro() # llamo al método de la clase perro o de su hija PerroAdulto