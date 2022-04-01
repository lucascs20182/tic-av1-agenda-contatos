# start point do programa
def novoContato(nome, telefone):
    global id_novo_contato
    
    contato = {'id': id_novo_contato + 1, 'nome': nome, 'telefone': telefone}
    id_novo_contato += 1
    
    return contato

if __name__ == '__main__':
    global id_novo_contato
    id_novo_contato = 0
    agenda_de_contatos = []
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
            nome = str(input('Nome do contato:'))
            telefone = input('Número do contato:')

            agenda_de_contatos.append(novoContato(nome, telefone))
            print(f'contato {nome} adicionado!!')

        elif(opcao == 2):
            print('Código de remover contato aqui')

        elif (opcao == 3):
            print('Código de mostrar contatos aqui')

        else:
            print('Programa encerrado.')
            exit
