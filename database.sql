CREATE TABLE art
(
  id BIGSERIAL,
  codigo character varying(100),
  descripcion character varying(100),
  tarifa1 money,
  CONSTRAINT pk_art PRIMARY KEY (id)
);

Import

COPY art(codigo,descripcion,tarifa1)
FROM '/home/jose/dev/alugandia/articulos/arttar.txt' DELIMITER '|' CSV HEADER;
