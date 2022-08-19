-- Script criação de um banco de dados
--CREATE DATABASE nome_do_banco;

-- Script de criação de tabelas
/*CREATE TABLE nome_da_tabela(
	atributo1 tipo_do_atributo,
	atributo2 tipo_do_atributo,
	...
	atributon tipo_do_atributo
);*/

-- Criação de um banco de cinema
CREATE TABLE ator(
	id_ator integer PRIMARY KEY,
	nome_ator varchar(255),
	idade_ator integer,
	cache_ator numeric(10,2)
);

CREATE TABLE filme(
	id_filme integer PRIMARY KEY,
	nome_filme varchar(255),
	genero_filme varchar(255),
	diretor_filme varchar(255),
	ano_filme integer,
	id_ator integer,
	FOREIGN KEY (id_ator) REFERENCES ator (id_ator)
);

-- Qual comando utilizaria para alterar o tipo do genero_filme de varchar para char?
/*
	ALTER TABLE nome_da_tabela
	OPERACAO ...
*/

ALTER TABLE filme
ALTER COLUMN genero_filme TYPE char(100);

ALTER TABLE filme
ALTER COLUMN ano_filme TYPE bigint;

ALTER TABLE ator
ADD COLUMN cpf_ator char(14);

ALTER TABLE ator
RENAME COLUMN cache_ator TO cachee;

ALTER TABLE ator
DROP COLUMN cpf_ator;

-- Excluir tabela que outra possui dependência
DROP TABLE ator CASCADE;

DROP TABLE filme;

-- Seleção
SELECT * FROM ator;

-- Inserção
/* INSERT INTO nome_da_tabela(coluna1, coluna2, coluna3)
   VALUES (valor1, valor2, valor3)
*/
INSERT INTO ator(id_ator, nome_ator, idade_ator, cache_ator)
VALUES (1, 'Diego Sousa', 18, 10000);

-- Update
/*
	UPDATE nome_da_tabela set coluna_valor_alterado = novo_valor 
	where condição
*/
UPDATE ator
SET idade_ator = 20
WHERE id_ator = 1

--------------------------------------------------------------------------------------
/* 16/08/2022 */
/*
	CRUD
	C -> Create = operação INSERT
	R -> Read = operação SELECT
	U -> Update = operação UPDATE
	D -> Delete = operação DELETE
*/

-- Select com where
SELECT * FROM ator WHERE cache_ator > 10000 and idade_ator > 18;

-- Insert
INSERT INTO ator(id_ator, nome_ator, idade_ator, cache_ator)
VALUES (2, 'Matheus Barbosa', 20, 20000);

INSERT INTO ator(id_ator, nome_ator)
VALUES (3, 'Camilla Sampaio');

INSERT INTO ator
VALUES(4, 'Patrick', 40, 30000);

INSERT INTO ator
VALUES(5, 'Jaqueline Damasceno', 18);

INSERT INTO ator
VALUES(6, 'Laura Camargo', 30000);

INSERT INTO ator(id_ator, nome_ator, cache_ator)
VALUES(7, 'João Victor', 30000);

-- Update
UPDATE ator
SET idade_ator = 20
WHERE id_ator = 3;

UPDATE ator
SET idade_ator = 19, cache_ator = 20000
WHERE id_ator = 3;

-- Delete
Delete FROM ator where id_ator IN (5,6)

-- Outros selects
Select * from ator order by id_ator desc

-- Delete usando subquery
delete from ator where id_ator IN(
select min(id_ator) from ator)

select avg(cache_ator) from ator

select nome_ator from ator where nome_ator LIKE '%C%' OR nome_ator LIKE '%c%'

-- 17/08/2022
select * from pizzaria.tb_pedido

select tipo_entrega, count(id_pedido) from pizzaria.tb_pedido
group by tipo_entrega;


select * from pizzaria.tb_pizza;

-- Qual a quantidade de pizzas por categoria?
select categoria, count(id_pizza) from pizzaria.tb_pizza
group by categoria;


select categoria, count(id_pizza) from pizzaria.tb_pizza
group by categoria
having count(id_pizza) > 4;

-- Exemplos de JOIN

-- Left join
select distinct  tc.id_cliente, nome from pizzaria.tb_cliente tc
left join pizzaria.tb_pedido tp on tp.id_cliente = tc.id_cliente
where tp.id_cliente is not null

-- Validação LEFT JOIN
select * from pizzaria.tb_pedido where id_cliente IN (13,14,15)

-- Right Join
select distinct nome from pizzaria.tb_cliente tc
right join pizzaria.tb_pedido tp on tc.id_cliente = tp.id_cliente

-- Outer join
select * from pizzaria.tb_cliente tc
full outer join pizzaria.tb_pedido tp on tp.id_cliente = tc.id_cliente

-- Inner join
select distinct tc.nome from pizzaria.tb_cliente tc
inner join pizzaria.tb_pedido tp on tp.id_cliente = tc.id_cliente


select * from pizzaria.tb_pedido_pizza tpp
inner join pizzaria.tb_pedido tp on tp.id_pedido = tpp.id_pedido
inner join pizzaria.tb_pizza tpi on tpi.id_pizza = tpp.id_pizza


-- Subselect
select nome from pizzaria.tb_cliente where id_cliente
                                               in (select id_cliente from pizzaria.tb_pedido)


---
--18/08/2022
select * from pizzaria.tb_pizza;


--avg, count, sum, min, max, etc
/*select coluna_categorica, funcao_matematica(coluna) from tabela
group by coluna_categorica;*/

-- Escreva um comando SQL que retorne a quantidade de pizzas por categoria
select categoria, count(preco) from pizzaria.tb_pizza
group by categoria;

select categoria, avg(preco) from pizzaria.tb_pizza
group by categoria
having avg(preco) > 50;


select distinct categoria from pizzaria.tb_pizza

/*
select colunas... from tabelas...
where condicao IN (select valor from tabela where condicao)
*/

-- Escreva uma consulta SQL que retorne todos os clientes
-- clientes que fizeram pedidos usando subquery

-- Subquery
select * from pizzaria.tb_cliente where id_cliente IN (

select distinct id_cliente from pizzaria.tb_pedido)


--
select * from pizzaria.tb_pizza

select categoria, count(preco) from pizzaria.tb_pizza
where preco > 60
group by categoria;


select categoria, count(preco) from pizzaria.tb_pizza
group by categoria
having count(preco) > 5;




where campo_data between '2000-01-01' and '2000-02-01'