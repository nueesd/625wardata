import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import koreanize_matplotlib

# 데이터 로드
@st.cache_data
def load_data():
    df = pd.read_csv('시도별 피난민 현황.csv', encoding='utf-8')
    for col in df.columns[1:]:
        df[col] = pd.to_numeric(df[col].str.replace(',', ''), errors='coerce')
    return df

df = load_data()

st.title('6.25 전쟁 시도별 피난민 현황')

# 데이터 출력
st.subheader("출처: 국가기록포털")
st.dataframe(df)

# 전체 데이터 그래프 (계 행만 사용)
fig, ax = plt.subplots(figsize=(8, 4))
total_data = df[df['구분'] == '계'].melt(id_vars=['구분'], var_name='날짜', value_name='피난민 수')
sns.barplot(x='날짜', y='피난민 수', data=total_data, ax=ax)


ax.set_ylabel('피난민 수 (100만명)')
ax.set_title('전체 피난민 현황')
plt.ylim(0, 8000000)  # y축 범위 설정
plt.yticks([0, 1000000, 2000000, 3000000, 4000000, 5000000, 6000000, 7000000], 
           ['0', '100', '200', '300', '400', '500', '600', '700'])


# 값 표시
for i, v in enumerate(total_data['피난민 수']):
    ax.text(i, v, f'{v:,}', ha='center', va='bottom')

st.pyplot(fig)

# 날짜 선택
selected_date = st.selectbox('날짜를 선택하세요:', ['1951. 3. 31.', '1951. 5. 31.', '1952. 12. 31.', '1953. 4. 30.'])

# 선택된 날짜의 데이터 그래프
fig, ax = plt.subplots(figsize=(12, 6))
sns.barplot(x='구분', y=selected_date, data=df[df['구분'] != '계'], ax=ax, color='lightgreen')

ax.set_xlabel('지역')
ax.set_ylabel('피난민 수 (100만명)')
ax.set_title(f'시도별 피난민 현황 ({selected_date})')
plt.xticks(rotation=45)

# y축 범위 및 눈금 설정
ax.set_ylim(0, 2000000)
ax.set_yticks([0, 500000, 1000000, 1500000, 2000000])
ax.set_yticklabels(['0', '50', '100', '150', '200'])

# 값 표시
for i, v in enumerate(df[df['구분'] != '계'][selected_date]):
    ax.text(i, v, f'{v:,}', ha='center', va='bottom')

plt.tight_layout()
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