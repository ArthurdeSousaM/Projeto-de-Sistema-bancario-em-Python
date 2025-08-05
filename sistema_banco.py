from datetime import datetime
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
    sucesso_operacao = False 
    if valor > 0:
        saldo += valor
        timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        extrato.append(f"{timestamp}\tDepósito feito no valor de:\tR$ {valor:.2f}")
        print("\nDepósito realizado com sucesso!")
        sucesso_operacao = True
    else: 
        print("\nA operação falhou! O valor informado é inválido.")
    return saldo, extrato, sucesso_operacao


def sacar(*, saldo, valor, extrato, limite_por_saque):
    sucesso_operacao = False 
    excedeu_saldo = valor > saldo 
    excedeu_limite_valor = valor > limite_por_saque
    
    if excedeu_saldo:
        print("\nOperação falhou! Não será possivel sacar o dinheiro por falta de saldo.")
    elif excedeu_limite_valor:
        print(f"\nOperação falhou! O valor do saque excede o limite permitido de R${limite_por_saque:.2f}")    
    elif valor > 0:
        saldo -= valor 
        timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        extrato.append(f"{timestamp}\tSaque feito no valor de:\tR$ {valor:.2f}")
        print("\nSaque realizado com sucesso!")
        sucesso_operacao = True
    else: 
        print("\nOperação falhou! O valor informado é inválido.")
    return saldo, extrato, sucesso_operacao


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
    LIMITE_POR_SAQUE = 500
    LIMITE_TRANSACOES_DIARIAS = 10

    saldo = 0 
    extrato = []
    numero_transacoes = 0
    data_atual = datetime.now().date()

    while True:
        if datetime.now().date() != data_atual:
            data_atual = datetime.now().date()
            numero_transacoes = 0
            print("\nUm novo dia começou! Seu limite de transações foi redefinido.")

        opcao = exibir_menu()

        if opcao in ("1", "2"):
            if numero_transacoes >= LIMITE_TRANSACOES_DIARIAS:
                print("\nOperação falhou! Você excedeu o número de transações permitida por dia.")
                continue

        if opcao == "1":
            valor = float(input("Informe o valor que deseja depositar: "))
            saldo, extrato, sucesso = depositar(saldo, valor, extrato)
            if sucesso:
                numero_transacoes += 1
        
        elif opcao == "2":
            valor = float(input("Informe o valor que deseja sacar: "))
            saldo, extrato, sucesso = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite_por_saque=LIMITE_POR_SAQUE, 
            )
            if sucesso:
                numero_transacoes += 1

        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "0":
            print("Saindo do sistema... Obrigado por usar nosso banco!")
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


if __name__ == "__main__":
    main()


    


