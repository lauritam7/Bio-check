from usuario import Usuario
from sistema import usuarios

def test_registrar_usuario():
    usuarios.clear()
    u = Usuario(1, "juan", "abc123", "estandar")
    usuarios.append(u)
    assert usuarios[0].nombre == "juan"
    assert usuarios[0].contraseña == "abc123"
    assert usuarios[0].rol == "estandar"

def test_iniciar_sesion():
    usuarios.clear()
    u = Usuario(2, "maria", "pass123", "admin")
    usuarios.append(u)
    nombre = "maria"
    contraseña = "pass123"
    usuario = None
    for user in usuarios:
        if user.nombre == nombre and user.contraseña == contraseña:
            usuario = user
            break
    assert usuario is not None
    assert usuario.rol == "admin"

def test_cambiar_rol():
    usuarios.clear()
    u = Usuario(3, "carlos", "clave123", "estandar")
    usuarios.append(u)
    assert usuarios[0].rol == "estandar"
    usuarios[0].rol = "admin"
    assert usuarios[0].rol == "admin"

def test_eliminar_usuario():
    usuarios.clear()
    u = Usuario(4, "ana", "test456", "estandar")
    usuarios.append(u)
    assert len(usuarios) == 1
    usuarios.pop(0)
    assert len(usuarios) == 0

if __name__ == "__main__":
    test_registrar_usuario()
    test_iniciar_sesion()
    test_cambiar_rol()
    test_eliminar_usuario()
    print("✅ Todos los tests pasaron correctamente.")

