
import time
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.messages import (
    HumanMessage,
    SystemMessage,
)
import streamlit as st
load_dotenv()
import os
# Load the environment variables from the .env file
# token = os.getenv("HggingFace_API_TOKEN")
llmvar=HuggingFaceEndpoint(repo_id="microsoft/Phi-3-mini-4k-instruct",
                        task="text-generation",
                        temperature=0.7,
                        max_new_tokens=100)
model=ChatHuggingFace(llm=llmvar)



# Streamlit ui    
st.title("Chat with LLM")
st.write("This is a simple chat interface with LLM.")
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# print(prompt)
if prompt:=st.chat_input("Your message"):

 with st.chat_message("user"):
        st.markdown(prompt)
 with st.chat_message("assistant"): 
    with st.spinner("Thinking..."):
        messages = [
            HumanMessage(
                prompt
            ),
                ]
        response = model.invoke(messages)
        assistant_response= response.content
        #  st.success("Response:")
        full_response = ""
        message_placeholder = st.empty()
        for chunk in assistant_response.split():
            
            full_response += chunk + " "
            time.sleep(0.05)
            # Add a blinking cursor to simulate typing
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    
     
        

    #  add history in chat
        st.session_state.chat_history.append({"role": "user", "content": prompt})
 st.session_state.chat_history.append({"role": "Assistant", "content": response.content})
    #  st.experimental_rerun()
    


# res=model.invoke(messages)
# # res=llm.invoke("what is capital of france?")
# print(res.content)
