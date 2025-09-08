import json
import random
import time


contador_acertos = 0
tempo = 5

with open ("perguntas.json", "r", encoding="utf-8") as arquivo: 
    perguntas = json.load(arquivo)
    random.shuffle(perguntas) 
    
print("\n👉 QUIZZZZZZZ.....\n")
print("Voce terá 5 segundos para responder cada pergunta:\n")
for pergunta in perguntas:
    print (pergunta ["pergunta"])
    print (pergunta ["opcao"])
    print ()
    inicio = time.time()
    resposta_user = input("Digite a sua resposta:\n")
    fim = time.time()
    if fim - inicio > tempo:
        print ("⏰ Tempo esgotado!!!Próxima pergunta: \n")
        continue

    if resposta_user.strip().lower() == pergunta["resposta"].lower():
        print ("✅ RESPOSTA CORRETA!!!\n")
        contador_acertos += 1
    else:
        print("🚫 RESPOSTA ERRADA. A resposta correta é:", pergunta["resposta"], "\n")


print ("\n👉 Seu numero de acertos foi de: ")
print (contador_acertos)




