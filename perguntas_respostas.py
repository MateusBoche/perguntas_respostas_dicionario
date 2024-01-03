# Exercício - sistema de perguntas e respostas
from os import system

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

i = 0 
tam = len(perguntas)
cont_acertos = 0
cont_erros = 0
while i < tam:
    system("Cls")
    print("Pergunta:", perguntas[i]["Pergunta"])
    opcoes = perguntas[i]["Opções"]
    respostas = perguntas[i]['Resposta']
    for j, opcao in enumerate(opcoes):
        print(j, opcao)
    
    try:
        escolha = int(input("EScolha uma ocpcao: "))
    except:
        print("Opcao invalida")

    print(respostas)
    
    if opcoes[escolha] == respostas:
        print("Acertou mizeravi")
        cont_acertos += 1
        system("pause")
    else:
        print("Errou vagabundo")
        cont_erros += 1
        system("pause")
    

    i += 1
print("Você Acertou", cont_acertos, "de", tam)
print("Você errou ",cont_erros,"de", tam)