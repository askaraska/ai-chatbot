import json


class Storage:

    FILE_NAME = "chat_history.json"

    @classmethod
    def save_history(cls, messages):
        with open(cls.FILE_NAME, "w", encoding="utf-8") as file:
            json.dump(messages, file, indent=4)

        print("💾 Conversation saved.")

    @classmethod
    def load_history(cls):
        try:
            with open(cls.FILE_NAME, "r", encoding="utf-8") as file:
                return json.load(file)

        except FileNotFoundError:
            return []    

    @classmethod
    def export_history(cls,messages, filename="conversation.txt"):
        with open(filename, "w", encoding="utf-8") as file:

            for message in messages:

                role = message["role"].capitalize()

                content = message["content"]

                file.write(f"{role}: {content}\n\n")    