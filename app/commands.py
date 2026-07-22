class CommandHandler:

    @staticmethod # This method doesn't need any object data.
    def is_command(user_input):
        commands = {
            "help",
            "history",
            "clear",
            "stats",
            "version",
            "exit"
        }

        return user_input.lower() in commands


    @staticmethod
    # It receives:

    # command → "help", "history", etc.
    # chatbot → your Chatbot object
    def execute(command, chatbot):

        command = command.lower()

        if command == "help":
            print(chatbot.settings.help_text())

        elif command == "history":
            chatbot.show_history()

        elif command == "clear":
            chatbot.clear_history()

        elif command == "stats":
            chatbot.show_stats()

        elif command == "version":
            print("🤖 AI Chatbot")
            print("Version : 1.0.0")
            print("Author  : Sulthan Askar")
            print()

        elif command == "exit":
            print("👋 Goodbye!")
            return False

        return True