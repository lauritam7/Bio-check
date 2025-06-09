from sistema import (
    registrar_usuario,
    iniciar_sesion,
    listar_usuarios,
    cambiar_rol,
    eliminar_usuario,
    usuarios
)

def mostrar_menu_admin():
    """
    Muestra las opciones disponibles para el rol administrador.
    """
    print("\n--- Menú Administrador ---")
    print("1. Listar usuarios")
    print("2. Cambiar rol de usuario")
    print("3. Eliminar usuario")
    print("4. Cerrar sesión")

def mostrar_menu_usuario():
    """
    Muestra las opciones disponibles para el rol estándar.
    """
    print("\n--- Menú Usuario Estándar ---")
    print("1. Ver mis datos")
    print("2. Cerrar sesión")

def main():
    """
    Función principal del sistema. Muestra el menú principal y 
    delega según las acciones del usuario.
    """
    while True:
        print("\n=== Menú Principal ===")
        print("1. Registrarse")
        print("2. Iniciar sesión")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_usuario()

        elif opcion == "2":
            usuario = iniciar_sesion()
            if usuario:
                if usuario.rol == "admin":
                    while True:
                        mostrar_menu_admin()
                        op_admin = input("Seleccione opción: ")
                        if op_admin == "1":
                            listar_usuarios()
                        elif op_admin == "2":
                            cambiar_rol()
                        elif op_admin == "3":
                            eliminar_usuario()
                        elif op_admin == "4":
                            print("Cerrando sesión...")
                            break
                        else:
                            print("Opción inválida.")
                else:
                    while True:
                        mostrar_menu_usuario()
                        op_std = input("Seleccione opción: ")
                        if op_std == "1":
                            usuario.ver_datos()
                        elif op_std == "2":
                            print("Cerrando sesión...")
                            break
                        else:
                            print("Opción inválida.")

        elif opcion == "3":
            print("¡Hasta luego!")
            break

        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()

