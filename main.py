from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot('Test')
conv = open('dictionary.txt', 'r').readlines()

trainer = ListTrainer(bot)

trainer.train(conv)

while True:
    request = input('you: ')
    response = bot.get_response(request)
    print('Bot: ', response)