import nltk
from nltk.chat.util import Chat, reflections

# Pares de padrão e respostas para o chatbot
pares = [
    ["Oi|Olá|Hey", ["Oi!", "Olá!", "Hey!"]],
    ["Como você está?", ["Eu estou bem, obrigado por perguntar.", "Eu estou ótimo!"]],
    ["Qual é o seu nome?", ["Me chamam de gabaJr.", "Pode me chamar de chatbot."]],
    ["Qual é o sentido da vida?", ["42, de acordo com o Guia do Mochileiro das Galáxias."]],
    ["Tchau|Até logo", ["Até mais!", "Tchau!"]]
    ]

# Criando o objeto Chat com os pares de padrão e resposta
chatbot = Chat(pares, reflections)

#Função para integragir com o chatbot
def interagir():
    print("Chatbot: Olá! Como posso ajudar?")
    while True:
        entrada = input("Você:")
        if entrada.lower() == "sair":
            print("Chatbot: Até mais!")
            break
        resposta = chatbot.respond(entrada)
        print("Chatbot:", resposta)

# Iniciando a interação com o chatbot
interagir()

