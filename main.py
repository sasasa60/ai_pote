import streamlit as st
import os
from langchain_openai import ChatOpenAI

# Streamlit Cloud 환경에서 secrets를 가져오도록 시도합니다.
# 'OPENAI_API_KEY'라는 키가 st.secrets에 존재하면 그 값을 사용합니다.
if "OPENAI_API_KEY" in st.secrets:
    api_key = st.secrets["OPENAI_API_KEY"]
else:
    # 로컬 환경이거나 st.secrets에 키가 없을 경우, .env 파일에서 로드합니다.
    from dotenv import load_dotenv
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")

# API 키가 여전히 None인 경우 오류 처리
if not api_key:
    st.error("오류: OpenAI API 키가 설정되지 않았습니다.")
    st.warning("로컬에서는 .env 파일에, Streamlit Cloud에서는 Secrets 설정에 'OPENAI_API_KEY'가 올바르게 설정되었는지 확인해주세요.")
    st.stop()

chat_model = ChatOpenAI(api_key=api_key)

st.title("인공지능 시인")

subject = st.text_input("시의 주제를 입력해주세요.")
st.write("시의 주제 : " + subject)

if st.button("시 작성"):
    with st.spinner("시 작성 중 ..."):
        result = chat_model.invoke(subject + "ai에 대한 시를 써줘")
        st.write(result.content)