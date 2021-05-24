#03 - Utilizando estruturas de repetição com teste lógico, faça um programa que peça uma senha para iniciar seu processamento, só deixe o usuário continuar se a senha estiver correta, após entrar dê boas vindas a seu usuário e apresente a ele o jogo da advinhação, onde o computador vai “pensar” em um número entre 0 e 10. O jogador vai tentar adivinhar qual número foi escolhido até acertar, a cada palpite do usuário diga a ele se o número escolhido pelo computador é maior ou menor ao que ele palpitou, no final mostre quantos palpites foram necessários para vencer.


# Utilizando estruturas de repetição com teste lógico, faça um programa que peça uma senha para iniciar seu processamento

# n = 1
# while n != 0: # O while é um laço com condição de parada, ENQUANTO o n for diferente de zero, faça...
#    n = int(input('Digite um valor: '))
# print('Fim')


# Utilizando estruturas de repetição com teste lógico, faça um programa que peça uma senha para iniciar seu processamento

senha='2021'
tentativa=input("Insira a sua senha:")

while (senha != tentativa):
    print("Poxa deu errado :/ tenta de novo!")
    tentativa=input("Digite a senha:")

print("Aeee Deu certo!. Entrando...")

# após entrar dê boas vindas a seu usuário e apresente a ele o jogo da advinhação, onde o computador vai “pensar” em um número entre 0 e 10. O jogador vai tentar adivinhar qual número foi escolhido até acertar, a cada palpite do usuário diga a ele se o número escolhido pelo computador é maior ou menor ao que ele palpitou, no final mostre quantos palpites foram necessários para vencer.

from random import randint
computador = randint(0, 10)
print('Bem vindo a maquina Blue🟦 Acabei de pensar em um número entre 0 e 10 tente adivinha ele')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Tente um número maior!')
        elif jogador > computador:
            print('Tente um número menor!')
print('conseguiu com {} tentativas! Parabéns'.format(palpites))

