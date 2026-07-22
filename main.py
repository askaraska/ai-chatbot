# from app.openai_client import client

# response = client.responses.create(
#     model="gpt-5.5",
#     input="Hello! Please introduce yourself in one sentence."
# )

# print(response.output_text)

from app.chatbot import Chatbot
from app.settings import validate_settings

validate_settings()

bot = Chatbot()
bot.chat()