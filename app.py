import streamlit as st
import ollama

st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖"
)

SYSTEM_PROMPT = """
You are a helpful AI assistant.
Give simple, clear and accurate answers.
Use previous conversation context when relevant.
If you are unsure, say so honestly.
"""

st.title("🤖 AI Chatbot")
st.write("Generative AI Chatbot using Prompt Engineering")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_input = st.chat_input("Ask me anything...")

if user_input:
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    try:
        response = ollama.chat(
            model="llama3.2",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT}
            ] + st.session_state.messages
        )

        answer = response["message"]["content"]

        st.session_state.messages.append(
            {"role": "assistant", "content": answer}
        )

        with st.chat_message("assistant"):
            st.markdown(answer)

    except Exception as e:
        st.error(f"Something went wrong: {e}")