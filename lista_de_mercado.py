import sys


print('*-' * 30)
print('{:=^60}'.format(' Lista de Compras '))
print('*-' * 30)

dict_1 = dict()
dict_2 = dict()
dict_3 = dict()
dict_4 = dict()
dict_5 = dict()
all_dict = [dict_1, dict_2, dict_3, dict_4, dict_5]
nome_primeira_lista = 'Vazio'
nome_segunda_lista = 'Vazio'
nome_terceira_lista = 'Vazio'
nome_quarta_lista = 'Vazio'
nome_quinta_lista = 'Vazio'
lista_atual = None
todos_nomes_lista = [nome_primeira_lista]
invalid_input = True

# POMODORO DE HOJE (30/20, 36/20, 40/20, 50) TOTAL:
# COLOCAR NOME NAS LISTAS
# (Paramos no nome da lista definido em string, e colocamos ele dentro de outra lista que é todas as listas precisamos)
# (definir que essa lista é um dict. e depois que conseguir fazer isso em uma função.)
# ADICIONAR E RENOMEAR UMA LISTA
# NA OPÇÃO 1 E 2, ADICIONAR AS OUTRAS LISTAS
# POSSO ADICIONAR PRODUTOS SEM TER CRIADO A LISTA PRIMEIRO?
# FUNÇÃO PARA CRIAR O NOME DA PRIMEIRA LISTA
# PRINT DA LISTA ESCOLHIDA PRECISA SER UM FOR
# GUARDAR OS PRODUTOS NO ARQUIVO TXT
# FUNÇÃO PARA ADD PRODUTOS NA LISTA


def add_produtos():
    while True:
        produto = input('Digite o produto que deseja adicionar: (Para sair pressione "X") ').capitalize()

        if produto == "X":
            start()

        else:
            quantidade = int(input('Quantidade?: '))

            if nome_primeira_lista == lista_atual:
                dict_1[produto] = quantidade
                print(f'Produto {produto} adicionado com sucesso')

            elif nome_segunda_lista == lista_atual:
                dict_2[produto] = quantidade
                print(f'Produto {produto} adicionado com sucesso')
            
            elif nome_terceira_lista == lista_atual:
                dict_3[produto] = quantidade
                print(f'Produto {produto} adicionado com sucesso')
                
            elif nome_quarta_lista == lista_atual:
                dict_4[produto] = quantidade
                print(f'Produto {produto} adicionado com sucesso')
                
            elif nome_quinta_lista == lista_atual:
                dict_5[produto] = quantidade
                print(f'Produto {produto} adicionado com sucesso')

def criador_de_lista():
    new_list.append(nome_da_lista)
    print(new_list)


def primeiro_acesso():
    nome_primeira_lista = input('Escolha o nome da sua primeira lista:\n')
    return nome_primeira_lista


def start():
#    if len(new_list) == 1:
#        nome_primeira_lista = input('Escolha o nome da sua primeira lista:\n')

    opcao = int(input("""Selecione a opção que você deseja: 
        [ 1 ] - Visualizar lista 
        [ 2 ] - Adicionar/remover itens na lista
        [ 3 ] - Ver todas as listas
        [ 4 ] - Sair """))

    if opcao == 1:
        print(nome_primeira_lista)
        print(dict_1)
        escolha = input('Deseja voltar as opções? Pressione "S" para Sim e "N" para Não.').upper()

        if escolha == "S":
            start()

        elif escolha == "N":
            print('Finalizando programa, até mais!')
            sys.exit()

    elif opcao == 2:
        add_or_del = input('Deseja adicionar ou Remover produtos? ( A ) para Adicionar e ( R ) para Remover ').upper()

        if add_or_del == "A":
            while True:
                produto = input('Digite o produto que deseja adicionar: (Para sair pressione "X") ').capitalize()

                if produto == "X":
                    start()

                else:
                    quantidade = int(input('Quantidade?: '))
                    dict_1[produto] = quantidade
                    print(f'Produto {produto} adicionado com sucesso')

        else:
            while True:
                produto = input('Digite o produto que deseja excluir: (Para sair pressione "X") ').capitalize()

                if produto == "X":
                    start()

                else:
                    del dict_1[produto]
                    print(f'Produto {produto} excluido com sucesso')

    elif opcao == 3:
        if len(todos_nomes_lista) == 1:
            print(f'Você possui um total de {len(todos_nomes_lista)} lista')
        else:
            print(f'Você possui um total de {len(todos_nomes_lista)} listas')

        print(f'Suas listas são: {todos_nomes_lista}')
        lista_escolhida = int(input(f"""Selecione a lista que você deseja alterar: 
        [ 0 ] - Cria uma lista nova
        [ 1 ] - {todos_nomes_lista}"""))

        if lista_escolhida == 1:
            print(f'Pronto! Agora você está na lista {todos_nomes_lista[0]}')
            lista_atual = todos_nomes_lista[0]


        elif lista_escolhida == 2:
            print(f'Pronto! Agora você está na lista {todos_nomes_lista[1]}')
            lista_atual = todos_nomes_lista[1]

        elif lista_escolhida == 3:
            print(f'Pronto! Agora você está na lista {todos_nomes_lista[2]}')
            lista_atual = todos_nomes_lista[2]

        elif lista_escolhida == 4:
            print(f'Pronto! Agora você está na lista {todos_nomes_lista[3]}')
            lista_atual = todos_nomes_lista[3]

        elif lista_escolhida == 5:
            # if vazio print(algumacoisa)
            print(f'Pronto! Agora você está na lista {todos_nomes_lista[4]}')
            lista_atual = todos_nomes_lista[4]

        elif lista_escolhida == 0:
            nome_da_lista = input('Qual nome deseja colocar na lista?:\n ')
            todos_nomes_lista.append(nome_da_lista)
            print(todos_nomes_lista)

        else:
            print('Nenhuma lista válida')

    elif opcao == 4:
        print('Finalizando programa, até mais!')
        sys.exit()


while invalid_input:
    start()