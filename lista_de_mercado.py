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
nome_da_primeira_lista = ''
new_list = [nome_da_primeira_lista]
invalid_input = True

# POMODORO DE HOJE (30/20, 36/20, 40/20) TOTAL: 1H:46MIN
# COLOCAR NOME NAS LISTAS
# (Paramos no nome da lista definido em string, e colocamos ele dentro de outra lista que é todas as listas precisamos)
# (definir que essa lista é um dict. e depois que conseguir fazer isso em uma função.)
# ADICIONAR E RENOMEAR UMA LISTA
# NA OPÇÃO 1 E 2, ADICIONAR AS OUTRAS LISTAS
# POSSO ADICIONAR PRODUTOS SEM TER CRIADO A LISTA PRIMEIRO?
# FUNÇÃO PARA CRIAR O NOME DA PRIMEIRA LISTA
# PRINT DA LISTA ESCOLHIDA PRECISA SER UM FOR


def criador_de_lista():
    new_list.append(nome_da_lista)
    print(new_list)


def primeiro_acesso():
    nome_da_primeira_lista = input('Escolha o nome da sua primeira lista:\n')


def start():
    if len(new_list) == 1:
        primeiro_acesso()
    opcao = int(input("""Selecione a opção que você deseja: 
        [ 1 ] - Visualizar lista 
        [ 2 ] - Adicionar/remover itens na lista
        [ 3 ] - Ver todas as listas
        [ 4 ] - Sair """))

    if opcao == 1:
        print(nome_da_primeira_lista)
        print(dict_1)
        escolha = input('Deseja voltar as opções? Pressione "S" para Sim e "N" para Não.').upper()

        if escolha == "S":
            start()

        elif escolha == "N":
            print('Finalizando programa, até mais!')
            sys.exit()

    elif opcao == 2:
        add_or_del = int(input('Deseja adicionar ou Remover produtos? ( 1 ) para Adicionar e ( 2 ) para Remover '))

        if add_or_del == 1:
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
        if len(new_list) == 1:
            print(f'Você possui um total de {len(new_list)} lista')
        else:
            print(f'Você possui um total de {len(new_list)} listas')

        print(f'Suas listas são: {new_list}')
        lista_escolhida = int(input(f"""Selecione a lista que você deseja: 
        [ 0 ] - Cria uma lista nova
        [ 1 ] - {nome_da_primeira_lista}
        [ 3 ] - 
        [ 4 ] -
        [ 5 ] - """))

        if lista_escolhida == 1:
            print(dict_1)

        elif lista_escolhida == 2:
            print(dict_2)

        elif lista_escolhida == 3:
            print(dict_3)

        elif lista_escolhida == 4:
            print(dict_4)

        elif lista_escolhida == 5:
            print(dict_5)

        elif lista_escolhida == 0:
            nome_da_lista = input('Qual nome deseja colocar na lista?:\n ')
            new_list.append(nome_da_lista)
            print(new_list)

        else:
            print('Nenhuma lista válida')

    elif opcao == 4:
        print('Finalizando programa, até mais!')
        sys.exit()


while invalid_input:
    start()
