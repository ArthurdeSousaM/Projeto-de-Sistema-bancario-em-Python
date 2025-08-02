# Sistema Bancário Simples em Python

Este é um projeto de um sistema bancário básico desenvolvido em Python. O objetivo é simular as operações fundamentais de uma conta bancária, como depósito, saque e visualização de extrato, através de uma interface de linha de comando (CLI).

## 📜 Descrição

O sistema permite que o usuário interaja com uma conta bancária fictícia. Ele pode adicionar fundos, retirar dinheiro (respeitando certas regras de negócio) e consultar o histórico de transações. O projeto foi estruturado utilizando funções para cada operação, tornando o código modular e de fácil compreensão.

---

## ✨ Funcionalidades

O sistema oferece um menu com as seguintes opções:

- **[1] Depositar:** Permite ao usuário adicionar qualquer valor positivo ao saldo da conta.
- **[2] Sacar:** Permite ao usuário retirar dinheiro da conta, sujeito a três condições:
    1. O valor do saque não pode exceder o saldo disponível.
    2. O valor por saque é limitado a R$ 500,00.
    3. O usuário pode realizar no máximo 3 saques por dia.
- **[3] Extrato:** Exibe o histórico de todas as transações (depósitos e saques) realizadas e o saldo atual da conta.
- **[0] Sair:** Encerra a execução do programa.

---

## 🚀 Como Executar o Projeto

Para rodar este projeto, você precisa ter o Python instalado em seu computador.

1. Clone o repositório ou baixe os arquivos.
2. Abra um terminal na pasta onde o arquivo `sistema_banco_projeto.py` está localizado.
3. Execute o seguinte comando:

   ```bash
   python sistema_banco_projeto.py


   
4. Siga as instruções apresentadas no menu do terminal para interagir com o sistema.

🛠️ Estrutura do Código
O código é organizado nas seguintes funções para garantir clareza e manutenibilidade:

1. exibir_menu(): Imprime o menu de opções para o usuário e captura a escolha dele.

2. depositar(saldo, valor, extrato, /): Função para adicionar fundos à conta. Recebe o saldo atual, o valor a ser depositado e a lista de extrato como argumentos posicionais. Retorna o novo saldo e o extrato atualizado.

3. sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques): Função para retirar dinheiro da conta. Recebe todos os seus argumentos por nome (keyword-only). Aplica as regras de negócio (limite de valor, saldo e número de saques) antes de permitir a transação. Retorna o novo saldo, o extrato atualizado e o número de saques realizados.

4. exibir_extrato(saldo, /, *, extrato): Mostra todas as transações registradas. Recebe o saldo como argumento posicional e o extrato como argumento nomeado (keyword-only).

5. main(): Função principal que inicializa as variáveis da conta (saldo, extrato, etc.) e contém o loop principal do programa, orquestrando as chamadas para as outras funções com base na entrada do usuário.

A estrutura if __name__ == "__main__": garante que a função main() seja executada apenas quando o script é rodado diretamente.
