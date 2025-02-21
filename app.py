import google.generativeai as genai
import streamlit as st

genai.configure(api_key="AIzaSyDtScJ6s_5Z902L-soKHxyFtV_DRZMJH4A")
st.title("An AI Code Reviewer")
user_prompt=st.text_area("Enter your code...")
if st.button("Generate") == True:
  model=genai.GenerativeModel(model_name='models/gemini-1.5-pro-latest',
  system_instruction="""You are a friendly AI assistant.
  Given a python code to review, analyze the submitted code and identify bugs, errors or areas of improvement.
  Provide the fixed codde snippets.
  Explain the reasoning behind code corrections or suggestions.
  If the code is not in python politely remind the user that you are a python code review assistant.  """)
  if user_prompt:
    response = model.generate_content(user_prompt)
    st.write(response.text)
