from datetime import datetime
import textwrap


def exibir_menu():
    menu = """
    ================ MENU ================
    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [4]\tNovo Usuário
    [5]\tNova Conta
    [6]\tListar Contas
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


def filtrar_usuario_por_cpf(cpf, usuarios):
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            return usuario
    return None


def cadastrar_usuario(usuarios):
    cpf = input("Informe o seu CPF(somente números): ")
    if filtrar_usuario_por_cpf(cpf, usuarios):
        print("\nErro: CPF já cadastrado no sistema!")
        return
    
    nome = input("Informe o seu nome completo: ")
    data_nascimento = input("Informe a sua data de nascimento (dd/mm/aaaa): ")
    endereco = input("Informe o seu endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    novo_usuario = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    }
    usuarios.append(novo_usuario)
    print("\nUsuário cadastrado com sucesso!")


def cadastrar_conta_bancaria(contas, usuarios):
    cpf = input("Informe o CPF dp usuário para vincular a conta: ")
    usuario = filtrar_usuario_por_cpf(cpf, usuarios)

    if not usuario:
        print("\nErro: Usuário não encontrado. Cadastre o usuário antes de criar uma conta.")
        return
    
    numero_conta = len(contas) + 1
    nova_conta = {
        "agencia": "0001",
        "numero_conta": numero_conta,
        "usuario": usuario,
        "saldo": 0,
        "extrato": [],
        "numero_transacoes_hoje": 0,
        "data_ultima_transacao": datetime.now().date()
    }
    contas.append(nova_conta)
    print(f"\nConta bancária nº {numero_conta} criada com sucesso para o usuário {usuario['nome']}!")


def listar_contas(contas):
    if not contas:
        print("\nNenhuma conta cadastrada no sistema.")
        return
    
    print("\n================ LISTA DE CONTAS ================")
    for conta in contas: 
        linha = f"""
        agência:\t{conta['agencia']}
        C/C:\t\t{conta['numero_conta']}
        Titular:\t{conta['usuario']['nome']}
        """
        print(textwrap.dedent(linha))
    print("=================================================")



def main():
    LIMITE_POR_SAQUE = 500
    LIMITE_TRANSACOES_DIARIAS = 10

    usuarios = []
    contas = []


    while True:
        opcao = exibir_menu()

        if opcao == "4":
            cadastrar_usuario(usuarios)
        
        elif opcao == "5":
            cadastrar_conta_bancaria(contas, usuarios)

        elif opcao == "6":
            listar_contas(contas)

        elif opcao in ("1", "2", "3"):
            if not contas:
                print("\nNenhuma conta existe. Crie uma conta primeiro.")
                continue

            num_conta_input = int(input("Informe o número da conta: "))
            conta_selecionada = next((conta for conta in contas if conta['numero_conta'] == num_conta_input), None)

            if not conta_selecionada:
                print("\nErro: Conta não encontrada.")
                continue
            
            # Resetar limite diário de transações se o dia mudou
            if datetime.now().date() != conta_selecionada['data_ultima_transacao']:
                conta_selecionada['data_ultima_transacao'] = datetime.now().date()
                conta_selecionada['numero_transacoes_hoje'] = 0
                print("\nUm novo dia começou! Seu limite de transações para esta conta foi redefinido.")
            
            # Verificar limite de transações para depósito e saque
            if opcao in ("1", "2"):
                if conta_selecionada['numero_transacoes_hoje'] >= LIMITE_TRANSACOES_DIARIAS:
                    print("\nOperação falhou! Você excedeu o número de transações permitidas por dia para esta conta.")
                    continue
            
            if opcao == "1":
                valor = float(input("Informe o valor que deseja depositar: "))
                saldo, extrato, sucesso = depositar(conta_selecionada['saldo'], valor, conta_selecionada['extrato'])
                if sucesso:
                    conta_selecionada['saldo'] = saldo
                    conta_selecionada['extrato'] = extrato
                    conta_selecionada['numero_transacoes_hoje'] += 1
            
            elif opcao == "2":
                valor = float(input("Informe o valor que deseja sacar: "))
                saldo, extrato, sucesso = sacar(
                    saldo=conta_selecionada['saldo'],
                    valor=valor,
                    extrato=conta_selecionada['extrato'],
                    limite_por_saque=LIMITE_POR_SAQUE, 
                )
                if sucesso:
                    conta_selecionada['saldo'] = saldo
                    conta_selecionada['extrato'] = extrato
                    conta_selecionada['numero_transacoes_hoje'] += 1

            elif opcao == "3":
                exibir_extrato(conta_selecionada['saldo'], extrato=conta_selecionada['extrato'])

        elif opcao == "0":
            print("\nSaindo do sistema... Obrigado por usar nosso banco!")
            break

        else:
            print("\nOperação inválida, por favor selecione novamente a operação desejada.")


    


if __name__ == "__main__":
    main()


    


    


