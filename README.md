# 🏦 Sistema de Simulação Bancária em Python 🐍

### 📋 Descrição do Projeto

Este script é uma aplicação de linha de comando (CLI) desenvolvida em Python que simula as operações transacionais de um sistema bancário. O programa foi estruturado de forma modular, com funções distintas para cada operação principal, e gerencia o estado da aplicação em memória durante sua execução. O objetivo é demonstrar conceitos de programação como manipulação de estado, fluxo de controle, modularidade com funções e o uso de bibliotecas padrão como `datetime` para registro de tempo e `textwrap` para formatação de texto.

---

### ✨ Funcionalidades e Regras Implementadas

O script executa três operações principais, governadas por um conjunto de regras de negócio:

* **Depósito:** Adiciona um valor ao saldo. A operação só é concluída se o valor informado for positivo.
* **Saque:** Subtrai um valor do saldo. A operação está sujeita às seguintes validações sequenciais:
    1.  O valor do saque não pode ser superior ao saldo atual.
    2.  O valor do saque não pode exceder o limite fixo de R$ 500,00, definido pela constante `LIMITE_POR_SAQUE`.
    3.  O valor do saque deve ser positivo.
* **Extrato:** Exibe o histórico de todas as transações bem-sucedidas (depósitos e saques) e o saldo final.
* **Controle de Transações:** Existe um limite de 10 transações diárias (`LIMITE_TRANSACOES_DIARIAS`). Este contador é reiniciado automaticamente quando a data do sistema muda.

---

### 🚀 Execução

Para executar o programa, utilize um interpretador Python em um terminal:

```bash
python teste.py
```

### 🛠️ Análise da Arquitetura do Código
A lógica do programa é segmentada em funções, cada uma com uma responsabilidade bem definida.

### ▶️ main()

1. Função: Atua como o ponto de entrada e o controlador principal do fluxo da aplicação.

2. Gerenciamento de Estado: Inicializa e mantém as variáveis que representam o estado da aplicação: saldo, extrato (uma lista de strings), numero_transacoes e data_atual.

3. Loop de Execução: Contém o loop principal (while True) que mantém o programa em execução, aguardando a entrada do usuário.

4. Lógica de Controle:

   - Verifica a data do sistema no início de cada iteração para resetar o contador numero_transacoes.

   - Invoca a função exibir_menu() para obter a entrada do usuário.

   - Utiliza uma estrutura condicional (if/elif/else) para rotear o comando do usuário para a função apropriada.

   - Atualiza as variáveis de estado com os valores retornados pelas funções de transação.

### 🧾 exibir_menu()

1. Função: Responsável exclusivamente pela interface com o usuário.

2. Implementação: Imprime um bloco de texto formatado (utilizando textwrap.dedent) no console e captura a entrada do usuário via input(), retornando o valor como uma string.

### ➕ depositar(saldo, valor, extrato, /)

1. Função: Processa a lógica de depósito.

2. Assinatura: Utiliza argumentos posicionais (/), exigindo que os parâmetros sejam passados na ordem correta, sem nomeação.

3. Implementação:

   - Valida se o valor é positivo.

   - Se a validação for bem-sucedida, o saldo é incrementado.

   - Uma string formatada, contendo um timestamp gerado por datetime.now(), é adicionada à lista extrato.

   - Retorna uma tupla contendo o novo saldo, o extrato atualizado e um booleano (True) indicando o sucesso da operação.

### ➖ sacar(*, saldo, valor, extrato, limite_por_saque)

1. Função: Processa a lógica de saque.

2. Assinatura: Utiliza argumentos nomeados (*), exigindo que os parâmetros sejam passados utilizando seus respectivos nomes (ex: saldo=...).

3. Implementação:

   - Executa uma cadeia de validações na ordem de precedência definida.

   - Se qualquer validação falhar, a função imprime uma mensagem de erro e termina sua execução.

   - Se todas as validações passarem, o saldo é decrementado e o registro da transação (com timestamp) é adicionado ao 
     extrato.

   - Retorna uma tupla com o saldo atualizado, o extrato e um booleano de sucesso.

### 📄 exibir_extrato(saldo, /, *, extrato)

1. Função: Responsável pela formatação e exibição do histórico de transações e do saldo.

2. Assinatura: Combina argumentos posicionais (saldo) e nomeados (extrato).

3. Implementação:

   - Imprime um cabeçalho para o extrato.

   - Itera sobre a lista extrato, imprimindo cada string de transação.

   - Caso a lista esteja vazia, exibe uma mensagem indicando a ausência de movimentações.

   - Ao final, imprime o valor da variável saldo recebida.
