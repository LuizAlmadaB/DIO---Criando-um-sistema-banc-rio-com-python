menu = """
Insira a opçãp desejada

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == 'd':
        valor = float(input('Informe o valor que deseja depositar: '))
        if valor > 0:
            saldo += valor
            print('Deposótio realizado com sucesso!')
            extrato.append(f'Depósito: R$ {valor}')

        else:
            print('O valor do depósito deve ser maior que zero.')

    elif opcao == 's':
        valor = float(input('Informe o valor que deseja sacar: '))
        if valor > saldo:
            print('Operação não concluída! Você não tem saldo suficiente.')

        elif valor > limite:
            print('Operação não concluída! Valor de saque maior que o limite autorizado.')

        elif numero_saques >= LIMITE_SAQUES:
            print('Operação não concluída! Número máximo de saques já realizado!')

        elif valor > 0:
            saldo -= valor
            extrato.append((f'Saque: R$ {valor}'))
            numero_saques += 1
            print('Saque realizado com sucesso!')

        else:
            print('Operação falhou! Valor informado é inválido.')

    elif opcao == 'e':
        print('EXTRATO'.center(12, '#'))
        print("Não foram realizadas transações") if not extrato else extrato
        for operacao in extrato:
            print(operacao)

    elif opcao == 'q':
        break

    else:
        print('Operação inválida. Por favor selecione uma das opções.')