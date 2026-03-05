import re
import random
import datetime

class RuleBasedChatbot:

    def __init__(self):
        self.patterns = [
            (r'hi|hello|hey',
             ["Hello! How can I help you today?",
              "Hi there! What can I do for you?",
              "Hey! Nice to meet you."]),

            (r'how are you',
             ["I'm doing great, thanks for asking!",
              "All systems running perfectly!",
              "I'm just a bot, but I'm doing well!"]),

            (r'(what is your name|who are you)',
             ["I am PyBot, a rule-based chatbot built using Python.",
              "You can call me PyBot, your virtual assistant."]),

            (r'help',
             ["I can respond to greetings, tell the date/time, and answer simple questions.",
              "Try asking me about time, date, or just say hello!"]),

            (r'time',
             [lambda: "Current time is " + datetime.datetime.now().strftime("%H:%M:%S")]),

            (r'date',
             [lambda: "Today's date is " + datetime.datetime.now().strftime("%Y-%m-%d")]),

            (r'bye|exit|quit',
             ["Goodbye! Have a great day!",
              "Bye! It was nice chatting with you.",
              "See you next time!"])
        ]

    def get_response(self, user_input):

        for pattern, responses in self.patterns:
            if re.search(pattern, user_input):

                response = random.choice(responses)

                if callable(response):
                    return response()

                return response

        return "Sorry, I didn't understand that. Could you please rephrase?"

    def start_chat(self):

        print("🤖 PyBot: Hello! I am your Rule-Based Chatbot.")
        print("Type 'bye' to end the conversation.\n")

        while True:

            user_input = input("You: ").lower()

            response = self.get_response(user_input)

            print("🤖 PyBot:", response)

            if re.search(r'bye|exit|quit', user_input):
                break


# Run chatbot
if __name__ == "__main__":
    bot = RuleBasedChatbot()
    bot.start_chat()