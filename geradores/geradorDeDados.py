from random import randint
from datetime import datetime
from datetime import timedelta
import sys

class Funcionario:
    def __init__(self,nome,cpf):
        self.nome = nome
        self.cpf = cpf
        
    def __repr__(self):
        return "Nome: "+self.nome+", CPF: "+self.cpf
    
    def to_sql(self):
        return "("+'"'+self.cpf+'"'+","+'"'+self.nome+'"'+")"
    
class Produto:
    def __init__(self,cod,nome,preco):
        self.cod = cod
        self.nome = nome
        self.preco = preco
        
    def __repr__(self):
        return "Cod: "+self.cod+" ,Nome: "+self.nome+", Preco: "+str(self.preco)  
        
class Franquia:
    def __init__(self,cod,estado,cidade,bairro,rua,numero):
        self.cod = cod
        self.estado = estado
        self.cidade = cidade
        self.bairro = bairro
        self.rua = rua
        self.numero = numero
        
    def __repr__(self):
         return "Cod: "+self.cod+", Estado: " +self.estado+", Cidade: "+self.cidade+", Bairro: "+self.bairro + ", Rua: "+self.rua+", Numero: "+self.numero
class Venda:
    def __init__(self,id,franquia,data,vendedor):
        self.vendedor = vendedor
        self.valor_total = 0.0
        self.id = id
        self.franquia = franquia
        self.data = data
        self.itens_venda = []
         
    def calcularValorTotal(self):
        for item in self.itens_venda:
            self.valor_total += item.valor
            
    def __repr__(self):    
        return "Id: "+str(self.id)+", Data: "+str(self.data)+", Valor: "+str(self.valor_total)+", Cod franquia: "+self.franquia.cod+", Vendedor: "+self.vendedor.cpf
        
class ItemVenda:
     def __init__(self,venda,produto,qtd):
         self.venda = venda
         self.produto = produto
         self.qtd = qtd
         self.valor = self.produto.preco * self.qtd
     def __repr__(self):    
         return "Venda: "+self.venda.cod+", Produto: "+str(self.produto.preco)+", Valor: "+str(self.valor)
        
class GeradorDados:
    def __init__(self):
        self.estados_siglas = open('dados/estados_siglas.txt', 'r',encoding="utf-8").read().split('\n')
        self.nomes_cidades  = open('dados/nomes_cidades.txt', 'r',encoding="utf-8").read().split('\n')
        self.nomes_bairros  = open('dados/nomes_bairros.txt', 'r',encoding="utf-8").read().split('\n')
        self.nomes_ruas     = open('dados/nomes_ruas.txt', 'r',encoding="utf-8").read().split('\n')
        self.primeiro_nomes = open('dados/primeiro_nomes.txt', 'r',encoding = "utf-8").read().split('\n')
        self.segundo_nomes =  open('dados/segundo_nomes.txt', 'r',encoding = "utf-8").read().split('\n')
        self.produtos_e_precos = open('dados/produtos.txt', 'r',encoding="utf-8").read().split('\n')
        self.funcionarios = []
        self.vendas = []
        self.itens_vendas = []
        self.produtos = []
        self.franquias = []
        
    def gerarFuncionarios(self,qtd):
        self.funcionarios = []
        cpfs = gerarCPFs(qtd)
        for x in range(0,qtd):
            self.funcionarios.append(Funcionario(self.primeiro_nomes[randint(0,(len(self.primeiro_nomes))-1)]+" "+self.segundo_nomes[randint(0,(len(self.segundo_nomes))-1)],cpfs[x]))
            
    def gerarProdutos(self,qtd,tam_cod):
        if qtd > len(self.produtos_e_precos):
            raise ValueError("Quantidade de produtos deve ser menor ou igual a "+str(len(self.produtos_e_precos)))
        if qtd < 1:
            raise ValueError("Quantidade de produtos deve ser maior ou igual a 1")
        if (10**tam_cod < qtd):
            raise ValueError("Impossivel gerar "+str(qtd)+" produtos com codigo de tamanho "+str(tam_cod))
        self.produtos = []
        codigos_produtos = gerarNumeros(qtd,tam_cod)
        nomes_precos = []
        while len(nomes_precos) != qtd :
            nome_preco = self.produtos_e_precos[randint(0,len(self.produtos_e_precos)-1)].split('|')
            if  nome_preco  not in nomes_precos:
                nomes_precos.append(nome_preco)
        x = 0       
        for (nome,preco) in nomes_precos:
            self.produtos.append(Produto(codigos_produtos[x],nome,float(preco)))
            x+=1

    def gerarFranquias(self,qtd_franquias,tam_cod,qtd_estados,qtd_cidades,qtd_bairros,qtd_ruas,tamanho_numero):
        if qtd_estados > len(self.estados_siglas):
            raise ValueError("Quantidade de estados deve ser menor ou igual a "+str(len(self.estados_siglas)))
        if qtd_estados < 1:
            raise ValueError("Quantidade de estados deve ser maior ou igual a 1")
        if qtd_cidades > len(self.nomes_cidades):
            raise ValueError("Quantidade de cidades deve ser menor ou igual a "+str(len(self.nomes_cidades)))
        if qtd_cidades < 1:
            raise ValueError("Quantidade de cidades deve ser menor ou igual a 1")
        if qtd_bairros > len(self.nomes_bairros):
            raise ValueError("Quantidade de bairros deve ser menor ou igual a "+str(len(self.nomes_bairros)))
        if qtd_bairros < 1:
            raise ValueError("Quantidade de bairros deve ser menor ou igual a 1")
        if qtd_ruas > len(self.nomes_ruas):
            raise ValueError("Quantidade de ruas deve ser menor ou igual a "+str(len(self.nomes_ruas)))
        if qtd_ruas < 1:
            raise ValueError("Quantidade de ruas deve ser menor ou igual a 1")
        if (10**tam_cod < qtd_franquias):
            raise ValueError("Impossivel gerar "+str(qtd_franquias)+" franquias com codigo de tamanho "+str(tam_cod))
            
        self.franquias = []
        codigos_franquias = gerarNumeros(qtd_franquias,tam_cod)
        estados_franquias = []
        while len(estados_franquias) != qtd_estados:
            estado = self.estados_siglas[randint(0,len(self.estados_siglas)-1)]
            if estado not in estados_franquias:
                estados_franquias.append(estado)          
        cidades_franquias = []
        while len(cidades_franquias) != qtd_cidades :
            cidade = self.nomes_cidades[randint(0,len(self.nomes_cidades)-1)]
            if cidade not in cidades_franquias:
                cidades_franquias.append(cidade)
        bairros_franquias = []
        while len(bairros_franquias) != qtd_bairros :
            bairro = self.nomes_bairros[randint(0,len(self.nomes_bairros)-1)]
            if bairro not in bairros_franquias:
                bairros_franquias.append(bairro)
        ruas_franquias = []
        while len(ruas_franquias) != qtd_ruas :
            rua = self.nomes_ruas[randint(0,len(self.nomes_ruas)-1)]
            if rua not in ruas_franquias:
                ruas_franquias.append(rua)
        numeros_franquias = gerarNumeros(qtd_franquias,tamanho_numero)
        for x in range(0,qtd_franquias):
            estado =  estados_franquias[randint(0,qtd_estados-1)]
            cidade =  cidades_franquias[randint(0,qtd_cidades-1)]
            bairro =  bairros_franquias[randint(0,qtd_bairros-1)]
            rua    =  ruas_franquias[randint(0,qtd_ruas-1)]
            self.franquias.append(Franquia(codigos_franquias[x],estado,cidade,bairro,rua,numeros_franquias[x]))
            
    def gerarVendas(self,qtd,data_comeco,data_final,formato_data,probabilidades):
        soma_p = 0
        for probabilidade in probabilidades:
            soma_p += probabilidade[0]
            soma_q = 0
            if probabilidade[1] < 1:
                raise ValueError("Quantidade de itens deve ser maior ou igual a 1")
            if probabilidade[1] > len(self.produtos):
                raise ValueError("Impossivel gerar "+str(probabilidade[1])+" itens por venda com "+
                                 str(len(self.produtos))+" produtos")
            for probabilidade_qtds in probabilidade[2]:
                soma_q += probabilidade_qtds[0]
                if probabilidade_qtds[1] < 1:
                    raise ValueError("Quantidade de produtos deve ser maior ou igual a 1")
            if soma_q != 100:
                raise ValueError("Soma das probabilidade deve ser igual a 100")
        if soma_p != 100:
             raise ValueError("Soma das probabilidade deve ser igual a 100")
        self.vendas = []
        comeco = datetime.strptime(data_comeco,formato_data)
        fim = datetime.strptime(data_final,formato_data)
        for x in range(0,qtd):
            data = getDataAleatoria(comeco,fim)
            franquia = self.franquias[randint(0,len(self.franquias)-1)]
            vendedor = self.funcionarios[randint(0,len(self.funcionarios)-1)]
            venda = Venda(x,franquia,data,vendedor)  
            index = getIndex(probabilidades,100)
            quantidade_itens = probabilidades[index][1]
            produtos_escolhidos = []
            for x in range (0,quantidade_itens):
                index_2 = getIndex(probabilidades[index][2],100)
                quantidade_produto = probabilidades[index][2][index_2][1]
                produto = self.produtos[randint(0,len(self.produtos)-1)]
                while produto in produtos_escolhidos:
                    produto = self.produtos[randint(0,len(self.produtos)-1)]
                produtos_escolhidos.append(produto)
                item_venda = ItemVenda(venda,produto,quantidade_produto)
                self.itens_vendas.append(item_venda)
                venda.itens_venda.append(item_venda)
            venda.calcularValorTotal()
            self.vendas.append(venda)
            
    def getMediaVendas(self):
        total = 0
        for venda in self.vendas:
            total += venda.valor_total
        return total/len(self.vendas)
    
    def gerarArquivoSQL(self):
        c = '("'
        c2 = '('
        s = '","'
        s2 ='",'
        s3 =',"'
        s4 = ','
        f =  '"),\n'
        f2 = '");\n'
        f3 =  '),\n'
        f4 = ');\n'
        formatodata = '"%Y-%m-%d %H:%i:%S"'
        arquivo = open('sql/popular_database.sql', 'w',encoding="utf8")
        arquivo.write("insert into Funcionario(cpf,nome) values \n")
        for x in range(0,len(self.funcionarios)-1):
            funcionario = self.funcionarios[x]
            arquivo.write(c+funcionario.cpf+s+funcionario.nome+f)
        x+=1
        funcionario = self.funcionarios[x]
        arquivo.write(c+funcionario.cpf+s+funcionario.nome+f2)
        arquivo.write("\n")
        arquivo.write("insert into Produto(cod,nome_produto,valor_unidade) values \n")
        for x in range(0,len(self.produtos)-1):
            produto = self.produtos[x]
            arquivo.write(c+produto.cod+s+produto.nome+s2+str(produto.preco)+f3)
        x+=1
        produto = self.produtos[x]
        arquivo.write(c+produto.cod+s+produto.nome+s2+str(produto.preco)+f4)
        arquivo.write("\n")
        arquivo.write("insert into Franquia(cod,estado,cidade,bairro,rua,numero) values \n")
        for x in range(0,len(self.franquias)-1):
            franquia = self.franquias[x]
            arquivo.write(c+franquia.cod+s+franquia.estado+s+franquia.cidade+s+
                          franquia.bairro+s+franquia.rua+s+franquia.numero+f)
        x+=1
        franquia = self.franquias[x]
        arquivo.write(c+franquia.cod+s+franquia.estado+s+franquia.cidade+s+
                          franquia.bairro+s+franquia.rua+s+franquia.numero+f2)
        arquivo.write("\n")
        arquivo.write("insert into Venda(id,valor_total,cod_franquia,data_venda,vendedor_cpf) values \n")
        for x in range(0,len(self.vendas)-1):
            venda = self.vendas[x]
            cod_franquia = venda.franquia.cod
            data = venda.data
            string_data = '",''str_to_date("'+str(data)+'",'+formatodata+')'+','+'"'
            valor_venda = "{0:.2f}".format(venda.valor_total)
            arquivo.write(c2+str(venda.id)+s4+valor_venda+s3+cod_franquia+string_data+venda.vendedor.cpf+f)
        x+=1
        venda = self.vendas[x]
        cod_franquia = venda.franquia.cod
        data = venda.data
        string_data = '",''str_to_date("'+str(data)+'",'+formatodata+')'+','+'"'
        valor_venda = "{0:.2f}".format(venda.valor_total)
        arquivo.write(c2+str(venda.id)+s4+valor_venda+s3+cod_franquia+string_data+venda.vendedor.cpf+f2)
        arquivo.write("\n")
        arquivo.write("insert into Item_venda(cod_produto,id_venda,quantidade) values \n")
        for x in range(0,len(self.itens_vendas)-1):
            item_venda = self.itens_vendas[x]
            arquivo.write(c+item_venda.produto.cod+s2+str(item_venda.venda.id)+s4+str(item_venda.qtd)+f3)
        x+=1
        item_venda  = self.itens_vendas[x]
        arquivo.write(c+item_venda.produto.cod+s2+str(item_venda.venda.id)+s4+str(item_venda.qtd)+f4)
        arquivo.close()

        
def getIndex(probabilidades,total):
    x = 0
    soma = 0
    limite = randint(0,total-1)
    if limite == 0:
        x +=1
    while x < len(probabilidades) and soma < limite:
        soma += probabilidades[x][0]
        x+=1
    x-=1
    return x

def gerarCPF():
    cpf = []
    for x in range(9):
      cpf.append(randint(0,9) )
    soma = 0
    for x in reversed(range(2,11)):
        soma += cpf[10-x]*x
    digitov1 = (soma * 10) % 11
    if (digitov1) > 9:
        digitov1 = 0;
    cpf.append(digitov1)
    soma = 0
    for x in reversed(range(2,12)):
        soma += cpf[11-x]*x
    digitov2 = (soma * 10) % 11
    if (digitov2) > 9:
        digitov2 = 0;
    cpf.append(digitov2)
    scpf = ''.join(str(v) for v in cpf)
    return scpf

def gerarCPFs(qtd):
    cpfs = []
    while len(cpfs) <= qtd:
        cpf = gerarCPF()
        if cpf not in cpfs:
            cpfs.append(cpf)
    return cpfs

def gerarNumeros(qtd,tamanho):
    numeros = []
    while len(numeros) < qtd:
        numero = ""
        for x in range (0,tamanho):
            numero = numero + str(randint(0,9))
        if numero not in numeros:
            numeros.append(numero)
    return numeros

def getDataAleatoria(comeco, fim):
    return comeco + timedelta(seconds=randint(0, int((fim - comeco).total_seconds())))

