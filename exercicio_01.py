#01 - Utilizando estruturas condicionais faça um programa que pergunte ao usuário dois números e mostre:
   # A soma deles;
   # A multiplicação entre eles;
   # A divisão inteira deles;
   # Mostre na tela qual é o maior;
   # Verifique se o resultado da soma é par ou impar e mostre na tela;
   # Se a multiplicação entre eles for maior que 40, divida pelo resultado da divisão inteira e mostre o resultado na tela. Se não, mostre que a multiplicação não foi maior que 40.


# pergunte ao usuário dois números:
num1 =  int(input("Digite um numero: "))
num2 =  int(input("Digite outro: "))

#calculo
soma = num1 + num2
multiplicacao = num1*num2
divisao = num1/num2

resultadoDivisao = multiplicacao / divisao

# A soma deles;
print(f'A soma de {num1} e do {num2} é igual a {soma} ')

# A multiplicação entre eles;
print(f'A multiplicação de {num1} e do {num2} é igual a {multiplicacao} ')

# A divisão inteira deles;
print(f'A divisao de {num1} e do {num2} é {divisao} ')

# Mostre na tela qual é o maior;
if(num1) > (num2):
  print(f'O {num1} é maior') 
else:
  print(f'O {num2} é o maior')

#Verifique se o resultado da soma é par ou impar e mostre na tela;
if(soma%2) == 0:
  print(f'O resultado da soma é Par')
else:
    print(f'o resultado da soma é impar')

# Se a multiplicação entre eles for maior que 40, divida pelo resultado da divisão inteira e mostre o resultado na tela. Se não, mostre que a multiplicação não foi maior que 40.

if(multiplicacao) > 40:
  multiplicacao / divisao
  print(f'A divisao da multiplicação pelo resultado da divisao é {resultadoDivisao} ')
else:
  print("A multiplicação nao foi maior que quarenta")





