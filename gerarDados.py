from geradores.geradorDeDados import GeradorDados

if __name__ == '__main__':
    print("Gerando dados")
    '''criar gerador de dados'''
    geradorDados = GeradorDados()
    
    '''gerar Funcionarios'''
    #quantidade de funcionario que serão gerados
    quantidade_funcionarios = 100
    geradorDados.gerarFuncionarios(quantidade_funcionarios)

    '''gerar Produtos'''
    #quantidade de produtos que serão gerados
    quantidade_produtos = 20
    #tamanho do codigo dos produtos
    tamanho_cod_produtos = 8
    geradorDados.gerarProdutos(quantidade_produtos,tamanho_cod_produtos)
    
    '''gerar Franquias'''
    #numero de franquias que serão geradas
    quantidade_franquias = 10
    #tamanho do codigo das franquias
    tamanho_cod_franquias = 8
    #tamanho do subconjunto de estados de onde os estados das franquias serão escolhidos
    quantidade_estados_franquias = 4
    #tamanho do subconjunto de cidades de onde as cidades das franquias serão escolhidas
    quantidade_cidades_franquias = 10
    #tamanho do subconjunto de bairros de onde os bairros das franquias serão escolhidos
    quantidade_bairros_franquias = 10
    #tamanho do subconjunto de ruas de onde as ruas das franquias serão escolhidas
    quantidade_ruas_franquias = 10
    #tamanho do numero dos enderecos das franquias
    tamanho_numero_franquias = 6
    
    geradorDados.gerarFranquias(quantidade_franquias,
                                tamanho_cod_franquias,
                                quantidade_estados_franquias,
                                quantidade_cidades_franquias,
                                quantidade_bairros_franquias,
                                quantidade_ruas_franquias,
                                tamanho_numero_franquias)
    '''gerar Vendas'''
    #quantiade de vendas que serão gerada
    qtd_vendas = 10000
    #data minima das vendas
    data_inicial = '14/12/2014 13:00'
    #data maxima das vendas
    data_final = '14/12/2015 13:00'
    #formato da data
    formato_data = '%d/%m/%Y %H:%M'
    
    probabilidades = []
    """
    15% de chance de ter 1 item de venda por venda,
    A cada item de venda 80% de chance de a quantidade de produtos ser 1, 15% de ser 2 e 5% de ser 1
    """
    probabilidades.append((15,1,((80,1),(15,2),(5,1))))
    """
    25% de chance de ter 2 itens de venda por venda,
    A cada item de venda 80% de chance de a quantidade de produtos ser 1, 15% de ser 2 e 5% de ser 1
    """
    probabilidades.append((25,2,((80,1),(15,2),(5,1))))
    """
    50% de chance de ter 3 itens de venda por venda,
    A cada item de venda 80% de chance de a quantidade de produtos ser 1, 15% de ser 2 e 5% de ser 1
    """
    probabilidades.append((50,3,((80,1),(15,2),(5,1))))
    """
    10% de chance de ter 4 itens de venda por venda,
    A cada item de venda 80% de chance de a quantidade de produtos ser 1, 15% de ser 2 e 5% de ser 1
    """
    probabilidades.append((10,4,((80,1),(15,2),(5,1))))
    geradorDados.gerarVendas(qtd_vendas,data_inicial,data_final,formato_data,probabilidades)
    ''' Gerar Arquivo .sql'''
    geradorDados.gerarArquivoSQL()
    
    print("Dados gerados")
