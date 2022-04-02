# start point do programa
def novoContato(nome, ddd , telefone):
    global id_novo_contato

    contato = {'id': id_novo_contato + 1, 'nome': nome, 'DDD': ddd, 'telefone': telefone}
    id_novo_contato += 1
    return contato

def obter_celular_ou_telefone():
    numero_do_contato = input('Número do contato:')
    while numero_do_contato != 8 or 9:
        print(f'Número invalido, tente novamente!!')
        numero_do_contato = input('Número do contato:')
    return numero_do_contato
    
# Starpoint Programa 
if __name__ == 'main':
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
            ddd = int(input('DDD:'))
            numero_de_telefone = obter_celular_ou_telefone()
            


            agenda_de_contatos.append(novoContato(nome,ddd,  numero_de_telefone))
            print(f'contato {nome} adicionado!!')

        elif(opcao == 2):
            print('Código de remover contato aqui')

        elif (opcao == 3):
            print('Código de mostrar contatos')


        else:
            print('Programa encerrado.')
            exit
