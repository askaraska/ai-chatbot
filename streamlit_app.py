# import streamlit as st

# st.set_page_config(
#     page_title="AI Chatbot",
#     page_icon="🤖",
#     layout="centered"
# )

# st.title("🤖 AI Chatbot")

# st.write("Welcome to your AI Chatbot!")

# user_input = st.text_input("Ask something")

# if st.button("Send"):

#     st.write("You:", user_input)

#     st.write("AI:", f"You said -> {user_input}")

# version:2
# import streamlit as st

# from app.ai_service import AIService

# st.set_page_config(
#     page_title="AI Chatbot",
#     page_icon="🤖"
# )

# st.title("🤖 AI Chatbot")

# service = AIService()

# user_input = st.text_input("Ask something")

# if st.button("Send"):

#     messages = [
#         {
#             "role": "user",
#             "content": user_input
#         }
#     ]

#     answer = service.generate_response(messages)

#     st.write("### You")
#     st.write(user_input)

#     st.write("### AI")
#     st.write(answer)

import streamlit as st

from app.ai_service import AIService

st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖"
)

st.title("🤖 AI Chatbot")

service = AIService()

if "messages" not in st.session_state:
    st.session_state.messages = []

if st.button("🗑️ Clear Chat"):
    st.session_state.messages = []
    st.rerun()     

# Display previous conversation
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.write(message["content"])

# User input
prompt = st.chat_input("Type your message...")

if prompt:

    # Show user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.write(prompt)

    # Generate AI response
    answer = service.generate_response(
        st.session_state.messages
    )

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    with st.chat_message("assistant"):
        st.write(answer)