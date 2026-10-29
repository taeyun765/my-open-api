import requests
import streamlit as st

st.title("☀️ 나의 첫 번째 Open API 웹 앱")

st.write("외부 데이터를 실시간으로 가져와 화면에 표시합니다.")

# 사용자가 입력할 수 있는 공간
city = st.text_input("도시 이름을 입력하세요 (예: Seoul)", "Seoul")

if st.button("날씨 조회하기"):
  # 예시 API 호출 코드 (실제 사용하는 API 주소와 키로 변경 필요)
  st.write(f"'{city}'의 데이터를 불러오는 중입니다...")

  # 여기에 requests.get("API_URL")을 사용해 데이터를 가져오고 파싱하는 코드가 들어갑니다.
  # st.metric() 이나 st.json()을 사용해 결과를 예쁘게 보여줄 수 있습니다.
  st.success("데이터 조회 성공! (여기에 API 결과 출력)")
