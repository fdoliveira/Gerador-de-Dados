DROP DATABASE IF EXISTS topicos_especiais_data_warehouse;
CREATE DATABASE topicos_especiais_data_warehouse;
USE topicos_especiais_data_warehouse;

create table local(
	id varchar(202),
	estado char(2),
	cidade varchar(100),
	bairro varchar(100),
	unique(estado,cidade,bairro),
	primary key(id)
);

create table franquia(
	cod char(8) not null,
	primary key(cod)
);

create table produto(
	cod char(8) not null,
	nome_produto varchar(100),
	primary key(cod)
);

create table vendedor(
	cpf char(11) not null,
	nome varchar(250),
	primary key(cpf)
);

create table tempo(
    id date not null,
	ano int,
	semestre int,
	trimestre int,
	mes int,
	dia int,
	primary key(id)
);

create table vendas(
	id int(11) not null auto_increment,
	id_local varchar(202),
	id_franquia char(8),
	id_produto  char(8) ,
	id_vendedor char(11),
	id_tempo date,
	qtd_produto int,
	valor_total double,
	foreign key(id_local) references local(id),
	foreign key(id_franquia) references franquia(cod),
	foreign key(id_produto) references produto(cod),
	foreign key(id_vendedor) references vendedor(cpf),
	foreign key(id_tempo) references tempo(id),
	primary key(id)
		
);