import streamlit as st

st.set_page_config(page_title="6.25 전쟁 결과 살펴보기", layout="wide")

st.title("6.25 전쟁 결과 살펴보기")

st.write("6.25 전쟁과 관련된 자료를 보고 분석 및 해석해봅시다.")


col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("시도별 피난민 현황")
    if st.button("시도별 피난민 현황 보기"):
        st.switch_page("pages/시도별 피난민 현황.py")

with col2:
    st.subheader("이산가족 신청 현황")
    if st.button("이산가족 신청 현황 보기"):
        st.switch_page("pages/이산가족 신청 현황.py")

with col3:
    st.subheader("참전군 피해 현황")
    if st.button("참전군 피해 현황 보기"):
        st.switch_page("pages/참전군 피해 현황.py")

st.markdown("---")
st.write("각 카테고리의 버튼을 클릭하면 해당 통계 페이지로 이동합니다.")
