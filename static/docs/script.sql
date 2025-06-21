DROP DATABASE IF EXISTS gestionventasinventario;
CREATE DATABASE gestionventasinventario;

\c gestionventasinventario

CREATE TABLE status (
    cods INTEGER NOT NULL PRIMARY KEY,
    dstatus VARCHAR(12) NOT NULL
);

INSERT INTO status (cods, dstatus) VALUES
(0, 'ELIMINADO'),
(1, 'ACTIVO');

CREATE TABLE login (
    id SERIAL NOT NULL PRIMARY KEY,
    nombre VARCHAR(12) NOT NULL,
    usuario VARCHAR(12) NOT NULL,
    clave VARCHAR(40) NOT NULL,
    fkcods INTEGER NOT NULL DEFAULT 1,
    FOREIGN KEY (fkcods) REFERENCES status(cods) ON UPDATE CASCADE ON DELETE RESTRICT
);

INSERT INTO login (nombre, usuario, clave) VALUES 
('EDGAR', 'ADMIN', '123456');

CREATE TABLE productos (
    codprod INTEGER NOT NULL PRIMARY KEY,
    nomprod VARCHAR(80) NOT NULL,
    cantprod INTEGER NOT NULL,
    precio NUMERIC(12,2) NOT NULL,
    fkcods INTEGER NOT NULL DEFAULT 1,
    FOREIGN KEY (fkcods) REFERENCES status(cods) ON UPDATE CASCADE ON DELETE RESTRICT
);

-- Inserción de 60 productos en la tabla productos

INSERT INTO productos (codprod, nomprod, cantprod, precio) VALUES
(1, 'Doritos 140 mg', 75, 3500.00),
(2, 'Pony Malta 330 ml', 50, 2500.00),
(3, 'Chocoramo', 100, 2200.00),
(4, 'Galletas Festival', 80, 1800.00),
(5, 'Arequipe Alpina 200g', 40, 4200.00),
(6, 'Arroz Diana 1kg', 60, 4500.00),
(7, 'Aceite Premier 1L', 30, 8900.00),
(8, 'Huevo por unidad', 90, 500.00),
(9, 'Pan Tajado Bimbo', 35, 5500.00),
(10, 'Huevos Kikes 12 und', 45, 8800.00),
(11, 'Azucar Incauca 1kg', 55, 3900.00),
(12, 'Leche Alqueria 1L', 60, 3500.00),
(13, 'Cafe Aguila Roja 250g', 25, 8200.00),
(14, 'Detergente Fab 500g', 70, 3600.00),
(15, 'Trident 40mg', 120, 4000.00),
(16, 'Papel Higienico Familia x4', 40, 5600.00),
(17, 'Gaseosa Colombiana 1.5L', 65, 4600.00),
(18, 'Agua Cristal 600 ml', 80, 1800.00),
(19, 'Frijoles Cargamanto 500g', 50, 4200.00),
(20, 'Lentejas Diana 500g', 45, 3900.00),
(21, 'Salchichas Zenu x6', 30, 5200.00),
(22, 'Atun Van Camps 160g', 35, 5700.00),
(23, 'Salsa de Tomate Fruco 400g', 40, 3400.00),
(24, 'Mayonesa Fruco 200g', 25, 4200.00),
(25, 'Mostaza Fruco 200g', 25, 3900.00),
(26, 'Cubitos Knorr x12', 60, 2500.00),
(27, 'Chocolate Corona en pastilla', 40, 5200.00),
(28, 'Leche condensada Alpina 395g', 30, 6800.00),
(29, 'Cereal Choco Krispis 300g', 20, 7800.00),
(30, 'Tostacos Natuchips 140g', 60, 3500.00),
(31, 'Mani salado Yupi 150g', 35, 3200.00),
(32, 'Nectar Hit 1L', 50, 3400.00),
(33, 'Vinagre La Constancia 500ml', 20, 2600.00),
(34, 'Harina Pan 1kg', 25, 4600.00),
(35, 'Arepas Dona Paisa x5', 40, 3800.00),
(36, 'Huevos AA x30', 20, 12800.00),
(37, 'Empanadas listas Zenu x6', 15, 6700.00),
(38, 'Mantequilla Alpina 250g', 30, 5400.00),
(39, 'Yogurt Yogo Yogo 150ml', 70, 1600.00),
(40, 'Queso Campesino Alpina 500g', 25, 9500.00),
(41, 'Sopa Maggi Gallina 65g', 60, 1200.00),
(42, 'Avena Alpina 250ml', 45, 1800.00),
(43, 'Champu Savital 400ml', 20, 6900.00),
(44, 'Crema Dental Colgate 100ml', 50, 3700.00),
(45, 'Jabon Protex 120g', 35, 4200.00),
(46, 'Traperos EspumaMax', 15, 7500.00),
(47, 'Bolsa de basura negra x10', 40, 2500.00),
(48, 'Escoba DuraMax', 18, 8500.00),
(49, 'Toalla Cocina Familia x1', 35, 4700.00),
(50, 'Vela Aromatica pequena', 22, 2300.00),
(51, 'Encendedor Cricket', 50, 1500.00),
(52, 'Cerillos x100', 45, 1000.00),
(53, 'Bolsas Ziploc x10', 25, 3900.00),
(54, 'Cloro Clorox 1L', 30, 4600.00),
(55, 'Limpiador Mr Musculo 500ml', 28, 5100.00),
(56, 'Desinfectante Lysol 360ml', 22, 7800.00),
(57, 'Esponja Multiusos x2', 60, 2200.00),
(58, 'Almohadas El Rey', 10, 15900.00),
(59, 'Velas de cumpleanos x5', 50, 2000.00),
(60, 'Almohabon Familiar x1', 12, 9900.00);

CREATE TABLE venta (
    nv SERIAL NOT NULL PRIMARY KEY,
    cliente VARCHAR(20),
    total NUMERIC(12,2) NOT NULL,
    fkcods INTEGER NOT NULL DEFAULT 1,
    fecha DATE NOT NULL,
    hora TIME,
    FOREIGN KEY (fkcods) REFERENCES status(cods) ON UPDATE CASCADE ON DELETE RESTRICT
);



CREATE TABLE detalleventa (
    id SERIAL NOT NULL PRIMARY KEY,
    producto VARCHAR(80) NOT NULL,
    cantidad INTEGER NOT NULL,
    precio NUMERIC(12,2) NOT NULL,
    fknv INTEGER NOT NULL,
    fkcods INTEGER NOT NULL DEFAULT 1,
    FOREIGN KEY (fknv) REFERENCES venta(nv) ON UPDATE CASCADE ON DELETE RESTRICT,
    FOREIGN KEY (fkcods) REFERENCES status(cods) ON UPDATE CASCADE ON DELETE RESTRICT
);

CREATE TABLE log_cambios (
    id SERIAL PRIMARY KEY,
    tabla VARCHAR(50) NOT NULL,
    operacion VARCHAR(10) NOT NULL, -- INSERT, UPDATE, DELETE
    usuario VARCHAR(50) DEFAULT current_user,
    fecha TIMESTAMP DEFAULT current_timestamp,
    datos_ant JSONB,     
    datos_nuevos JSONB,
    fkcods integer not null default 1,
    foreign key(fkcods) references status(cods) on update cascade on delete restrict
);


CREATE OR REPLACE FUNCTION fn_log_cambios() RETURNS trigger AS $$
BEGIN
    IF TG_OP = 'INSERT' THEN
        INSERT INTO log_cambios(tabla, operacion, datos_nuevos)
        VALUES (TG_TABLE_NAME, TG_OP, row_to_json(NEW));
        RETURN NEW;
    ELSIF TG_OP = 'UPDATE' THEN
        INSERT INTO log_cambios(tabla, operacion, datos_ant, datos_nuevos)
        VALUES (TG_TABLE_NAME, TG_OP, row_to_json(OLD), row_to_json(NEW));
        RETURN NEW;
    ELSIF TG_OP = 'DELETE' THEN
        INSERT INTO log_cambios(tabla, operacion, datos_ant)
        VALUES (TG_TABLE_NAME, TG_OP, row_to_json(OLD));
        RETURN OLD;
    END IF;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_log_venta
AFTER INSERT OR UPDATE OR DELETE ON venta
FOR EACH ROW EXECUTE FUNCTION fn_log_cambios();

CREATE TRIGGER trg_log_detalleventa
AFTER INSERT OR UPDATE OR DELETE ON detalleventa
FOR EACH ROW EXECUTE FUNCTION fn_log_cambios();

CREATE TRIGGER trg_log_productos
AFTER INSERT OR UPDATE OR DELETE ON productos
FOR EACH ROW EXECUTE FUNCTION fn_log_cambios();
