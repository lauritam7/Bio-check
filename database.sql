CREATE TABLE IF NOT EXISTS usuarios (
    id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL UNIQUE,
    contraseña TEXT NOT NULL,
    rol TEXT CHECK(rol IN ('admin', 'estandar')) NOT NULL
);
