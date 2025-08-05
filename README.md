# 🏦 Sistema Bancário Simples em Python

Bem-vindo ao projeto de Sistema Bancário Simples! Este é um sistema desenvolvido em Python puro, focado em simular as operações bancárias mais comuns de um caixa eletrônico diretamente no seu terminal. O projeto foi estruturado de forma modular e com funções bem definidas, ideal para demonstrar e praticar conceitos fundamentais da linguagem Python, como manipulação de estruturas de dados, modularização de código e lógica de programação.

## ✨ Funcionalidades Principais

O sistema permite uma experiência completa de gerenciamento de contas e transações, incluindo:

* **Gestão de Clientes**: Cadastro de novos usuários no sistema.
* **Criação de Contas**: Vinculação de contas correntes a usuários já existentes.
* **Operações Financeiras**: Realizão de depósitos e saques.
* **Controle de Transações**: Emissão de extratos detalhados.
* **Segurança e Regras de Negócio**:
    * Limite de saque por operação.
    * Limite de transações diárias.
    * Validação para evitar saques maiores que o saldo.

## 🛠️ Detalhes Técnicos e Estrutura do Código

O código é organizado em funções distintas, cada uma com uma responsabilidade única, o que torna o sistema coeso e de fácil manutenção.

### Funções Principais

#### `main()`
É a função central que executa o loop principal do programa. Ela gerencia o estado da aplicação (listas de `usuarios` e `contas`), exibe o menu de opções e orquestra a chamada das outras funções com base na escolha do usuário. É aqui que as regras de negócio, como o limite diário de transações, são verificadas antes de cada operação.

---

### Funções de Operações Bancárias

#### `depositar(saldo, valor, extrato, /)`
Responsável por adicionar fundos a uma conta.
* **Argumentos Posicionais (Positional-Only)**: Recebe `saldo`, `valor` e `extrato` como argumentos que só podem ser passados pela posição.
* **Validação**: Verifica se o `valor` do depósito é positivo.
* **Registro**: Adiciona a transação ao `extrato` com data e hora.
* **Retorno**: Devolve o novo `saldo`, o `extrato` atualizado e um booleano indicando o sucesso da operação.

#### `sacar(*, saldo, valor, extrato, limite_por_saque)`
Processa a retirada de fundos de uma conta.
* **Argumentos Nominais (Keyword-Only)**: Recebe `saldo`, `valor`, `extrato` e `limite_por_saque` como argumentos que só podem ser passados pelo nome.
* **Validações**:
    1.  Verifica se o `valor` do saque ultrapassa o saldo disponível.
    2.  Verifica se o `valor` excede o `limite_por_saque` (R$ 500,00).
    3.  Verifica se o `valor` é positivo.
* **Registro**: Adiciona a transação de saque ao `extrato`.
* **Retorno**: Devolve o `saldo` atualizado, o `extrato` e um booleano de sucesso.

#### `exibir_extrato(saldo, /, *, extrato)`
Mostra o histórico de transações e o saldo final da conta.
* **Argumentos Híbridos**: Recebe `saldo` como argumento posicional e `extrato` como nominal.
* **Funcionalidade**: Itera sobre a lista de `extrato` e exibe cada transação registrada. Caso não haja transações, uma mensagem informativa é exibida. Ao final, apresenta o saldo atual.

---

### Funções de Gerenciamento de Contas e Usuários

#### `cadastrar_usuario(usuarios)`
Adiciona um novo usuário ao sistema.
* **Validação de CPF**: Utiliza a função `filtrar_usuario_por_cpf` para garantir que o CPF informado ainda não esteja cadastrado.
* **Coleta de Dados**: Solicita nome, data de nascimento e endereço.
* **Armazenamento**: Guarda os dados do usuário em um dicionário e o adiciona à lista `usuarios`.

#### `cadastrar_conta_bancaria(contas, usuarios)`
Cria uma nova conta corrente e a associa a um usuário.
* **Requisito**: O usuário (identificado pelo CPF) já deve estar cadastrado.
* **Geração de Conta**: O número da conta é gerado sequencialmente.
* **Estrutura da Conta**: A conta é um dicionário que armazena a agência (fixa "0001"), o número da conta, os dados do usuário titular e informações para controle de transações.

#### `listar_contas(contas)`
Exibe de forma organizada todas as contas correntes cadastradas no sistema, mostrando agência, número da conta e o nome do titular.

#### `filtrar_usuario_por_cpf(cpf, usuarios)`
Uma função utilitária que busca e retorna um usuário na lista de `usuarios` com base no CPF fornecido. Retorna `None` se nenhum usuário for encontrado.

## 🚀 Como Executar

Para rodar este projeto, você precisa apenas ter o Python 3 instalado.

1.  Clone o repositório ou baixe o arquivo `teste.py`.
2.  Abra seu terminal ou prompt de comando.
3.  Navegue até o diretório onde o arquivo está localizado.
4.  Execute o seguinte comando:

```bash
python teste.py
```
5. Siga as instruções apresentadas no menu interativo.
