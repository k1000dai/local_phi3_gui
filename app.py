import streamlit as st
from llama_index.llms.ollama import Ollama
from llama_index.core.llms import ChatMessage

# 使用モデルを選択します。
st.title('Ollama phi3')

if "llm" not in st.session_state:
    st.session_state.llm = Ollama(model="phi3", request_timeout=30.0)
    
# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

def response_generator():
    messages = [
        ChatMessage(role="system", content="あなたは日本人の優秀なアシスタントです。"),
        ChatMessage(role="user", content="日本語で答えることはできますか?"),
        ChatMessage(role="assistant", content="はい、日本語で丁寧にお答えします。"),
        ChatMessage(role="user", content=prompt),
    ]
    response = st.session_state.llm.stream_chat(messages=messages)
    for chunk in response:
        yield chunk.delta

with st.chat_message("assistant"):
    response = st.write_stream(response_generator())
# Add assistant response to chat history
st.session_state.messages.append({"role": "assistant", "content": response})
