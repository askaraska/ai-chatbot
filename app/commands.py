class CommandHandler:

    @staticmethod # This method doesn't need any object data.
    def is_command(user_input):
        commands = {
            "help", "h",
            "history", "hist",
            "clear", "cls",
            "stats",
            "version", "v",
            "export", "exp",
            "exit", "quit", "q"
        }

        return user_input.lower() in commands

    @staticmethod
    def normalize(command):

        aliases = {
            "h": "help",
            "hist": "history",
            "cls": "clear",
            "v": "version",
            "exp": "export",
            "quit": "exit",
            "q": "exit"
        }

        return aliases.get(command.lower(), command.lower())

    @staticmethod
    def get_commands():
        return {
            "help",
            "history",
            "clear",
            "stats",
            "version",
            "export",
            "exit"
        }

    @staticmethod
    # It receives:

    # command → "help", "history", etc.
    # chatbot → your Chatbot object
    def execute(command, chatbot):

        # command = command.lower()
        command = CommandHandler.normalize(command)

        if command == "help":
            print("\nAvailable Commands:")
            print("help / h        - Show available commands")
            print("history / hist  - Show conversation history")
            print("clear / cls     - Clear conversation history")
            print("stats           - Show conversation statistics")
            print("version / v     - Show chatbot version")
            print("export / exp    - Export conversation")
            print("exit / quit / q - Exit chatbot\n")

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

        elif command == "export":
            chatbot.export_history()

        elif command == "exit":
            print("👋 Goodbye!")
            return False

        return True