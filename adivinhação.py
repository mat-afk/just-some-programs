import random

print("-----------------------------------------")
print(">> Bem-vindo ao jogo de adivinhação!!! <<")
print("-----------------------------------------")

#inicialização das principais variáveis
numero_secreto = round(random.randrange(1, 101))
tentativas = 0
pontos = 1000

print("Em qual nível você quer jogar?")
print("[1] Fácil  [2] Médio  [3] Difícil\n")

nivel = int(input("Digite 1, 2 ou 3 para selecionar: "))

if nivel == 1:
    tentativas = 10

elif nivel == 2:
    tentativas = 5

elif nivel == 3:
    tentativas = 3

for rodada in range(1, tentativas + 1):

    print(f"\nTentativa {rodada} de {tentativas}")

    chute = int(input("Digite um número de 1 a 100: "))

    if chute < 1 or chute > 100:

        print("\nVocê deve digitar um número no intervalo entre 1 e 100.")
        continue

    print("\nO seu chute foi ", chute)

    acertou = chute == numero_secreto
    chute_maior = chute > numero_secreto
    chute_menor = chute < numero_secreto

    if acertou:
        print(f"\n>>> Você acertou! Você fez +{pontos} pontos!")
        break

    else:

        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos

        if chute_maior:
            print("\n>>> Você errou! Tente novamente.")
            print("\nDica: O número digitado é maior do que o número secreto.")

        elif chute_menor:
            print("\n>>> Você errou! Tente novamente.")
            print("\nDica: O número digitado é menor do que o número secreto.")

print("\n." * 5)
print("Fim de jogo")