from chatterbot import ChatBot


bot = ChatBot(
    "Chutter",
    logic_adapters=['chatterbot.logic.BestMatch'],
    preprocessors=['chatterbot.preprocessors.clean_whitespace'],
    database_uri='sqlite:///./bot.db'
)