def adicionar_contato(nome, ddd , telefone):
    global id_novo_contato

    contato = {'id': id_novo_contato + 1, 'nome': nome, 'DDD': ddd, 'telefone': telefone}
    id_novo_contato += 1
    return contato

def remover_contato(id):
    index_do_contato_que_sera_removido = None

    for contato in agenda_de_contatos:
        if contato['id'] == id:
            index_do_contato_que_sera_removido = agenda_de_contatos.index(contato)
            break

    if index_do_contato_que_sera_removido != None:
        agenda_de_contatos.pop(index_do_contato_que_sera_removido)
        return True
    else:
        return False

def exibir_contatos():
    print('\nLista de contatos\n')

    for contato in agenda_de_contatos:
        print('Id: ' + str(contato['id']))
        print('Nome: ' + contato['nome'])
        print('DDD: ' + contato['DDD'])
        print('Telefone: ' + contato['telefone'] + '\n')

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
        print('4 - Sair')
        opcao = int(input('Opção: '))

        if(not (opcao >= 1 and opcao <= 4)):
            print('Opção inválida! Tente novamente.')
        elif(opcao == 1):
            nome = str(input('Nome do contato: '))
            ddd = str(input('DDD: '))
            numero_do_contato = obter_celular_ou_telefone()

            agenda_de_contatos.append(adicionar_contato(nome, ddd, numero_do_contato))
            print(f'\nContato {nome} salvo!')
        elif(opcao == 2):
            id_do_contato_que_sera_removido = int(input('Digite o id do contato: '))

            if remover_contato(id_do_contato_que_sera_removido):
                print(f'\nContato {id_do_contato_que_sera_removido} removido!')
            else:
                print(f'\nO id {id_do_contato_que_sera_removido} não foi encontrado. Tente novamente.')

        elif (opcao == 3):
            exibir_contatos()
        else:
            print('Programa encerrado.')
            exit
