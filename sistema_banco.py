import textwrap

def exibir_menu():
    menu = """
    ================ MENU ================
    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [0]\tSair
    """

    print(textwrap.dedent(menu))
    return input("Digite a opção desejada: ")


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito no valor de:\tR$ {valor:.2f}")
        print("\nDepósito realizado com sucesso!")
    else: 
        print("\nA operação falhou! O valor informado é inválido.")
    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo 
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\nNão será possivel sacar o dinheiro por falta de saldo.")
    elif excedeu_limite:
        print(f"\nOperação falhou! O valor do saque excede o limite permitido de R${limite:.2f}")
    elif excedeu_saques:
        print("\nOperação falhou! Número máximo de saques diários atingidos.")
    elif valor > 0:
        saldo -= valor 
        extrato.append(f"Saque no valor de:\tR$ {valor:.2f}")
        numero_saques += 1
        print("\nSaque realizado com sucesso!")
    else: 
        print("\nOperação falhou! O valor informado é inválido.")
    return saldo, extrato, numero_saques


def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else: 
        for transacao in extrato:
            print(transacao)
    print(f"\nO seu saldo atual é de:\tR$ {saldo:.2f}")
    print("==========================================")


def main():
    LIMITE_SAQUES = 3
    LIMITE_POR_SAQUE = 500

    saldo = 0 
    extrato = []
    numero_saques = 0

    while True:
        opcao = exibir_menu()

        if opcao == "1":
            valor = float(input("Informe o valor que deseja depositar: "))
            saldo, extrato = depositar(saldo, valor, extrato)
        
        elif opcao == "2":
            valor = float(input("Informe o valor que deseja sacar: "))
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=LIMITE_POR_SAQUE,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES, 
            )

        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "0":
            print("Saindo do sistema... Obrigado por usar nosso banco!")
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


if __name__ == "__main__":
    main()


    

