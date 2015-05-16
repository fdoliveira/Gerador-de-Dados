DROP DATABASE IF EXISTS topicos_especiais_database;
CREATE DATABASE topicos_especiais_database;
USE topicos_especiais_database;

create table Funcionario (
	cpf char(11) not null,
	nome varchar(250),
    primary key(cpf)
);

create table Produto(
	cod char(8)  not null,
	nome_produto varchar(100),
    valor_unidade double,
    primary key (cod)
);

create table Franquia(
	cod char(8) not null,
	estado char(2),
	cidade varchar(100),
    bairro varchar(100),
    rua varchar(100),
    numero varchar(6),
    primary key (cod)
);

create table Venda(
	id INT UNSIGNED,
	valor_total double,
    cod_franquia char(8) not null,
	data_venda datetime,
    vendedor_cpf char(11) not null,
    primary key(id),
    foreign key (cod_franquia) references Franquia(cod),
    foreign key (vendedor_cpf) references Funcionario(cpf)
);

create table Item_venda(
	cod_produto char(8)  not null,
    id_venda INT UNSIGNED not null,
	quantidade int,
    primary key (id_venda,cod_produto),
	foreign key (cod_produto) references Produto(cod),
    foreign key (id_venda)   references Venda(id)
)