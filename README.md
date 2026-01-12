#Jogo Pedra, Papel e Tesoura (Versão Multiplayer)

##Sobre o Projeto

Este projeto foi desenvolvido como um exercício prático do curso da Data Science Academy (DSA). O objetivo principal foi exercitar a *lógica de algoritmos, uso de variáveis, estruturas condicionais e funções de entrada e saída de dados*.

Este código foi estruturado *antes* de consultar a resolução do instrutor, focando em criar uma solução robusta e com uma *boa experiência* para o usuário.

##Diferenciais Técnicos e Implementações

Diferente de implementações básicas, este script traz recursos avançados de usabilidade e tratamento de dados:

* **Validação com Funções e Loops**: Criei uma função específica para validar a entrada dos jogadores, garantindo que o programa não quebre caso o usuário digite algo inesperado. O loop `while True` só permite o avanço do jogo após uma entrada válida.

* **Tratamento de Strings**: Utilizei os métodos `.lower()` e `.strip()` para garantir que o *sistema aceite* entradas com letras maiúsculas ou espaços acidentais, melhorando a experiência do usuário (UX).

* **Feedback Personalizado**: O sistema identifica exatamente *qual jogador* inseriu uma entrada inválida, facilitando a correção durante a partida.

* **Lógica de Empate**: O jogo reinicia automaticamente em caso de empate, mantendo o *fluxo contínuo* até que haja um vencedor definido.

##Aprendizados Consolidados

* **Estruturação de algoritmos independentes**.

* **Manipulação de listas e operadores de pertinência** (`in / not in`).

* **Escopo de variáveis dentro e fora de funções**.
