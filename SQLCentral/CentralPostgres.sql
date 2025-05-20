-- Crear la base de datos y activar extensiones

-- Crear base de datos (si no existe)
CREATE DATABASE centraldb;

-- Conectarse a la base
\c centraldb

-- Activar extensión para UUIDs
CREATE EXTENSION IF NOT EXISTS "pgcrypto";

-- Crear las tablas

-- Tabla: clientes
CREATE TABLE clientes (
id_cliente UUID PRIMARY KEY DEFAULT gen_random_uuid(),
cedula VARCHAR(15) UNIQUE NOT NULL,
nombre_completo VARCHAR(100) NOT NULL,
telefono VARCHAR(20),
correo VARCHAR(100),
fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
saldo_actual DECIMAL(10,2) DEFAULT 0
);

-- Tabla: historial de envíos
CREATE TABLE historial_envios (
id_envio UUID PRIMARY KEY DEFAULT gen_random_uuid(),
id_cliente UUID REFERENCES clientes(id_cliente) ON DELETE SET NULL,
fecha_envio TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
estado VARCHAR(20),
costo_envio DECIMAL(10,2),
qr_codigo TEXT
);

-- Tabla: historial de pagos (recargas)
CREATE TABLE historial_pagos (
id_pago UUID PRIMARY KEY DEFAULT gen_random_uuid(),
id_cliente UUID REFERENCES clientes(id_cliente) ON DELETE CASCADE,
monto DECIMAL(10,2) NOT NULL CHECK (monto > 0),
fecha_pago TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
medio_pago VARCHAR(50)
);

--Crear rol de replicación

-- Crear un usuario de replicación
CREATE USER dev_admin WITH PASSWORD 'dev123';

CREATE ROLE rol_replica WITH REPLICATION LOGIN PASSWORD '12345';

-- Otorgar permisos necesarios
GRANT ALL PRIVILEGES ON DATABASE centraldb TO dev_admin;

GRANT CONNECT ON DATABASE centraldb TO rol_replica;
GRANT USAGE ON SCHEMA public TO rol_replica;
GRANT SELECT ON ALL TABLES IN SCHEMA public TO rol_replica;

-- Para futuras tablas también
ALTER DEFAULT PRIVILEGES IN SCHEMA public
GRANT SELECT ON TABLES TO rol_replica;

--Crear la publicación lógica

-- Crear la publicación con las 3 tablas
CREATE PUBLICATION central_pub
FOR TABLE clientes, historial_envios, historial_pagos;
SELECT * FROM api_cliente;