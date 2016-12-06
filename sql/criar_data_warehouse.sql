DROP DATABASE IF EXISTS dw;
CREATE DATABASE dw;

CREATE TABLE IF NOT EXISTS dw.dm_local (
 id	     			INT	 NOT NULL,
 CodMunicipioGeo   	INT	 NOT NULL,
 NomeMunicipioGeo	VARCHAR(60) NOT NULL,
 CodMicroGeo    	INT	 NOT NULL,
 NomeMicroGeo  	 	VARCHAR(60) NOT NULL,
 CodMesoGeo    	 	INT      NOT NULL,
 NomeMesoGeo    	VARCHAR(60) NOT NULL,
 CodUFGeo	   		INT	 NOT NULL,	
 SiglaUFGeo	 		CHAR(2)	 NOT NULL,	
 NomeUFGeo	   		VARCHAR(20) NOT NULL,
 CodRegiaoGeo	 	INT  NOT NULL,
 RegiaoGeo	   		VARCHAR(15) NOT NULL,
 PRIMARY KEY  (id)
);

create table dw.dm_franquia(
	id int not null,
	primary key(id)
);

create table dw.dm_produto(
	id int not null,
	nome_produto varchar(100),
	primary key(id)
);

create table dw.dm_vendedor(
	id int not null,
    cpf varchar(13) not null,
	nome varchar(250),
	primary key(id)
);

create table dw.dm_tempo(
    id int not null,
    tempo date,
	ano int,
	semestre int,
	trimestre int,
	mes int,
	dia int,
	primary key(id)
);

create table dw.ft_vendas(
	id int not null auto_increment,
	id_local int,
	id_franquia int,
	id_produto  int,
	id_vendedor int,
	id_tempo int,
	qtd_produto int,
	valor_total double,
	foreign key(id_local) references dm_local(id),
	foreign key(id_franquia) references dm_franquia(id),
	foreign key(id_produto) references dm_produto(id),
	foreign key(id_vendedor) references dm_vendedor(id),
	foreign key(id_tempo) references dm_tempo(id),
	primary key(id)
    );