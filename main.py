from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
import streamlit as st

# 먼저 .env 파일에서 환경 변수를 로드합니다. (로컬 환경의 기본 설정)
load_dotenv()

# 환경 변수에서 OpenAI API 키를 가져옵니다.
api_key = os.getenv("OPENAI_API_KEY")

# 만약 로컬 .env 파일에서 API 키를 찾지 못했으나, Streamlit Cloud 배포를 염두에 둔다면
# st.secrets에서 찾아볼 수도 있습니다. (로컬 테스트 시에는 이 블록에 들어오지 않도록 .env 설정이 필수)
if not api_key:
    # Streamlit Cloud 환경에서 실행 중일 가능성 또는 로컬에서 secrets.toml을 사용하려는 경우
    # 하지만 로컬에서는 .env 사용이 기본입니다.
    # 만약 로컬에서 이 오류가 발생하면, .env 파일이 없거나 잘못 설정된 것입니다.
    if "OPENAI_API_KEY" in st.secrets:
        api_key = st.secrets["OPENAI_API_KEY"]
    else:
        st.error("오류: OpenAI API 키가 설정되지 않았습니다.")
        st.warning(".env 파일에 'OPENAI_API_KEY=YOUR_SECRET_KEY' 형태로 키가 올바르게 설정되었는지 확인해주세요.")
        st.stop()


# API 키가 여전히 None인 경우 앱 중지
if not api_key:
    st.error("오류: OpenAI API 키를 찾을 수 없습니다. 설정 파일을 확인해주세요.")
    st.stop()

chat_model = ChatOpenAI(api_key=api_key)

st.title("인공지능 시인")

subject = st.text_input("시의 주제를 입력해주세요.")
st.write("시의 주제 : " + subject)

if st.button("시 작성"):
    with st.spinner("시 작성 중 ..."):
        result = chat_model.invoke(subject + "ai에 대한 시를 써줘")
        st.write(result.content)