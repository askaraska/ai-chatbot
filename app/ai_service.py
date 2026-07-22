import json
import time # allow us to pause the program

from app.openai_client import client
from app.settings import MODEL_NAME, TEMPERATURE, MAX_OUTPUT_TOKENS

class AIService:

    def generate_response(self, messages):

        print("\nConversation Sent to AI:\n")

        for message in messages:
            print(message)

        last_message = messages[-1]["content"]

        start_time = time.time()
        
        try:
            response = client.responses.create(
                model=MODEL_NAME,
                input=messages
        )

            answer = response.output_text

        except Exception:

            answer = f"You said -> {last_message}"

        response_time = round(time.time() - start_time,2)

        response = {
            "answer": answer,
            "status": "success",
            "model": MODEL_NAME,
            "response_time": response_time
        }
        
        json_response = json.dumps(response, indent=4)

        for word in json_response.split(): #Becomes: ["You", "said", "->", "hello"]


            print(word, end=" ", flush=True) # flush = True, immediately show each word.

            time.sleep(0.3) # Wait 0.3 seconds before printing the next word.

        print()

        return response["answer"]
    

    def generate_streaming_response(self, messages):
        """Future streaming support.
           Currently uses the normal response method.
        """

        return self.generate_response(messages)

#Currently returns a dummy response.
# Later we'll replace only this line with the real OpenAI API call.

#When You Get API Credits

# stream = client.responses.create(
#     model="gpt-5.5",
#     input=user_input,
#     stream=True
# )