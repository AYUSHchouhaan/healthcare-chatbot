!pip install groq

from dotenv import load_dotenv
import streamlit as st
import os
from groq import Groq

load_dotenv()
# ...

from dotenv import load_dotenv
import streamlit as st
import os
from groq import Groq

load_dotenv()
client = Groq(api_key="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")

st.set_page_config(page_title="Q&A User Support Chatbot", page_icon="🤖")
st.header("healthcare Chatbot 🤖 Ask Anything")
def get_response(question):
    safe_prompt = (
        "You are a helpful and informative assistant, not a doctor. "
        "You may provide general health and wellness information, but you should always say: "
        "'This is not medical advice. Consult a healthcare provider for professional guidance.'\n\n"
        f"User: {question}\nAssistant:"
    )

    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {"role": "user", "content": safe_prompt}
        ],
        temperature=0.7,
        max_tokens=512
    )
    return response.choices[0].message.content

user_input = st.text_input("Ask your question:", key="input")
submit = st.button("Ask the question ✨")
show_history = st.checkbox("Show Chat History 🗨️")

if 'history' not in st.session_state:
    st.session_state.history = []

if submit and user_input:
    response = get_response(user_input)
    st.session_state.history.append(f"You: {user_input}")
    st.session_state.history.append(f"Bot: {response}")
    st.subheader("The Response is ✨")
    st.write(response)

if show_history:
    st.subheader("Chat History 🗨️")
    for chat in st.session_state.history:
        st.write(chat)
