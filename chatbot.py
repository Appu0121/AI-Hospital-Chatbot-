import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [r'I want to book an appointment', ['Sure, what day and time work for you?']],
    [r'Thank you', ['You're welcome!']]
]

chatbot = Chat(pairs, reflections)
chatbot.converse()