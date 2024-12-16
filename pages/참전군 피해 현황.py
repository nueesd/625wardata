import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import koreanize_matplotlib

# 데이터 로드
@st.cache_data
def load_data():
    return pd.read_csv('참전군 피해 현황.csv', encoding='utf-8')

df = load_data()

st.title('6.25 전쟁 참전군 피해 현황')

# 데이터 출력
st.subheader("출처: 국가기록포털")
st.dataframe(df.head())

# 그래프 생성
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x='구분', y='사상(사망 및 부상)', data=df, color='lightcoral', label='사상(사망 및 부상)', ax=ax)
sns.barplot(x='구분', y='실종/포로', data=df, color='skyblue', label='실종/포로', bottom=df['사상(사망 및 부상)'], ax=ax)

# 값 표시
for index, row in df.iterrows():
    ax.text(index, row['사상(사망 및 부상)'] / 2, f"{row['사상(사망 및 부상)']:,}", ha='center', va='center', color='black')
    ax.text(index, row['사상(사망 및 부상)'] + row['실종/포로'] / 2, f"{row['실종/포로']:,}", ha='center', va='center', color='black')
    total = row['사상(사망 및 부상)'] + row['실종/포로']
    ax.text(index, total + 20000, f"{total:,}", ha='center', va='bottom', color='black', fontsize=9, fontweight='bold')

ax.set_xlabel('참전군 분류')
ax.set_ylabel('인원 수')
ax.set_title('6.25 전쟁 인명 피해 현황')
ax.set_ylim(0, 1200000)
ax.set_yticks(range(0, 1200000 + 1, 100000))
ax.set_yticklabels([f'{int(i/10000)}만' for i in range(0, 1200000 + 1, 100000)])

plt.legend()
plt.tight_layout()

# 스트림릿에 그래프 표시
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