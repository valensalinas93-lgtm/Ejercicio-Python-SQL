-- ============================================
-- Base de datos de práctica: LIBRERIA
-- Ejecuta este script completo en MySQL Workbench
-- (File → Open SQL Script → rayo ⚡)
-- ============================================

DROP DATABASE IF EXISTS libreria;
CREATE DATABASE libreria CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE libreria;

CREATE TABLE libros (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(100) NOT NULL,
    autor VARCHAR(60) NOT NULL,
    categoria VARCHAR(30) NOT NULL,
    precio DECIMAL(8, 2) NOT NULL,
    stock INT NOT NULL DEFAULT 0
);

INSERT INTO libros (titulo, autor, categoria, precio, stock) VALUES
('1984',                           'George Orwell',        'Novela',    12.95, 12),
('Rebelión en la granja',          'George Orwell',        'Novela',     9.95, 30),
('Homenaje a Cataluña',            'George Orwell',        'Ensayo',    13.50,  8),
('Un mundo feliz',                 'Aldous Huxley',        'Novela',    11.95, 25),
('Fahrenheit 451',                 'Ray Bradbury',         'Novela',    10.95,  0),
('El shock del futuro',            'Alvin Toffler',        'Ensayo',    14.90,  6),
('La tercera ola',                 'Alvin Toffler',        'Ensayo',    15.90, 14),
('El cambio del poder',            'Alvin Toffler',        'Ensayo',    16.50,  0),
('Sesenta semanas en el trópico',  'Antonio Escohotado',   'Ensayo',    19.90,  5),
('Los enemigos del comercio',      'Antonio Escohotado',   'Ensayo',    34.90,  9),
('Caos y orden',                   'Antonio Escohotado',   'Filosofía', 21.00, 11),
('Ética para Amador',              'Fernando Savater',     'Filosofía',  9.95, 40),
('Política para Amador',           'Fernando Savater',     'Filosofía',  9.95, 22),
('Las preguntas de la vida',       'Fernando Savater',     'Filosofía', 10.95, 18),
('El valor de educar',             'Fernando Savater',     'Ensayo',     9.50, 16),
('La sociedad del cansancio',      'Byung-Chul Han',       'Filosofía', 12.00, 35),
('La condición humana',            'Hannah Arendt',        'Filosofía', 14.95, 13),
('Meditaciones',                   'Marco Aurelio',        'Filosofía',  8.95, 50),
('Sapiens',                        'Yuval Noah Harari',    'Ensayo',    13.95, 28),
('La rebelión de las masas',       'José Ortega y Gasset', 'Filosofía', 11.50, 20),
('La rebelión de Atlas',           'Ayn Rand',             'Novela',    24.90, 10),
('El manantial',                   'Ayn Rand',             'Novela',    19.90, 15);

-- Comprobación: si todo ha ido bien, esta consulta muestra los 22 libros
SELECT * FROM libros;
