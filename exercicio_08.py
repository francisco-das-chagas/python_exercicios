#08 - Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário. Se por acaso a CTPS for diferente de 0, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente , além da idade, com quantos anos a pessoa vai se aposentar. Considere que o trabalhador deve contribuir por 35 anos para se aposentar.



from os import system
import datetime

ano = datetime.datetime.today().year
trabalhador = dict()

trabalhador['Nome'] = str(input("Digite o Nome:"))
trabalhador['Ano_Nascimento'] = int(input("Digite o Ano de Nascimento: [YYYY]: "))
idade = ano - (trabalhador['Ano_Nascimento'])
trabalhador['CTPS'] = int(input("Digite o Numero da Sua Carteira De Trabalho: ")) 
if trabalhador.get('Idade') == None:
    trabalhador.setdefault('Idade',idade)
    
if trabalhador['CTPS'] != 0:
    trabalhador['Ano_Contratacao'] = int(input("Digite o Ano de Contratação:"))
    trabalhador['Salario'] = float(input("Digite o Salario Correspondente:"))
    falta = 35 - (ano - trabalhador['Ano_Contratacao'])
    if trabalhador.get('Anos_Restantes') == None:
        trabalhador.setdefault('Anos_Restantes',falta)

system('cls')

print("Resumo:")
print("--" *30)
for i, j in trabalhador.items():
    print(f"{i}: {j}")