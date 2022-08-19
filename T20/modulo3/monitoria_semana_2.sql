/*
	Entidade Aluno:
	
	id_aluno
	nome_aluno
	matricula_aluno
	genero_aluno
	cpf_aluno
	idade_aluno
*/

CREATE TABLE aluno(
	id_aluno integer PRIMARY KEY,
	nome_aluno varchar(255) ,
	matricula_aluno bigint ,
	genero_aluno char(50),
	cpf_aluno varchar(255)
);

/*
	Comando para apagar tabela: 
		DROP TABLE aluno;
	Comando para criar uma nova coluna na tabela: 
		ALTER TABLE aluno ADD idade_aluno integer;
	Comando para remover uma coluna da tabela: 
		ALTER TABLE aluno DROP COLUMN idade_aluno;
	Comando para alterar o tipo de uma coluna: 
		ALTER TABLE aluno ALTER COLUMN id_aluno TYPE bigint;
	Comando para renomear coluna: 
		ALTER TABLE aluno RENAME COLUMN matricula_aluno TO matricula;
*/

-- Inserção de dados em tabela
INSERT INTO aluno(id_aluno, nome_aluno)
VALUES(1, 'Diego Sousa');

INSERT INTO aluno(id_aluno)
VALUES(2);

-- Seleção de dados em tabela
SELECT * FROM aluno;








