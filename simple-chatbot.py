import spacy
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

nlp = spacy.load('en_core_web_sm')

bot = ChatBot("Lu",
              storage_adapter='chatterbot.storage.SQLStorageAdapter',
              database_uri='sqlite:///database.sqlite3'
              )

conversa = ListTrainer(bot)
conversa.train([
    'Oi?',
    'Fala',
    'Qual o seu nome?',
    'Lu, foi um prazer te conhecer',
    'Prazer em te conhecer',
    'Igualmente meu patrão',
    'Tudo bem com você?',
    'Tudo ótimo'
])

while True:
    try:
        resposta = bot.get_response(input("Usuário: "))
        if float(resposta.confidence) > 0.5:
            print("Lu: ", resposta)
        else:
            print("Não compreendi :/")
    except(KeyboardInterrupt, EOFError, SystemExit):
        break