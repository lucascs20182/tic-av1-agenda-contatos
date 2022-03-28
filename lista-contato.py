# start point do programa
if __name__ == '__main__':
    opcao = 0

    while(opcao != 4):
        print('\nMenu')
        print('1 - Inserir contato')
        print('2 - Remover contato')
        print('3 - Mostrar contatos')
        print('4 - Sair\n')
        opcao = int(input('Opção: '))

        if(not (opcao >= 1 and opcao <= 4)):
            print('Opção inválida! Tente novamente.')
        elif(opcao == 1):
            print('Código de cadastro de contato aqui')
        elif(opcao == 2):
            print('Código de remover contato aqui')
        elif(opcao == 3):
            print('Código de mostrar contato aqui')
        else:
            print('Programa encerrado.')
            exit
