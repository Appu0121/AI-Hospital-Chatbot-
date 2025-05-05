import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [r'Hi|Hello', ['Hello! How can I assist you today?']],
    [r'I want to book an appointment', ['Sure! What day and time would you prefer?']],
    [r'Thank you', ['You're welcome!']],
    [r'(.*)', ['Sorry, I didn't understand that.']]
]

def run_chatbot():
    print("HospitalBot: Hello! I am your medical assistant.")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == '__main__':
    run_chatbot()
