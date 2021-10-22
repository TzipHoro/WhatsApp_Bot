from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
from pandas import read_csv

bot = ChatBot(
    "Chutter",
    logic_adapters=['chatterbot.logic.BestMatch'],
    preprocessors=['chatterbot.preprocessors.clean_whitespace'],
    database_uri='sqlite:///./chutter.db'
)

# trainer = ChatterBotCorpusTrainer(bot)
# trainer.train(
#     "chatterbot.corpus.english",
# )
#
# trainer2 = ListTrainer(bot)
# chat1 = read_csv(r'path\to\chat.csv', delimiter=',')['message'].astype(str).to_list()
# trainer2.train(chat1)
#
# bot.get_response('My name is Tziporah')

while True:
    response = input('Tziporah: ')
    if response == 'break':
        break
    print('Bot: ', bot.get_response(response))
