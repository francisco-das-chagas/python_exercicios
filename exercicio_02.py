#02 - Utilizando estruturas de repetição com variável de controle, faça um programa que receba uma string com uma frase informada pelo usuário e conte quantas vezes aparece as vogais a,e,i,o,u e mostre na tela, depois mostre na tela essa mesma frase sem nenhuma vogal.

frase = str(input('digite uma frase: ').upper())
cont = 0
for i  in frase:
  if i in 'AEIOU':
    cont += 1
for i in 'AEIOU':
  cons = frase.replace(i,'')
  frase = cons
print(f'Aa vogais (A,E,I,O,U) aparecem na frase {cont} e a frase sem as vogais fica {cons} ')

