class CommandHandler:

    @staticmethod # This method doesn't need any object data.
    def is_command(user_input):
        commands = {
            "help",
            "history",
            "clear",
            "stats",
            "exit"
        }

        return user_input.lower() in commands