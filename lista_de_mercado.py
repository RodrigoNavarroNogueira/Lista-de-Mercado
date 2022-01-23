import sys


print('*-' * 30)
print('{:=^60}'.format(' Lista de Compras '))
print('*-' * 30)


opcao = int(input("""Selecione a opção que você deseja: 
[ 1 ] - Visualizar lista 
[ 2 ] - Ver todas as listas
[ 3 ] - Adicionar/remover itens na lista
[ 4 ] - Sair"""))



lista_atual = ['banana']
todas_listas = []
produto = 0

if opcao == 1:
    print(lista_atual)
    escolha = input('Deseja voltar as opções? Pressione "S" para Sim e "N" para Não.').upper()
    if escolha == "S":
        start()

    elif escolha == "N":
        print('Finalizando programa, até mais!')
        sys.exit()

elif opcao == 2:
    print(todas_listas)

elif opcao == 3:
    produto = input('Digite o produto que deseja adicionar: ')
    lista_atual.append(produto.capitalize())
    start()

elif opcao == 4:
    print("a")



