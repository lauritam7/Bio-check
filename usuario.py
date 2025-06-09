class Usuario:
    """
    Representa un usuario del sistema.

    Atributos:
        id_usuario (int): ID único del usuario.
        nombre (str): Nombre del usuario.
        contraseña (str): Contraseña del usuario.
        rol (str): Rol del usuario ('admin' o 'estandar').
    """

    def __init__(self, id_usuario, nombre, contraseña, rol="estandar"):
        """
        Inicializa un nuevo usuario con los datos proporcionados.
        """
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.contraseña = contraseña
        self.rol = rol

    def ver_datos(self):
        """
        Muestra los datos del usuario por pantalla.
        """
        print(f"\nID: {self.id_usuario}")
        print(f"Nombre: {self.nombre}")
        print(f"Rol: {self.rol}")

