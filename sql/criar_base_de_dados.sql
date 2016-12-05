DROP DATABASE IF EXISTS oltp;
CREATE DATABASE oltp;

create table oltp.Funcionario (
	cpf char(11) not null,
	nome varchar(250),
    primary key(cpf)
);

create table oltp.Produto(
	cod char(8)  not null,
	nome_produto varchar(100),
    valor_unidade double,
    primary key (cod)
);

create table oltp.Franquia(
	cod char(8) not null,
	estado char(2),
	cidade varchar(100),
    bairro varchar(100),
    rua varchar(100),
    numero varchar(6),
    primary key (cod)
);

create table oltp.Venda(
	id INT UNSIGNED,	
    cod_franquia char(8) not null,
	data_venda datetime,
    vendedor_cpf char(11) not null,
    primary key(id),
    foreign key (cod_franquia) references oltp.Franquia(cod),
    foreign key (vendedor_cpf) references oltp.Funcionario(cpf)
);

create table oltp.Item_venda(
	cod_produto char(8)  not null,
    id_venda INT UNSIGNED not null,
	quantidade int not null,
    valor_tabela double not null,
    valor_unitario double not null,
    primary key (id_venda,cod_produto),
	foreign key (cod_produto) references oltp.Produto(cod),
    foreign key (id_venda)   references oltp.Venda(id)
)