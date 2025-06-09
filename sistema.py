from usuario import Usuario

usuarios = []  # Lista para guardar usuarios

def validar_contraseña(contrasena):
    if len(contrasena) < 6:
        return False
    tiene_letra = any(c.isalpha() for c in contrasena)
    tiene_numero = any(c.isdigit() for c in contrasena)
    return tiene_letra and tiene_numero

def registrar_usuario():
    print("\n--- Registro de Usuario ---")
    id_usuario = len(usuarios) + 1
    nombre = input("Ingrese nombre: ")
    
    while True:
        contraseña = input("Ingrese contraseña (mínimo 6 caracteres, letras y números): ")
        if validar_contraseña(contraseña):
            break
        else:
            print("Contraseña inválida. Debe tener mínimo 6 caracteres, incluir letras y números.")
    
    rol = input("Ingrese rol ('admin' o 'estandar'): ").lower()
    if rol not in ["admin", "estandar"]:
        rol = "estandar"
        print("Rol asignado por defecto: estandar")
    
    nuevo_usuario = Usuario(id_usuario, nombre, contraseña, rol)
    usuarios.append(nuevo_usuario)
    print(f"Usuario {nombre} registrado exitosamente.\n")

def iniciar_sesion():
    print("\n--- Iniciar Sesión ---")
    nombre = input("Ingrese nombre: ")
    contraseña = input("Ingrese contraseña: ")
    
    for usuario in usuarios:
        if usuario.nombre == nombre and usuario.contraseña == contraseña:
            print(f"Bienvenido, {usuario.nombre}!")
            return usuario
    print("Nombre o contraseña incorrectos.")
    return None

def listar_usuarios():
    if not usuarios:
        print("No hay usuarios registrados.")
        return
    print("\n--- Lista de Usuarios ---")
    for u in usuarios:
        u.ver_datos()
def cambiar_rol():
    print("\n--- Cambiar Rol de Usuario ---")
    if not usuarios:
        print("No hay usuarios registrados.")
        return
    id_usuario = input("Ingrese el ID del usuario al que desea cambiar el rol: ")
    for usuario in usuarios:
        if str(usuario.id_usuario) == id_usuario:
            nuevo_rol = input("Ingrese nuevo rol ('admin' o 'estandar'): ").lower()
            if nuevo_rol in ["admin", "estandar"]:
                usuario.rol = nuevo_rol
                print(f"Rol de {usuario.nombre} cambiado a {nuevo_rol}.")
            else:
                print("Rol inválido.")
            return
    print("Usuario no encontrado.")

def eliminar_usuario():
    print("\n--- Eliminar Usuario ---")
    if not usuarios:
        print("No hay usuarios registrados.")
        return
    id_usuario = input("Ingrese el ID del usuario a eliminar: ")
    for i, usuario in enumerate(usuarios):
        if str(usuario.id_usuario) == id_usuario:
            confirmacion = input(f"¿Confirma eliminar al usuario {usuario.nombre}? (s/n): ").lower()
            if confirmacion == 's':
                usuarios.pop(i)
                print("Usuario eliminado.")
            else:
                print("Operación cancelada.")
            return
    print("Usuario no encontrado.")
    
