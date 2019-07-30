import time
import telepot
from telepot.loop import MessageLoop
from requests import get

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print 'Got command: %s' % command

    if command == '/ip':
        ip = get('https://api.ipify.org').text
        bot.sendMessage(chat_id,'My Pi Server IP: {}'.format(ip))

"""Replace the capital sentence below with your unique real telegram bot token"""
bot = telepot.Bot('TOKEN HERE')

MessageLoop(bot, handle).run_as_thread()
print 'I am listening ...'

while 1:
    time.sleep(10)
