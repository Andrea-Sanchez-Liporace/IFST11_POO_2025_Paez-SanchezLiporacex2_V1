# Importamos las clases desde __init__.py
from clases import Perro, PerroAdulto, UsuarioAdoptante, SistemaAdopcion

# Función principal del sistema
def main():
    # Instancio el sistema
    sistema = SistemaAdopcion()

    # Menú de opciones
    while True:
        print("\n Menu del Sistema de Adopcion")
        print("1. Registrar usuario")
        print("2. Cargar perro")
        print("3. Eliminar perro")       
        print("4. Mostrar perros disponibles")
        print("5. Postular a adopcion")
        print("6. Confirmar adopcion")
        print("7. Sugerencias por preferencias")
        print("8. Ver historial de usuario")
        print("9. Ver listado de usuarios adoptantes")
        print("0. Salir")

        # El usuario selecciona una opción
        opcion = input("Elegi una opcion: ")

        # Opción 1: Registrar nuevo usuario adoptante
        if opcion == "1":
            nombre = input("Nombre: ")
            apellido = input ("Apellido: ")
            dni = input("DNI: ")
            email = input("Email: ")
            sexo = input ("Preferencia de sexo: ")
            raza = input("Preferencia de raza: ")
            edad = int(input("Preferencia de edad: "))
            tamaño = input("Preferencia de tamaño: ")
            # Guardo las preferencias como un diccionario
            preferencias = {'sexo':sexo, 'raza': raza, 'edad': edad, 'tamaño': tamaño}
            # Creo una instancia del usuario y lo registro
            usuario = UsuarioAdoptante(nombre, apellido, dni, email, preferencias)
            sistema.registrar_usuario(usuario)
            # Le confirmo al usuario que quedó registrado
            print("Usuario registrado.")

        # Opción 2: Cargar un nuevo perro
        elif opcion == "2":
            nombre = input("Nombre del perro: ")
            raza = input("Raza: ")
            edad = int(input("Edad: "))
            sexo = input("Sexo: ")
            tamaño = input("Tamaño: ")
            peso = float(input("Peso: "))
            estado_salud = input("Estado de salud: ")
            vacunado = input("¿Está vacunado? (s/n): ").lower() == "s"  # convierte 's' a True, otra cosa a False
            estado = "disponible"
            temperamento = input("Temperamento: ")
            # Si el perro tiene 8 años o más, usamos la subclase PerroAdulto (clase hija de padre)
            if edad >= 8:
                perro = PerroAdulto(nombre, raza, edad, sexo, tamaño, peso, estado_salud, vacunado, estado, temperamento)
            # Sino, usamos la clase perro (clase padre)
            else:
                perro = Perro(nombre, raza, edad, sexo, tamaño, peso, estado_salud, vacunado, estado, temperamento)
            # Cargamos el perro al sistema
            sistema.cargar_perro(perro)
            # Le confirmo al usuario que el perro quedó registrado
            print("Perro cargado.")

        # Opción 3: Eliminar perros disponibles
        elif opcion == "3":
            id_perro = input("ID del perro: ")
            sistema.eliminar_perro(id_perro)

        # Opción 4: Mostrar perros disponibles
        elif opcion == "4":
            sistema.mostrar_perros("disponible")

        # Opción 5: Postular un usuario para adoptar un perro (reserva)
        elif opcion == "5":
            dni_usuarioAdoptante = input("DNI del usuario: ")
            id_perro = input("ID del perro: ")
            sistema.reservar_perro(dni_usuarioAdoptante, id_perro)

        # Opción 6: Confirmar la adopción (pasa de reservado a adoptado)
        elif opcion == "6":
            dni_usuarioAdoptante = input("DNI del usuario: ")
            id_perro = input("ID del perro: ")
            sistema.confirmar_adopcion(dni_usuarioAdoptante, id_perro)

        # Opción 7: Sugerir perros según las preferencias del usuario
        elif opcion == "7":
            dni_usuarioAdoptante = input("DNI del usuario: ")
            usuario = sistema.buscar_usuario(dni_usuarioAdoptante)
            if usuario:
                sistema.recomendar_perros(usuario)
            else:
                print("Usuario no encontrado.")

        # Opción 8: Mostrar historial de adopciones del usuario
        elif opcion == "8":
            dni_usuarioAdoptante = input("DNI del usuario: ")
            usuario = sistema.buscar_usuario(dni_usuarioAdoptante)
            if usuario:
                usuario.ver_historial()
            else:
                print("Usuario no encontrado.")

        # Opción 9: Mostrar usuarios adoptantes
        elif opcion == "9":
            sistema.mostrar_usuarios()

        # Opción 0: Salir del programa
        elif opcion == "0":
            print("¡Hasta luego!")
            break

        # En caso de que el usuario ingrese una opción inválida
        else:
            print("Ingresaste una opción inválida.")

if __name__ == "__main__":
   main()