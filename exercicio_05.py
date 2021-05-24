#05 - Refatore o exercício 2, para que uma função receba a frase, faça todo o tratamento necessário e retorne o resultado. Depois mostre na tela o resultado e a quantidade de letras foram retiradas da frase original.

def tratar(frase):
    cont = 0
    for vogal in frase:
        if vogal in 'aáâãeéêiíoõôuú':
            frase = frase.replace(vogal, ' ')
            cont += 1
    print(frase)
    print(f'{cont} vogais retiradas')


frase = str(input('Digite uma frase: ')).lower()
tratar(frase)