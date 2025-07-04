# Clase que representa el sistema principal de adopciones.
class SistemaAdopcion:
    # Inicializo el sistema con listas vacías de perros y usuarios para guardar la información de cada perro y usuario que se vaya creando en el sistema.
    def __init__(self):
        self.perros = []
        self.usuarios = []

    # Método para crear un nuevo perro y agregarlo a la lista de perros.
    def cargar_perro(self, perro):
        self.perros.append(perro)
        perro.mostrar_id_perro()

    # Método para eliminar un perro de la lista de perros.
    def eliminar_perro(self, id_perro):
        perro_a_eliminar = None
        for perro in self.perros:
            if str(perro.id) == str(id_perro): # perro.id es un entero pero, id_perro es un string. Por eso convertimos ambos a string para que al comparar los datos, arroje un resultado correcto.
                perro_a_eliminar = perro # Guardo la info del perro que quiero eliminar porque en el mensaje de confirmación queremos mostrar el nombre y el id del perro eliminado.
                break
        if perro_a_eliminar:
            self.perros.remove(perro_a_eliminar)
            print(f"El perro '{perro_a_eliminar.nombre}' con ID {perro_a_eliminar.id} se eliminó correctamente.")
        else:
            print("No se encontró ningún perro con ese ID.")

    # Método para crear un nuevo usuario y agregarlo a la lista de usuarios.
    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)
        usuario.mostrar_id_usuario()

    # Método de búsqueda de un perro por ID.
    def buscar_perro(self, id_perro):
        for perro in self.perros:
            if str(perro.id) == str(id_perro): # perro.id es un entero pero, id_perro es un string. Por eso convertimos ambos a string para que al comparar los datos, arroje un resultado correcto.
                return perro
        return print(f"El perro que estás buscando, no existe! Lo borraste o nunca lo creaste")

    # Método de búsqueda de un usuario por DNI.
    def buscar_usuario(self, dni_usuarioAdoptante):
        for usuario in self.usuarios:
            if usuario.dni == dni_usuarioAdoptante:
                return usuario
        return print(f"El usuario que estás buscando, no existe! Nunca lo creaste paparule")
    
    # Método para encontrar perros para un usuario según sus preferencias: sexo, raza, edad, tamaño
    def recomendar_perros(self, usuario):
        sugerencias = []
        for perro in self.perros:
            if perro.estado != 'disponible':  # Verifico que el perro esté disponible, si no, paso al siguiente
                continue
            # Variables booleanas para analizar si las preferencias del usuario se cumplen o no
            cumple_raza = usuario.preferencias['raza'] == 'indistinto' or perro.raza == usuario.preferencias['raza']
            cumple_edad = usuario.preferencias['edad'] == 'indistinto' or perro.edad == usuario.preferencias['edad']
            cumple_tamaño = usuario.preferencias['tamaño'] == 'indistinto' or perro.tamaño == usuario.preferencias['tamaño']
            if cumple_raza and cumple_edad and cumple_tamaño:
                sugerencias.append(perro)
        # Mensaje al usuario según si hubo o no sugerencias
        if sugerencias:
            print("Te sugerimos estos pichichos:")
            for perro in sugerencias:
                perro.mostrar_info_perro()
        else:
            print("No encontramos un perro de acuerdo a tus preferencias... ¡Adoptá un gato!")
        return sugerencias

    # Método de reserva de un perro
    def reservar_perro(self, dni_usuarioAdoptante, id_perro):
        usuario = self.buscar_usuario(dni_usuarioAdoptante)
        perro = self.buscar_perro(id_perro)
        if perro and usuario and perro.estado == 'disponible':
            perro.cambiar_estado('reservado')
            print(f"{usuario.nombre} ha reservado a {perro.nombre}.")
        else:
            print("Error: el perro no está disponible o el usuario no existe.")

    # Método para confirmar una adopción de un perro. 
    # Cambia el estado del perro a 'adoptado' y lo agrega al historial del usuario.
    def confirmar_adopcion(self, dni_usuarioAdoptante, id_perro):
        usuario = self.buscar_usuario(dni_usuarioAdoptante)
        perro = self.buscar_perro(id_perro)
        if perro and usuario and perro.estado == 'reservado':
            perro.cambiar_estado('adoptado')
            usuario.historial_adopciones.append(perro)
            print(f"{usuario.nombre} ha adoptado a {perro.nombre}.")
        else:
            print("Error: el perro no está reservado o los datos no coinciden.")

    # Método que muestra el listado de perros.
    def mostrar_perros(self, estado=None):
        print(f"Listado de perros (estado: {estado if estado else 'todos'}):")
        for perro in self.perros:
            if estado is None or perro.estado == estado:
                perro.mostrar_info_perro()

    # Método que muestra el listado de usuarios adoptantes.
    def mostrar_usuarios(self):
        print(f"Listado de usuarios adoptantes registrados")
        for usuario in self.usuarios:
            usuario.mostrar_info_usuario()