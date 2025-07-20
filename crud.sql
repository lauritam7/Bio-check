-- Insertar un nuevo usuario
INSERT INTO usuarios (nombre, contraseña, rol) VALUES ('nico', 'abc123', 'estandar');

-- Listar usuarios
SELECT * FROM usuarios;

-- Actualizar el rol de un usuario
UPDATE usuarios SET rol = 'admin' WHERE nombre = 'nico';

-- Eliminar un usuario
DELETE FROM usuarios WHERE nombre = 'nico';
