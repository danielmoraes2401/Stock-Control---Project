"""++++++++++++++++++++++++++++++++++++++++++++++++++++                                 PROJETO P1                          +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"""

#função data e hora
def dataHorario():
    '''Usada para importar biblioteca datetime edeterminar a data e o horário exato em outras funções.'''
    from datetime import datetime
    HorarioAtual = datetime.now()
    HorarioEmTexto = HorarioAtual.strftime('%d/%m/%Y %H:%M')
    return HorarioEmTexto

#função eliminando barraEne
def eliminaBarraEne(string):
    '''Usada para remover os \n's dos arquivos usados no programa'''
    stringNova = ""
    for caractere in string:
        if caractere != "\n":
            stringNova += caractere
    return stringNova

#função relatorio
def relatorio():
    '''Usada enviar dados dos elementos para o relatorio.csv'''
    listaElementos = list(elementos.values())
    import csv
    with open('relatorio.csv', 'w', newline='') as csvfile:
        tabela = csv.writer(csvfile, delimiter = ',')
        tabela.writerow(['CÓDIGO','PRODUTO','MARCA','QUANT.','DATA CRIAÇÃO PRODUTO','DATA MODIFICAÇÃO PRODUTO'])
        cont = 0
        for codigo in elementos:   
            tabela.writerow([f'{codigo}',f'{listaElementos[cont][0]}',f'{listaElementos[cont][1]}',f'{listaElementos[cont][2]}',f'{listaElementos[cont][3]}',f'{listaElementos[cont][4]}'])
            cont+=1
        print('\n<<RELATÓRIO GERADO COM SUCESSO>>\n')
        fraseLog = (f'<<< Às {dataHorario()} um RELATÓRIO foi gerado >>>')
        log.append(fraseLog)

# função para criptografar
def criptografar(nome):
    '''Usada para criptografar o dicionários de elementos do programa'''
    arq = open('chavePublica.txt', 'r')
    e = int(eliminaBarraEne(arq.readline()))
    n = int(arq.readline())
    arq.close()
    nomeCript = ''
    for caracter in nome:
        nomeCript += str((ord(caracter)**e)%n)
        nomeCript += ' '
    return nomeCript
    
# funcao para descriptografar
def descriptografar(nome):
    '''Usada para descriptografar o arquivo de elementos do programa'''
    arq = open('chavePrivada.txt','r')
    d = int(eliminaBarraEne(arq.readline()))
    n = int(arq.readline())
    arq.close()
   
    numero = ''
    lista = []
    for caracter in nome:
        if caracter != ' ':
            numero += caracter
        else:
            lista.append(numero)
            numero = ''
    palavra = ''        
    for caracter in lista:
        conversor = (int(caracter)**d)%n
        palavra += chr(conversor)
    return palavra

#função menu
def menu():
    '''Usada para chamar o menu principal e inicial do programa'''
    print()
    print('!'*2,'LOJÃO GAMES','!'*2,'')
    print('1 - LOGIN\n2 - FECHAR\n3 - RELATÓRIO')
    paradaMenu = True
    while paradaMenu:
        opcao = input('Digite a opção referente: ')
        if opcao == '1':
            paradaMenu = False
            entrarLogin(usuarios)
            menuTela = False
        elif opcao == '2':
            paradaMenu = False
            menuTela = False
        elif opcao == '3':
            paradaMenu = False
            relatorio()
            menu()
            menuTela = False
        else:
            print('\n<<OPÇÃO INVÁLIDA>>\n')
    return menuTela

#função ler arquivoLOG
def lerArquivoLog():
    '''Função utilizada para ler o arquivo: 'log.txt' e colocar as informação dentro de uma lista'''
    listaLog = []
    arq = open("log.txt", "r")
    linhas = arq.readlines()
    arq.close()
    qtdeLog = len(linhas)
    cont=0
    while(cont < qtdeLog):
        log = eliminaBarraEne(str(linhas[1*cont])) 
        listaLog.append(log)
        cont+=1
    return listaLog

#função escreveArquivoLog
def escreverArquivoLog(lista):
    '''Função utilizada para escrever o arquivo: 'log.txt',  mas com as informações atualizadas a partir da entrada de um usuário no programa'''
    arq = open("log.txt", "w")
    for frase in lista:
        arq.write(str(frase)+ '\n')  
    arq.close()

#função vendedor
def funcaoVendedor(elementos,cpfLogin):
    '''Usada para chamar a única função do vendedor no controle de estoque da loja'''
    paradaFuncaoVendedor = True
    while paradaFuncaoVendedor:
        print('''
1- PROCURAR PRODUTO
---------------------
2- VENDA DE PRODUTO
---------------------''')
        opcao = input('Digite o número referente à tabela: ')
        if opcao == '1':
            procurarProduto(elementos,cpfLogin)
            paradaFuncaoVendedor = False
        elif opcao == '2':
            venderProduto(elementos,cpfLogin)
            paradaFuncaoVendedor = False                       
        else:
            print('\n<<NÚMERO INVÁLIDO>>')

    
#função para a tabela do vendedor
def tabelaVendedor(elementos,cpfLogin):
    '''Usada para verificar se o usuário necessita fazer outra operação ou sair pro menu inicial'''
    print('<<MENU VENDEDOR>>')
    funcaoVendedor(elementos,cpfLogin)
    paradaTabela = True
    while paradaTabela:
        print('1 - TABELA NOVAMENTE\n2 - SAIR PRO MENU\n')
        tabela = input('Digite o número referente a opção desejada: ')
        if tabela == '1':
            funcaoVendedor(elementos,cpfLogin)
        elif tabela == '2':
            paradaTabela = False
            fraseLog = (f'<<< O usuário de CPF: {cpfLogin} às {dataHorario()} fez o LOGOUT >>>')
            log.append(fraseLog)
            menu()               
        else:
            print('\n<<NÚMERO INVÁLIDO>>\n')

#função subGerente
def funcaoSubGerente(elementos,cpfLogin):
    '''Usada para chamar as funções do sub-gerente no controle de estoque da loja'''
    paradaFuncaoSubGerente = True
    while paradaFuncaoSubGerente:
        print("""
1-ATUALIZAR PRODUTO
-------------------------------------
2-REMOVER PRODUTO
-------------------------------------
3-ADICIONAR PRODUTO
-------------------------------------
4-ORDENAR BANCO DE DADOS DOS PRODUTOS
-------------------------------------""")
        opcao = input('Digite o número referente à tabela: ')
        if opcao == '1':
            alterarQuantidade(elementos,cpfLogin)
            paradaFuncaoSubGerente = False            
        elif opcao == '2':
            removerElementos(elementos,cpfLogin)
            paradaFuncaoSubGerente = False
        elif opcao == '3':
            cadastrarElementos(elementos,cpfLogin)
            paradaFuncaoSubGerente = False
        elif opcao == '4':
            ordenarElementos(elementos,cpfLogin)
            paradaFuncaoSubGerente = False            
        else:
            print('\n<<NÚMERO INVÁLIDO>>')

#funcao chamando tabela subGerente
def tabelaSubGerente(elementos,cpfLogin):
    '''Usada para verificar se o usuário necessita fazer outra operação ou sair pro menu inicial'''
    print('<<MENU SUB-GERENTE>>')
    funcaoSubGerente(elementos,cpfLogin)
    paradaTabela = True
    while paradaTabela:
        print('1 - TABELA NOVAMENTE\n2 - SAIR PRO MENU \n')
        tabela = input('Digite o número referente a opção desejada: ')
        if tabela == '1':
            funcaoSubGerente(elementos,cpfLogin)
        elif tabela == '2':
            paradaTabela = False
            fraseLog = (f'<<< O usuário de CPF: {cpfLogin} às {dataHorario()} fez o LOGOUT >>>')
            log.append(fraseLog)
            menu()                        
        else:
            print('\n<<NÚMERO INVÁLIDO>>\n')

#funcao menu gerente
def funcaoGerente(usuarios,cpfLogin):
    '''Usada para chamar as funções do gerente no controle de estoque da loja'''
    paradaFuncaoGerente = True
    while paradaFuncaoGerente:
        print('''
1- CADASTRAR USUÁRIO
---------------------
2- REMOVER USUÁRIO
---------------------
3- PROMOVER USUÁRIO
---------------------''')
        opcao = input('Digite o número referente à tabela: ')
        if opcao == '1':
            cadastrarUsuario(usuarios,cpfLogin)
            paradaFuncaoGerente = False
        elif opcao == '2':
            removerUsuarios(usuarios,cpfLogin)
            paradaFuncaoGerente = False
        elif opcao == '3':
            promoverUsuario(usuarios,cpfLogin)
            paradaFuncaoGerente = False                        
        else:
            print('\n<<NÚMERO INVÁLIDO>>')

#função chamando tabela gerente
def tabelaGerente(usuarios,cpfLogin):
    '''Usada para verificar se o usuário necessita fazer outra operação ou sair pro menu inicial'''
    print('<<MENU GERENTE>>')
    funcaoGerente(usuarios,cpfLogin)
    paradaTabela = True
    while paradaTabela:
        print('1 - IR PARA A TABELA\n2 - SAIR PRO MENU\n')
        tabela = input('Digite o número referente a opção desejada: ')
        if tabela == '1':
            funcaoGerente(usuarios,cpfLogin)
        elif tabela == '2':
            paradaTabela = False
            fraseLog = (f'<<< O usuário de CPF: {cpfLogin} às {dataHorario()} fez o LOGOUT >>>')
            log.append(fraseLog)
            menu()
        else:
            print('\n<<NÚMERO INVÁLIDO>>\n')

#funcao para entrar no login
def entrarLogin(dicionario):
    '''Função utilizada para aprovar o login de um usuário ao tentar entrar no programa'''
    cont = 0
    loginTela = True
    while loginTela:
        print('\n<< LOGIN >>\n1 - VENDEDOR\n2 - SUB-GERENTE\n3 - GERENTE\n4 - MENU\n')
        loginOpcao = input('Digite a opção desejada: ')
        if loginOpcao == '1':
            cpfExistente = False
            while cpfExistente == False:    
                cpfLogin = input('\nCPF: ')
                if cpfLogin in usuarios and dicionario[cpfLogin][1] == 'VENDEDOR':
                    cpfExistente = True
                    cont = 1
                else:
                    print('\n<< CPF NÃO CADASTRADO >>\n')
                    perg = input('''Deseja repetir o CPF?
-- Digite 'N' para voltar pro login --
-- Digite qualquer outra tecla pra repetir --

Opção: ''').lower()
                    if perg == 'n':
                        entrarLogin(usuarios)
                        cpfExistente = True
                                
            senhaCorreta = False
            while senhaCorreta == False and cont == 1:
                senhaLogin = input('SENHA: ')
                print()
                if senhaLogin in usuarios[cpfLogin]:
                    senhaCorreta = True
                    fraseLog = (f'<<< O usuário de CPF: {cpfLogin} às {dataHorario()} ENTROU atráves de um LOGIN >>>')
                    log.append(fraseLog)
                    tabelaVendedor(elementos,cpfLogin)
                    
                else:
                    print('<< SENHA INVÁLIDA >>\n')
                    perg = input('''Deseja repetir a SENHA?
-- Digite 'N' para voltar pro login --
-- Digite qualquer outra tecla pra repetir --

Opção: ''').lower()
                    if perg == 'n':
                        entrarLogin(usuarios)
                        senhaCorreta = True
            loginTela = False
                                       
        elif loginOpcao == '2':
            cpfExistente = False
            while cpfExistente == False:    
                cpfLogin = input('\nCPF: ')
                if cpfLogin in usuarios and dicionario[cpfLogin][1] == 'SUB-GERENTE':
                    cpfExistente = True
                    cont = 1

                else:
                    print('\n<< CPF NÃO CADASTRADO >>\n')
                    perg = input('''Deseja repetir o CPF?
-- Digite 'N' para voltar pro login --
-- Digite qualquer outra tecla pra repetir --

Opção: ''').lower()
                    if perg == 'n':
                        entrarLogin(usuarios)
                        cpfExistente = True
                            
            senhaCorreta = False
            while senhaCorreta == False and cont == 1:
                senhaLogin = input('SENHA: ')
                print()
                if senhaLogin in usuarios[cpfLogin]:
                    senhaCorreta = True
                    fraseLog = (f'<<< O usuário de CPF: {cpfLogin} às {dataHorario()} ENTROU atráves de um LOGIN >>>')
                    log.append(fraseLog)
                    tabelaSubGerente(elementos,cpfLogin)

                else:
                    print('<< SENHA INVÁLIDA >>\n')
                    perg = input('''Deseja repetir a SENHA?
-- Digite 'N' para voltar pro login --
-- Digite qualquer outra tecla pra repetir --

Opção: ''').lower()
                    if perg == 'n':
                        entrarLogin(usuarios)
                        senhaCorreta = True
            loginTela = False                        

        elif loginOpcao == '3':
            cpfExistente = False
            while cpfExistente == False:    
                cpfLogin = input('\nCPF: ')
                if cpfLogin in usuarios and dicionario[cpfLogin][1] == 'GERENTE':
                    cpfExistente = True
                    cont = 1

                else:
                    print('\n<< CPF NÃO CADASTRADO >>\n')
                    perg = input('''Deseja repetir o CPF?
-- Digite 'N' para voltar pro login --
-- Digite qualquer outra tecla pra repetir --

Opção: ''').lower()
                    if perg == 'n':
                        entrarLogin(usuarios)
                        cpfExistente = True

            senhaCorreta = False
            while senhaCorreta == False and cont == 1:
                senhaLogin = input('SENHA: ')
                print()
                if senhaLogin in usuarios[cpfLogin ]:
                    senhaCorreta = True
                    fraseLog = (f'<<< O usuário de CPF: {cpfLogin} às {dataHorario()} ENTROU atráves de um LOGIN >>>')
                    log.append(fraseLog)
                    tabelaGerente(usuarios,cpfLogin)

                else:
                    print('<< SENHA INVÁLIDA >>\n')
                    perg = input('''Deseja repetir a SENHA?
-- Digite 'N' para voltar pro login --
-- Digite qualquer outra tecla pra repetir --

Opção: ''').lower()
                    if perg == 'n':
                        entrarLogin(usuarios)
                        senhaCorreta = True
            loginTela = False
                                                                
        elif loginOpcao == '4':
            loginTela = False
            menu()
        else:
            print('\n<<NÚMERO INVÁLIDO>>')

#lendo arquivo Elementos.txt
def lerArquivoElementos():
    '''Função utilizada para ler o arquivo: 'elementos.txt' e colocar as informação dentro de um dicionário'''
    elementos = {}
    arq = open("elementos.txt", "r")
    linhas = arq.readlines()
    arq.close()
    qtdesElementosCadastrados = len(linhas)//6
    cont=0
    while(cont < qtdesElementosCadastrados):
        codigo = descriptografar(eliminaBarraEne(linhas[6*cont]))
        produto = descriptografar(eliminaBarraEne(linhas[6*cont+1]))
        marca = descriptografar(eliminaBarraEne(linhas[6*cont+2]))
        quantidade = descriptografar(eliminaBarraEne(linhas[6*cont+3]))
        dataCriaçao = descriptografar(eliminaBarraEne(linhas[6*cont+4]))
        dataModificaçao = descriptografar(eliminaBarraEne(linhas[6*cont+5]))
        tuplaElementos = (produto, marca, quantidade, dataCriaçao, dataModificaçao) 
        elementos[codigo] = tuplaElementos
        cont+=1
    return elementos

#procurando elemenentos
def procurarProduto(dicionario,cpfLogin):
    '''Função usada para procurar algum produto da empresa, função que apenas atraves do login de um VENDEDOR é executada'''
    cont = 0
    buscaProduto = input('\nDigite o código do produto: ')
    for (chave,(produto, marca, quantidade, dataCriaçao, dataModificaçao)) in dicionario.items():
        if buscaProduto == chave:
            if quantidade == '0':
                print('\nEM FALTA!\n')
                fraseLog = (f'<<< O usuário de CPF: {cpfLogin} às {dataHorario()} PROCUROU o produto de código: {buscaProduto} >>>')
                log.append(fraseLog)
            else:
                print(f'\nTemos {quantidade} unidade(s) de {produto} da marca {marca}.\n')
                cont+=1
            fraseLog = (f'<<< O usuário de CPF: {cpfLogin} às {dataHorario()} PROCUROU o produto de código: {buscaProduto} >>>')
            log.append(fraseLog)
    if cont == 0:
        print('\n << PRODUTO INEXISTENTE >>\n')
        fraseLog = (f'<<< O usuário de CPF: {cpfLogin} às {dataHorario()} TENTOU PROCURAR um produto INEXISTENTE >>>')
        log.append(fraseLog)

#funcao venda de produto
def venderProduto(dicionario,cpfLogin):
    '''Função usada para diminuir a quantidade de algum produto da empresa, função que apenas atraves do login de um LOGIN é executada'''
    cont = 0
    codigo = input('\nDigite o código do produto: ')
    for (chave,(produto, marca, quantidade, dataCriaçao, dataModificaçao)) in dicionario.items():
        if codigo == chave:
            vendas = input('Digite a quantidade de vendas: ')
            dataModificaçao = dataHorario()   
            quantidade = int(quantidade)- int(vendas)
            dicionario[codigo] = (produto, marca, str(quantidade), dataCriaçao, dataModificaçao)
            fraseLog = (f'<<< O usuário de CPF: {cpfLogin} às {dataHorario()} anunciou a VENDA de {vendas} unidade(s) do produto de código: {codigo} >>>')
            log.append(fraseLog)
            print('\n!!QUANTIDADE ALTERADA!!\n')  
            cont +=1
    if cont == 0:
        print('<< \n CÓDIGO INEXISTENTE >>\n')
        fraseLog = (f'<<< O usuário de CPF: {cpfLogin} às {dataHorario()} TENTOU mudar a quantidade de um produto INEXISTENTE >>>')
        log.append(fraseLog)

#cadastrando elementos
def cadastrarElementos(dicionario,cpfLogin):
    '''Função usada para cadastrar algum produto da empresa, função que apenas atraves do login de um SUB-GERENTE é executada'''
    codigo = input("\ndigite o código do produto: ")
    if codigo not in dicionario:
        produto = input("digite o nome do produto: ").upper()
        marca = input("digite a marca do produto: ").upper()
        quantidade = input('digite a quantidade desses produto: ')
        dataCriaçao = dataHorario()
        dataModificaçao = '-'
        tuplaElementos = (produto, marca, quantidade, dataCriaçao, dataModificaçao)
        dicionario[codigo] = tuplaElementos
        print('\n<< PRODUTO CADASTRADO >> \n')
        fraseLog = (f'<<< O usuário de CPF: {cpfLogin} às {dataHorario()} CADASTROU um produto de codigo:{codigo} >>>')
        log.append(fraseLog)
    else:
        print('\n<< PRODUTO JÁ CADASTRADO >>\n')
        fraseLog = (f'<<< O usuário de CPF: {cpfLogin} às {dataHorario()} TENTOU CADASTRAR um produto JÁ EXISTENTE >>>')
        log.append(fraseLog)

#removendo elementos
def removerElementos(dicionario,cpfLogin):
    '''Função usada para remover algum produto da empresa, função que apenas atraves do login de um SUB-GERENTE é executada'''
    buscar = input('\nDigite o código do produto: ')
    cont = 0
    if buscar in dicionario:
        cont+=1
    if cont == 0:
        print('\n<< CÓDIGO INEXISTENTE >>\n')
        fraseLog = (f'<<< O usuário de CPF: {cpfLogin} às {dataHorario()} TENTOU REMOVER um produto INEXISTENTE >>>')
        log.append(fraseLog)
    else:
        fraseLog = (f'<<< O usuário de CPF: {cpfLogin} às {dataHorario()} REMOVEU um produto de código: {buscar} >>>')
        log.append(fraseLog)
        del dicionario[buscar]
        print('\n!!REMOVIDO COM SUCESSO!!\n')

#atualizar quantidade elemento
def alterarQuantidade(dicionario,cpfLogin):
    '''Função usada para alterar a quantidade de algum produto da empresa, função que apenas atraves do login de um SUB-GERENTE é executada'''
    cont = 0
    codigo = input('\nDigite o código do produto: ')
    for (chave,(produto, marca, quantidade, dataCriaçao, dataModificaçao)) in dicionario.items():
        if codigo == chave:
            troca = input('Digite a nova quantidade: ')
            dataModificaçao = dataHorario()   
            dicionario[codigo] = (produto, marca, troca, dataCriaçao, dataModificaçao)
            fraseLog = (f'<<< O usuário de CPF: {cpfLogin} às {dataHorario()} ALTEROU a quantidade do produto de código: {codigo} >>>')
            log.append(fraseLog)
            print('\n!!ALTERAÇÃO REALIZADA!!\n')  
            cont +=1
    if cont == 0:
        print('\n<< CÓDIGO INEXISTENTE >>\n')
        fraseLog = (f'<<< O usuário de CPF: {cpfLogin} às {dataHorario()} TENTOU ALTERAR um produto INEXISTENTE >>>')
        log.append(fraseLog)

#ordenar dicionario de elementos pela quantidade
def ordenarElementos(dicionario,cpfLogin):
    '''Função usada para ordenar produtos da empresa com base na quantidade restante, função que apenas atraves do login de um SUB-GERENTE é executada'''
    lista = []
    for chave in dicionario:
        tupla = (int(dicionario[chave][2]),chave)
        lista.append(tupla)

    tamLista = len(lista)
    for i in range(tamLista):
        troca = False
        for j in range(1,tamLista-i):
            if lista[j][0] < lista[j-1][0]:
                lista[j], lista[j-1] = lista[j-1], lista[j]
                troca = True
        if not troca:
            break
    print()
    for (codigo,quant) in lista:
        print(f'O produto de código {quant} tem {codigo} unidade(s).')
    print()

    fraseLog = (f'<<< O usuário de CPF: {cpfLogin} às {dataHorario()} ORDENOU os produtos da loja >>>')
    log.append(fraseLog)

#reescrevendo o arquivo Elementos
def escreverArquivoElementos(dicionario):
    '''Função utilizada para escrever o arquivo: 'elementos.txt',  mas com as informações atualizadas a partir da entrada de um usuário no programa'''
    arq = open("elementos.txt", "w")
    listaValores = list(dicionario.values())
    cont = 0
    for codigo in dicionario:
        arq.write(str(criptografar(codigo))+'\n')
        arq.write(str(criptografar(listaValores[cont][0]))+'\n')
        arq.write(str(criptografar(listaValores[cont][1]))+'\n')
        arq.write(str(criptografar(listaValores[cont][2]))+'\n')
        arq.write(str(criptografar(listaValores[cont][3]))+'\n')
        arq.write(str(criptografar(listaValores[cont][4]))+'\n')
        cont+=1    
    arq.close()

#lendo arquivo usuarios.txt
def lerArquivoUsuarios():
    '''Função usada para ler o arquivo: 'usuarios.txt' e assim saber quais usuários são permitidos entrar no programa'''
    usuarios = {}
    arq = open("usuarios.txt", "r")
    linhas = arq.readlines()
    arq.close()
    qtdesUsuariosCadastrados = len(linhas)//3
    cont=0
    while(cont < qtdesUsuariosCadastrados):
        cpf = eliminaBarraEne(linhas[3*cont])
        senha = eliminaBarraEne(linhas[3*cont+1])
        funcao = eliminaBarraEne(linhas[3*cont+2])
        tuplaUsuario = (senha, funcao)
        usuarios[cpf] = tuplaUsuario
        cont+=1
    return usuarios

#promover usuario
def promoverUsuario(dicionario,cpfLogin):
    '''Função usada para promover algum usuário da empresa, função que apenas atraves do login de um GERENTE é executada''' 
    cont = 0
    cpf = input('\ndigite o CPF que deseja promover: ')
    for (chave,(senha,funcao)) in dicionario.items():
        if cpf == chave and funcao == 'VENDEDOR':
            novaFuncao = 'SUB-GERENTE'   
            dicionario[cpf] = (senha, novaFuncao)
            print('\n!!ALTERAÇÃO REALIZADA!!\n')
            fraseLog = (f'<<< O usuário de CPF: {cpfLogin} às {dataHorario()} PROMOVEU um usuário de CPF: {cpf} >>>')
            log.append(fraseLog)
            cont +=1                     
        elif cpf == chave and funcao == 'SUB-GERENTE':
            novaFuncao = 'GERENTE'   
            dicionario[cpf] = (senha, novaFuncao)
            print('\n!!ALTERAÇÃO REALIZADA!!\n')
            fraseLog = (f'<<< O usuário de CPF: {cpfLogin} às {dataHorario()} PROMOVER um usuário de CPF: {cpf} >>>')
            log.append(fraseLog)
            cont +=1
    if cont == 0:
        print('\n<< PROMOÇÃO INVÁLIDA >>\n')
        fraseLog = (f'<<< O usuário de CPF: {cpfLogin} às {dataHorario()} TENTOU PROMOVER um usuário INEXISTENTE de CPF: {cpf} >>>')
        log.append(fraseLog)

#cadastrando usuarios
def cadastrarUsuario(dicionario,cpfLogin):
    '''Função usada para cadastrar algum usuário da empresa, função que apenas atraves do login de um GERENTE é executada'''
    cpf = input("\ndigite o CPF: ")
    if cpf not in dicionario:
        senha = input("digite a senha: ")
        paradaFuncao = True
        while paradaFuncao:
            funcao = input("digite sua função: ").upper()
            if funcao == 'VENDEDOR' or funcao == 'GERENTE' or funcao == 'SUB-GERENTE':
                paradaFuncao = False
                print('\n!!REALIZADO COM SUCESSO!!\n')
                fraseLog = (f'<<< O usuário de CPF: {cpfLogin} às {dataHorario()} CADASTROU um usuário de CPF: {cpf} >>>')
                log.append(fraseLog)
            else:
                print('\n << FUNÇÃO INEXISTENTE >>\n')
        tuplaUsuario = (senha, funcao)
        dicionario[cpf] = tuplaUsuario
    else:
        print('\n<< CPF JÁ CADASTRADO >>\n')
        fraseLog = (f'<<< O usuário de CPF: {cpfLogin} às {dataHorario()} TENTOU CADASTRAR um usuário JÁ EXISTENTE >>>')
        log.append(fraseLog)
        
#removendo usuarios
def removerUsuarios(dicionario,cpfLogin):
    '''Função usada para remover algum usuário da empresa, função que apenas atraves do login de um GERENTE é executada'''
    buscar = input('\nDigite o CPF: ')
    cont = 0
    if buscar in dicionario:
        if buscar == cpfLogin:
            cont = 2
        else:
            cont = 1
    if cont == 0:
        print('\n<< CPF INEXISTENTE >>\n')
        fraseLog = (f'<<< O usuário de CPF: {cpfLogin} às {dataHorario()} TENTOU REMOVER um usuário INEXISTENTE >>>')
        log.append(fraseLog)
    elif cont == 2:
        print('\n << VOCÊ NÃO PODE SE REMOVER >> \n')
    else:
        fraseLog = (f'<<< O usuário de CPF: {cpfLogin} às {dataHorario()} REMOVEU um usuário de CPF: {buscar} >>>')
        log.append(fraseLog)
        del dicionario[buscar]

        print('\n!!REMOVIDO COM SUCESSO!!\n')

#reescrevendo o arquivo Usuarios.txt
def escreverArquivoUsuarios(dicionario):
    '''Função que escreve o arquivo: 'usuarios.txt' novamente, mas com as informações atualizadas a partir da entrada de um usuário no programa'''
    arq = open("usuarios.txt", "w")
    listaValores = list(dicionario.values())
    cont = 0
    for cpf in dicionario:
        arq.write(str(cpf)+'\n')
        arq.write(str(listaValores[cont][0])+'\n')
        arq.write(str(listaValores[cont][1])+'\n')
        cont+=1
    arq.close()

#Fluxo Principal
usuarios = lerArquivoUsuarios()
elementos = lerArquivoElementos()
log = lerArquivoLog()

menuTela = True
while menuTela:
    menuTela = menu()
 
escreverArquivoUsuarios(usuarios)
escreverArquivoElementos(elementos)
escreverArquivoLog(log)












































        



