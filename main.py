from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
import streamlit as st

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    st.error("오류: OpenAI API 키가 설정되지 않았습니다.")
    st.warning(".env 파일에 'OPENAI_API_KEY=YOUR_SECRET_KEY' 형태로 키가 올바르게 설정되었는지 확인해주세요.")
    st.stop()
chat_model = ChatOpenAI(api_key=api_key)

st.title("인공지능 시인")

subject = st.text_input("시의 주제를 입력해주세요.")
st.write("시의 주제 : " + subject)

if st.button("시 작성"):
    with st.spinner("시 작성 중 ..."):
        result = chat_model.invoke(subject + "ai에 대한 시를 써줘")
        st.write(result.content)