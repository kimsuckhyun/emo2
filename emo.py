import streamlit as st
from textblob import TextBlob

def analyze_sentiment(text):
    return TextBlob(text).sentiment.polarity

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