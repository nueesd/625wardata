import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 데이터 로드
@st.cache_data
def load_data():
    df = pd.read_csv('fardata.csv', encoding='utf-8')
    return df

df = load_data()

st.title('이산가족 신청 현황')

# 데이터 출력
st.subheader("출처: 이산가족 신청 현황")
st.dataframe(df)

# 사망자와 생존자 원그래프
fig1, ax1 = plt.subplots()
labels = ['생존자', '사망자']
sizes = [df['생존자'].sum(), df['사망자'].sum()]
colors = ['lightgreen', 'lightcoral']
explode = (0.1, 0)  # 생존자를 강조하기 위해 약간 분리

ax1.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('이산가족 신청자 중 생존자와 사망자 비율')

st.pyplot(fig1)

# 생존자의 연령별 비율 막대그래프 생성
age_labels = df['구분'].tolist()[:-1]  # '계' 제외
survivor_sizes = df['생존자'].tolist()[:-1]  # '계' 제외

# 막대그래프 생성
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(age_labels, survivor_sizes, color='green')

ax.set_xlabel('연령대')
ax.set_ylabel('생존자 수')
ax.set_title('생존자 연령별 분포')


# 값 표시
for i, v in enumerate(survivor_sizes):
    ax.text(i, v + 100, f'{v:,}', ha='center', va='bottom')  # 막대 위에 값 표시

st.pyplot(fig)

st.write("그래프를 보고 알게 된 점을 써주세요.")

user_comment = st.text_area("여러분의 생각을 적어주세요:", height=150)

if st.button("글 남기기"):
    if user_comment:
        st.success("글이 성공적으로 등록되었습니다!")
        st.write("---")
        st.write("**입력한 글:**")
        st.info(user_comment)
    else:
        st.warning("글을 입력해주세요.")

# Return to Main Page Button
if st.button("메인 페이지로 돌아가기"):
    st.switch_page("main.py")  # Assuming "main" is the name of your main page script