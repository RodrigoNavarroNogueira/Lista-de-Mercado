import sys


def dicionario_um():
    global dict_1
    dict_1 = dict()


def nome_da_primeira_lista():
    global nome_primeira_lista
    nome_primeira_lista = input('Escolha o nome da sua lista:\n').capitalize()


def visualizador_de_listas():
    print(nome_primeira_lista)
    if dict_1 == {}:
        print('A lista está vazia')
    else:
        print(dict_1)
        start()


def add_produtos():
    while True:
        produto = input('Digite o produto que deseja adicionar: (Para sair pressione "X") ').capitalize()

        if produto == "X":
            start()

        else:
            quantidade = int(input('Quantidade?: '))

            dict_1[produto] = quantidade
            print(f'Produto {produto} adicionado com sucesso')


dicionario_um()
nome_da_primeira_lista()

print('*-' * 30)
print('{:=^60}'.format(' Lista de Compras '))
print('*-' * 30)

invalid_input = True
def start():
    opcao = int(input("""Selecione a opção que você deseja: 
        [ 1 ] - Visualizar lista 
        [ 2 ] - Adicionar/remover itens na lista
        [ 3 ] - Fechar o programa\n\n"""))

    if opcao == 1:
        visualizador_de_listas()

    elif opcao == 2:
        add_or_del = input('Deseja adicionar ou Remover produtos? ( A ) para Adicionar e ( R ) para Remover ').upper()

        if add_or_del == "A":
            add_produtos()

        else:
            while True:
                produto = input('Digite o produto que deseja excluir: (Para sair pressione "X") ').capitalize()

                if produto == "X":
                    start()

                else:
                    del dict_1[produto]
                    print(f'Produto {produto} excluido com sucesso')

    elif opcao == 3:
        print('Finalizando programa, até mais!')
        sys.exit()



while invalid_input:
    start()
