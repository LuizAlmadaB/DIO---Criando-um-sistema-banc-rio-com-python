import datetime
import textwrap


formato_horario = '%d-%m-%Y %H:%M'
horario_transacao = datetime.datetime.strftime(datetime.datetime.now(), formato_horario)

def menu():

    menu = f"""\n
    Insira a opçãp desejada

    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [lu]\tListar usuário
    [q]\tSair
    => """

    return input(textwrap.dedent(menu))


def depositar(saldo, valor, extrato, numero_transacao, /):
    if valor > 0:
        saldo += valor
        extrato.append(f'{horario_transacao} - Depósito: R$ {valor}')
        numero_transacao += 1
        print('Deposótio realizado com sucesso!')
    else:
        print('O valor do depósito deve ser maior que zero.')

    return saldo, extrato, numero_transacao

def sacar(*, saldo, valor, extrato, limite, numero_transacao, limite_saque):
    saldo -= valor
    extrato.append((f'{horario_transacao} - Saque: R$ {valor}'))
    numero_transacao += 1
    print('Saque realizado com sucesso!')

    return saldo, extrato, numero_transacao

def exibir_extrato(saldo,/, extrato):
    print('EXTRATO'.center(12, '#'))
    print("Não foram realizadas transações") if not extrato else extrato
    for operacao in extrato:
        print(f'{operacao}')
    print(f'Saldo: {saldo}')

def cadastrar_usuario(clientes):
    cpf = input('Informe o CPF do cliente (somente números): '.replace('.', '').replace('-', '').replace('/', ''))
    if cpf in clientes['CPF']:
        print("Cliente já cadastrado!")
        return

    nome = input('Insira o nome do cliente: ')
    data_nascimento = input('Insira a data de nascimento do cliente (dd-mm-aaaa): ')
    endereco = input('Insira o endereço do cliente (logradouro, nro - bairro - cidade/UF): ')

    clientes.update({'CPF': cpf, 'nome': nome ,'data_nascimento': data_nascimento, 'endereco': endereco})

    return cpf, nome, data_nascimento, endereco

    print('Cliente cadastrado com sucesso!')

def listar_usuaruio(clientes):
    CPF = input('Insira o CPF do cliente: ')
    if CPF in clientes['CPF']:
        print(clientes)
    else:
        print('Cliente não cadastrado')

def criar_conta(agencia, numero_conta, clientes):
    CPF = input('Informe o CPF do cliente: ')
    if CPF in clientes['CPF']:
        print('\n Conta criada com sucesso')
        return {'agencia': agencia, 'numero_conta': numero_conta, 'cliente': clientes}

    print('\n Cliente não encontrado, realizar o cadastro primeiro.')

def listar_contas(contas):
    if len(contas) == 0:
        print('Não há contas cadastradas')
    else:
        for conta in contas:
            linha = f'''
            Agência: \t{conta['agencia']}
            C/C: \t{conta['numero_conta']}
            Titular: \t{conta['cliente']['nome']}
            '''
            print(textwrap.dedent(linha))


def main():
    saldo = 0
    limite = 500
    extrato = []
    numero_transacao = 0
    LIMITE_TRANSACAO = 10
    AGENCIA = '0001'
    clientes = {'CPF': '', 'nome': '', 'data_nascimento': '', 'endereco': '' }
    contas = []
    while True:
        opcao = menu()

        if opcao == 'nu':
            cadastrar_usuario(clientes)

        if opcao == 'd':
            valor = float(input('Informe o valor que deseja depositar: '))
            if numero_transacao >= LIMITE_TRANSACAO:
                print('Operação não concluída! Número máximo de transações já realizado!')
            else:
                saldo, extrato, numero_transacao = depositar(saldo, valor, extrato, numero_transacao)
                print(numero_transacao)

        elif opcao == 's':
            valor = float(input('Informe o valor que deseja sacar: '))
            if valor > saldo:
                print('Operação não concluída! Você não tem saldo suficiente.')
            elif valor > limite:
                print('Operação não concluída! Valor de saque maior que o limite autorizado.')
            elif numero_transacao >= LIMITE_TRANSACAO:
                print('Operação não concluída! Número máximo de transações já realizado!')
            elif valor > 0:
                saldo, extrato, numero_transacao = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_transacao=numero_transacao,
                      limite_saque=LIMITE_TRANSACAO)
                print(numero_transacao)
            else:
                print('Operação falhou! Valor informado é inválido.')

        elif opcao == 'lu':
            listar_usuaruio(clientes)

        elif opcao == 'nc':
            numero_conta = len(contas) + 1
            contas.append(criar_conta(AGENCIA, numero_conta, clientes))


        elif opcao == 'e':
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == 'lc':
            listar_contas(contas)

        elif opcao == 'q':
            break

    else:
        print('Operação inválida. Por favor selecione uma das opções.')


main()