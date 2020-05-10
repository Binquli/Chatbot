from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

# Luodaan chatbotille instanssi
chatbot = ChatBot(
    'CoronaBot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.BestMatch',
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand. I am still learning.',
            'maximum_similarity_threshold': 0.90
        }
    ],
    database_uri='sqlite:///database.sqlite3'
) 

 
 # Haetaan kysymykset & vastaukset .txt tiedostoista
training_questions1 = open('training/questions_1.txt').read().splitlines()
training_questions2 = open('training/questions_2.txt').read().splitlines()

# Botin treenausta, opetetaan botille kieli ja sanat/lauseet
training_data = training_questions1 + training_questions2

trainer = ListTrainer(chatbot)
trainer.train(training_data)  

trainer = ListTrainer(chatbot)
trainer.train(training_data)


trainer_corpus = ChatterBotCorpusTrainer(chatbot)
trainer_corpus.train(
    'chatterbot.corpus.english'
) 