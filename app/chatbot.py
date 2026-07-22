# from app.history import ConversationHistory
# from app.prompts import SYSTEM_PROMPT 
# from app.logger import logger

# class Chatbot:
#     def __init__(self):
#         print("🤖 Chatbot initialized!")
#         logger.info("Chatbot started")
#         self.history = ConversationHistory()

#         print("System Prompt Loaded:")
#         print(SYSTEM_PROMPT)

#     def chat(self):
#         while True:
#             user_input = input("You: ")

#             if user_input.lower() == "exit":
#                 print("👋 Goodbye!")
#                 break

#             try:
#                 self.history.add_user_message(user_input)

#                 logger.info(f"User: {user_input}")

#                 ai_response = f"You said -> {user_input}"

#                 self.history.add_assistant_message(ai_response)

#                 print(f"AI: {ai_response}")

#                 logger.info(f"AI: {ai_response}")

#                 print(self.history.get_messages())        

#             except Exception as e:
#                 print(f"Error: {e}")    

#                 logger.error(str(e))

from app.history import ConversationHistory
from app.logger import logger
from app.ai_service import AIService
from app.storage import Storage
from app.commands import CommandHandler

class Chatbot:
    def __init__(self):
        print("🤖 Chatbot initialized!")

        print("=" * 50)
        print("Welcome to AI Chatbot Internship Project")
        print("Type 'help' to see available commands.")
        print("=" * 50)

        logger.info("Chatbot started") #chatbot.log

        self.history = ConversationHistory() #Creates a ConversationHistory object.
        
        saved_messages = Storage.load_history()

        if saved_messages:
            self.history.load_messages(saved_messages)
            print("📂 Previous conversation loaded.")

        self.ai_service = AIService()

    def get_user_input(self):
        return input("You: ")

    # def generate_response(self, messages): #Generates the AI response.
    #     return self.ai_service.generate_response(messages)
    
    def generate_response(self, messages):
        return self.ai_service.generate_streaming_response(messages)

    def process_message(self, user_input): # Processes one complete user message.
        self.history.add_user_message(user_input) # Stores user message.

        messages = self.history.get_messages()

        ai_response = self.generate_response(messages) #Gets AI response.

        self.history.add_assistant_message(ai_response) # Stores AI response.

        Storage.save_history(self.history.get_messages())

        logger.info(f"User: {user_input}") #Writes user message to log file.
        logger.info(f"AI: {ai_response}") #Writes AI response to log file.

        print("\n🤖 AI:")
        print(ai_response)
        print()

        # Temporary for learning
        # print(self.history.get_messages())

    def show_history(self):
        print("\nConversation History:\n")

        for message in self.history.get_messages():
            print(f"{message['role'].title()}: {message['content']}")

        print()

    def clear_history(self):
        self.history.clear()
        print("🧹 Conversation history cleared.\n")

    def show_stats(self):
        stats = self.history.get_stats()

        print("\n📊 Conversation Statistics\n")
        print(f"Total Messages     : {stats['total']}")
        print(f"System Messages    : {stats['system']}")
        print(f"User Messages      : {stats['user']}")
        print(f"Assistant Messages : {stats['assistant']}")
        print()

    def chat(self):
        while True:
            user_input = self.get_user_input()

            # if CommandHandler.is_command(user_input):
            #     print(f"'{user_input}' is a command.")

            if CommandHandler.is_command(user_input):

                should_continue = CommandHandler.execute(
                    user_input,
                    self
                )

                if not should_continue:
                    break

                continue

            # if user_input.lower() == "exit":
            #     print("👋 Goodbye!")
            #     break
            
            # if user_input.lower() == "help":
            #     print("\nAvailable Commands:")
            #     print("help    - Show available commands")
            #     print("history - Show conversation history")
            #     print("clear   - Clear conversation history")
            #     print("exit    - Exit chatbot\n")
            #     continue

            # if user_input.lower() == "history":

            #     print("\nConversation History:\n")

            #     for message in self.history.get_messages():
            #         print(f"{message['role'].title()}: {message['content']}")

            #     print()

            #     continue

            # if user_input.lower() == "clear":
            #     self.history.clear()
            #     print("🧹 Conversation history cleared.\n")
            #     continue

            # if user_input.lower() == "stats":
            #     stats = self.history.get_stats()

            #     print("\n📊 Conversation Statistics\n")
            #     print(f"Total Messages     : {stats['total']}")
            #     print(f"System Messages    : {stats['system']}")
            #     print(f"User Messages      : {stats['user']}")
            #     print(f"Assistant Messages : {stats['assistant']}")
            #     print()

            #     continue

            try:
                self.process_message(user_input) #Processes the complete conversation.

            except Exception as e:
                logger.error(str(e)) #Save the error to the log file.
                print(f"⚠️ Error: {e}")