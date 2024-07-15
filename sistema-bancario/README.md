# Sistema Bancário

## 📒 Descrição
Este código é um programa de controle de conta bancária. Ele permite ao usuário depositar dinheiro, sacar dinheiro e ver o extrato das movimentações. Vamos entender cada parte dele:

1. Menu Principal
O programa começa mostrando um menu com opções:

[d] Depositar: Para adicionar dinheiro à conta.
[s] Sacar: Para retirar dinheiro da conta.
[e] Extrato: Para mostrar todas as movimentações (depósitos e saques).
[q] Sair: Para encerrar o programa.

Além das opções acima, foram acrescentadas novas opções ao menu:

[nc] Nova conta: Para criar uma nova conta
[lc] Listar contas: Para listar as contas criadas
[nu] Novo usuário: Para criar um novo usuário

----------------------------------------------------------------

2. Funções
Para organizar o código, usamos funções. Cada função faz uma tarefa específica:

mostrar_menu: Mostra o menu e pede ao usuário que escolha uma opção.
depositar: Pede ao usuário um valor para depositar. Se o valor for maior que zero, ele é adicionado ao saldo e registrado no extrato.
sacar: Pede ao usuário um valor para sacar. O programa verifica se há saldo suficiente, se o valor não ultrapassa o limite permitido e se o número de saques diários não foi excedido. Se tudo estiver certo, o valor é subtraído do saldo e registrado no extrato.
exibir_extrato: Mostra todas as movimentações registradas (depósitos e saques) e o saldo atual.

Novas funções foram adicionadas

criar_usuario: Cria usuários aptos para utilziar o sistema
filtrar_usuario: Retorna um usuário de acordo com o cpf
criar_conta: Cria uma conta no banco reutilizando alguns atributos da classe Usuario
listar_contas: Retorna uma lista com as contas já criadas.

----------------------------------------------------------------

3. Função Principal
A função main é a parte principal do programa. Ela define as variáveis iniciais, como saldo, limite de saque, extrato e número de saques. Em seguida, usa um laço (loop) para mostrar o menu e chamar as funções de acordo com a escolha do usuário.

<img src="assets/images/primeiro-codigo.png"/>
<img src="assets/images/segundo-codigo.png"/>
<img src="assets/images/terceiro-codigo.png"/>

## 🔎 Saiba Mais
- Material desenvolvido com o objetivo de concluir desafios do curso de Python na plataforma de estudos [dio.me](https://web.dio.me)
- Não contém GUI.
- Todo o código foi refatorado posteriormente aplicando conceitos de POO.

## 💻 Ferramentas utilizadas
- [Python](https://www.python.org/) - Linguagem utilizada para criação do código.
- [VS Code](https://code.visualstudio.com/) - IDE utilizada para facilitação da criação do código

## ✨ Features
- Modularização: Código dividido em funções separadas para cada operação (mostrar_menu, depositar, sacar, exibir_extrato).
- Reutilização: As funções podem ser reutilizadas facilmente em diferentes contextos.
- POO: O código foi refatorado completamente para se adequar ao paradigma de orientação a objetos em Python.
- Estrutura Principal (main): Lógica principal em uma função main e verificamos se o script está sendo executado diretamente antes de chamar main.

## 📚 Referências
- [Trilha Python DIO](https://github.com/digitalinnovationone/trilha-python-dio) - Para análise dos códigos.
