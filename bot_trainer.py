from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
from pandas import read_csv

bot = ChatBot(
    "Chutter",
    logic_adapters=['chatterbot.logic.BestMatch'],
    preprocessors=['chatterbot.preprocessors.clean_whitespace'],
    database_uri='sqlite:///../bot.db'
)

# trainer2 = ChatterBotCorpusTrainer(bot)
# trainer2.train(
#     "chatterbot.corpus.english",
# )
#
# trainer = ListTrainer(bot)
# chat1 = read_csv(r'C:\Users\rebec\WhatsappBot\Response_Bot\chats\chat1.txt', delimiter=',')['message'].astype(str).to_list()
# chat2 = read_csv(r'C:\Users\rebec\WhatsappBot\Response_Bot\chats\chat2.txt', delimiter=',')['message'].astype(str).to_list()
# chat3 = read_csv(r'C:\Users\rebec\WhatsappBot\Response_Bot\chats\chat3.txt', delimiter=',')['message'].astype(str).to_list()
# #chat4 = read_csv(r'C:\Users\rebec\WhatsappBot\Response_Bot\chats\chat4.txt', delimiter=',')['message'].astype(str).to_list()
# train_data = chat1 + chat2 + chat3
# trainer.train(train_data)

# bot.get_response('My name is Tziporah')
#
# while True:
#     response = input('Tziporah: ')
#     if response == 'break':
#         break
#     print('Bot: ', bot.get_response(response))
