import sys


print('*-' * 30)
print('{:=^60}'.format(' Lista de Compras '))
print('*-' * 30)

lista_atual = list()
todas_listas = [lista_atual]
invalid_input = True


def start():
    opcao = int(input("""Selecione a opção que você deseja: 
        [ 1 ] - Visualizar lista 
        [ 2 ] - Adicionar/remover itens na lista
        [ 3 ] - Ver todas as listas
        [ 4 ] - Sair """))

    if opcao == 1:
        print(lista_atual)
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
                produto = input('Digite o produto que deseja adicionar: (Para sair pressione "X") ').upper()

                if produto == "X":
                    start()

                else:
                    lista_atual.append(produto.capitalize())

        else:
            while True:
                produto = input('Digite o produto que deseja excluir: (Para sair pressione "X") ').upper()

                if produto == "X":
                    start()

                else:
                    lista_atual.remove(produto.capitalize())

    elif opcao == 3:
        print(f'Você possui um total de {len(todas_listas)} lista')
        print(f'Selecione as lista que deseja{lista_atual}')

    elif opcao == 4:
        print('Finalizando programa, até mais!')
        sys.exit()


while invalid_input:
    start()


