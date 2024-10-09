import random
import re

class Chatbot:
    def __init__(self):
        self.rules = {
            'hello|hi|hey': ['Hello!', 'Hi there!', 'Hey!'],
            'how are you': ['I am good, thank you!', 'Just a program, but I feel fine!'],
            'what is your name': ['I am a rule-based chatbot.', 'You can call me Chatbot.'],
            'weather': ['I cannot check the weather, but I hope it is nice where you are!', 'You probably should download a weather app for live weather updates.'],
            'help': ['I can answer general questions such as greetings and request for assistance among other things. Just try!', 'Ask me about my name, how I am, or just say hello!'],
        }

        self.synonyms = {
            'bye': 'exit',
            'goodbye': 'exit',
            'quit': 'exit'
        }
    
        self.fallbacks = [
            'Sorry, I didn\'t quite catch that. Could you say it differently?',
            'I\'m not sure I understand. Can you clarify?',
            'I don’t know the answer to that, but I’m always learning!'
        ]

    def preprocess_input(self, user_input):
        """Convert input to lowercase and replace synonyms"""
        user_input = user_input.lower()

        # Replace synonyms like 'bye' or 'quit' with 'exit'
        for word, synonym in self.synonyms.items():
            user_input = user_input.replace(word, synonym)
        return user_input

    def match_rule(self, user_input):
        """Match user input with predefined rules and return a response"""
        for pattern, responses in self.rules.items():
            if re.search(pattern, user_input):
                return random.choice(responses)  # Return a random response from the matching rule
        return random.choice(self.fallbacks)  # Fallback if no rules match

    def chat(self):
        """Main chat loop for user interaction"""
        print("Chatbot: Hello! How can I help you today?")

        while True:
            user_input = input("You: ").strip()  # Get user input

            if not user_input:
                print("Chatbot: Please enter something!")  # Prompt for input if nothing is entered
                continue

            # Preprocess and handle exit commands
            processed_input = self.preprocess_input(user_input)
            if 'exit' in processed_input:
                print("Chatbot: Goodbye! Have a wonderful day!")
                break

            # Generate a response based on matching rules
            response = self.match_rule(processed_input)
            print(f"Chatbot: {response}")

# Start the chatbot
if __name__ == "__main__":
    bot = Chatbot()
    bot.chat()
