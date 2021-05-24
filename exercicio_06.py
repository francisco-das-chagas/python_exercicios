# 06 - Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#    "Telefonou para a vítima?"
#    "Esteve no local do crime?"
#    "Mora perto da vítima?"
#    "Devia para a vítima?"
#    "Já trabalhou com a vítima?" 
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
#    Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
#    Entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
#    Caso contrário, ele será classificado como "Inocente".
 

suspeita = 0
respostas = ""

perguntas = ["Telefonou para a vítima? ", 
              "Esteve no local do crime? ", 
              "Mora perto da vítima? ", 
              "Devia para a vítima? ", 
              "Já trabalhou com a vítima? "]

Rell = str(input("Insira seu nome: "))
print("Responda usando [sim] ou [não]")

for i in range(0,5):
    print(perguntas[i])
    respostas = str(input("Resposta: ").upper())
    if respostas == "SIM":
        suspeita += 1
    
if suspeita == 2: 
    print(f"{Rell} Foi Classificado Como Suspeita")
elif suspeita > 2 and suspeita < 5:
    print(f"{Rell} Foi Classificado Como Cúmplice")
elif suspeita == 5:
    print(f"{Rell} Foi Classificado Como Assasino")
elif suspeita <= 1:
    print(f"{Rell} Foi Classificado Como Inocente")






