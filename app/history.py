from app.prompts import SYSTEM_PROMPT

class ConversationHistory:
    def __init__(self):
        # self.messages = [] # Creates an empty list.
        self.messages = [
          {
            "role": "system",
            "content": SYSTEM_PROMPT
          }
    ]

    def add_user_message(self, message): # receives user's text
        #add new user message as a dict format, appendto self.messages list
        self.messages.append({
            "role": "user",
            "content": message
        })

    def add_assistant_message(self, message):  # Stores the AI response.
        self.messages.append({
            "role": "assistant",
            "content": message
        })

    def get_messages(self):
        return self.messages #Returns the whole conversation.
    
    def clear(self):
        self.messages = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            }
        ]

    def get_stats(self):
        return {
            "total": len(self.messages),
            "system": sum(1 for msg in self.messages if msg["role"] == "system"),
            "user": sum(1 for msg in self.messages if msg["role"] == "user"),
            "assistant": sum(1 for msg in self.messages if msg["role"] == "assistant"),
        }   

    def load_messages(self, messages):
        if messages:
            self.messages = messages 
        
    