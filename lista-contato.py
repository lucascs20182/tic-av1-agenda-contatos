def novo_contato(nome, ddd , telefone):
    global id_novo_contato

    contato = {'id': id_novo_contato + 1, 'nome': nome, 'DDD': ddd, 'telefone': telefone}
    id_novo_contato += 1
    return contato



def obter_celular_ou_telefone():
    numero_do_contato = str(input('Número do contato: '))

    while not is_numero_do_contato_valido(numero_do_contato):
        print(f'Número inválido, tente novamente!')
        numero_do_contato = str(input('Número do contato: '))

    return numero_do_contato



def is_numero_do_contato_valido(numero_do_contato):
    return len(numero_do_contato) != 8 or len(numero_do_contato) != 9



def formatar_numero_do_contato(numero_do_contato):
    numero_do_contato_formatado = ''

    if len(numero_do_contato) == 8:
        numero_do_contato_formatado = f'{numero_do_contato[0:4]}-{numero_do_contato[4:8]}'

    if len(numero_do_contato) == 9:
        numero_do_contato_formatado = f'{numero_do_contato[0:5]}-{numero_do_contato[5:9]}'

    return numero_do_contato_formatado



# start point do programa
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
            nome = str(input('Nome do contato: '))
            ddd = str(input('DDD: '))
            numero_do_contato = obter_celular_ou_telefone()

            agenda_de_contatos.append(novo_contato(nome, ddd, numero_do_contato))
            print(f'contato {nome} salvo!')
        elif(opcao == 2):
            print('Código de remover contato aqui')
        elif (opcao == 3):
            print('Código de mostrar contatos')
        else:
            print('Programa encerrado.')
            exit
