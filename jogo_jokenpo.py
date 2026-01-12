#Criação de lista para a validação da entrada do usuário
entrada_valida = ["pedra", "papel", "tesoura"]

#Declaração das possibilidades
sit1 = "pedra > tesoura"
sit2 = "papel > pedra"
sit3 = "tesoura > papel"

#Impressão do nome do jogo
print("****** JOGO DE PEDRA, PAPEL E TESOURA ******")

#Variáveis para armazenamento dos nomes do usuário
nome1 = input("Jogador 1, coloque seu nome: ")
nome2 = input("Jogador 2, coloque seu nome: ")

#Definição da função para valiidação de entrada
#O parâmentro 'nome_do_jogador' indica para a máquina que ela receberá esse valor quando eu começar a rodar ela
def validaEntrada(nome_do_jogador):
    
    while True:#Loop para continuar rodando o input até obter uma entrada válida

        escolhat = input(f"{nome_do_jogador}, digite sua escolha (pedra/papel/tesoura): ").lower().strip() #Uso de funções para as palavras ficarem todas minúsculas e sem espaços
        if escolhat not in entrada_valida:
                print(f"Entrada inválida! Tente novamente!")
        else:
                return escolhat #O valor que a função vai retornar para mim da variável 'escolhat' que só existe dentro da função
            
   
#O objetivo do loop são os seguintes passos:
#Chamar a função para validação e armazenamento das escolhas nas variáveis
#Comparação das escolhas dos jogadores
#Condições de comparação para determianr vitória
#Quando há a vitória o loop pára
#Quando chega no empate o loop reinicia para o passo 1
while True:
    jogador1 = validaEntrada(nome1)
    jogador2 = validaEntrada(nome2)
    escolha = f"{jogador1} > {jogador2}"
    if escolha == sit1:
        print(f"\n O Jogador 1 venceu!! \n Escolha do(a) {nome1}: {jogador1} \n Escolha do(a) {nome2}: {jogador2}")
        break
            
    elif escolha == sit2:
        print(f"\n O Jogador 1 venceu!! \n Escolha do(a) {nome1}: {jogador1} \n Escolha do(a) {nome2}: {jogador2}")
        break
        
    elif escolha == sit3:
        print(f"\n O Jogador 1 venceu!! \n Escolha do(a) {nome1}: {jogador1} \n Escolha do(a) {nome2}: {jogador2}")
        break
        
    elif jogador1 == jogador2:
        print(f"\n Empate!! Tente novamente! \n Escolha do(a) {nome1}: {jogador1} \n Escolha do(a) {nome2}: {jogador2}")
          
    else:
        print(f"\n O Jogador 2 venceu!! \n Escolha do(a) {nome1}: {jogador1} \n Escolha do(a) {nome2}: {jogador2}")
        break