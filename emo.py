import streamlit as st
from textblob import TextBlob
단계 2: 감정 분석을 위한 함수 생성하기

다음으로 텍스트 문자열을 입력으로 받고 해당 텍스트의 감정을 반환하는 함수를 만들겠습니다. TextBlob의 sentiment.polarity 메서드는 -1부터 1까지의 부동 소수점 값을 반환합니다. 여기서 -1은 부정적인 감정, 1은 긍정적인 감정, 0은 중립적인 감정을 나타냅니다.

def analyze_sentiment(text):
    return TextBlob(text).sentiment.polarity
단계 3: Streamlit 앱 만들기

이제 Streamlit 앱을 만들겠습니다. 제목과 텍스트 입력 필드를 추가하여 사용자가 텍스트를 입력할 수 있도록 하고, 버튼을 추가하여 클릭할 때 입력된 텍스트의 감정을 분석하고 결과를 표시하겠습니다.

st.title('감정 분석 앱')
 
user_input = st.text_input("텍스트를 입력하세요.")
 
if st.button('분석하기'):
    sentiment = analyze_sentiment(user_input)
    if sentiment < 0:
        st.write('이 텍스트의 감정은 부정적입니다.')
    elif sentiment > 0:
        st.write('이 텍스트의 감정은 긍정적입니다.')
    else:
        st.write('이 텍스트의 감정은 중립적입니다.')