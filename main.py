from pywinauto.application import Application
from pywinauto import keyboard
from pandas import Series
from time import sleep
from bot_trainer import bot
import re


class WhatsApp:
    def __init__(self, com_obj: str = 'WhatsApp', chat_name: str = 'Chat'):
        self.com_obj = Application(backend='uia').connect(title=com_obj)
        self.chat_name = chat_name
        sleep(1)

    def select_chat(self):
        name = self.chat_name.replace(' ', '{VK_SPACE}')

        search_chats = self.com_obj.WhatsApp.Document.GroupBox4.Button.wrapper_object()
        search_chats.invoke()
        sleep(1)
        keyboard.send_keys(name)

        # enter first search result
        chat = self.com_obj.WhatsApp.GroupBox6.wrapper_object()
        chat.type_keys('\t')

        # clear search for next time
        search_chats = self.com_obj.WhatsApp.Document.GroupBox4.Button.wrapper_object()
        search_chats.click_input()

    def _get_messages(self):
        check = self.com_obj.WhatsApp.GroupBox8.GroupBox.wrapper_object()
        return check.children_texts()

    def send_message(self, text: str):
        txt = text.replace(' ', '{VK_SPACE}')

        message = self.com_obj.WhatsApp.messageGroupBox2.wrapper_object()
        message.invoke()
        sleep(1)
        keyboard.send_keys(txt)

    def _parse_message(self, message):
        try:
            msg = message[:re.search('\d{2}:\d{2} \w{1}M', message).span()[0] - 1]
        except AttributeError:
            try:
                msg = message[:re.search('\d{1}:\d{2} \w{1}M', message).span()[0] - 1]
            except AttributeError:
                msg = 'Huh?'

        return ' '.join(msg.split(' ')[2:])

    def read_and_respond(self):
        while True:
            msgs = Series(self._get_messages())
            last_msg = msgs.iloc[-1]

            try:
                if last_msg[:3] == 'You':
                    sleep(10)

                last_msg = self._parse_message(last_msg)
                response = bot.get_response(last_msg)
                response = response.text.replace(' ', '{VK_SPACE}')

                new_message = self.com_obj.WhatsApp.messageGroupBox2.wrapper_object()
                new_message.invoke()
                sleep(1)
                keyboard.send_keys(response + '{ENTER}')

            except:
                new_message = self.com_obj.WhatsApp.messageGroupBox2.wrapper_object()
                new_message.invoke()
                sleep(1)
                keyboard.send_keys('huh?{ENTER}')


if __name__ == '__main__':
    w_bot = WhatsApp(chat_name='Something Else')
    w_bot.select_chat()
    w_bot.read_and_respond()
