import cv2
import streamlit as st
import numpy as np

def detect_and_blur_faces(image):
    # 그레이스케일로 변환
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 얼굴 감지
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # 얼굴에 블러 처리
    for (x, y, w, h) in faces:
        face_roi = image[y:y+h, x:x+w]
        blurred_roi = cv2.GaussianBlur(face_roi, (99, 99), 30)
        image[y:y+h, x:x+w] = blurred_roi

    return image

def main():
    st.title("얼굴 블러 처리 프로그램")
    uploaded_file = st.file_uploader("이미지 파일을 업로드하세요.", type=['jpg', 'jpeg', 'png'])

    if uploaded_file is not None:
        # 업로드한 파일을 OpenCV 이미지로 변환
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        image = cv2.imdecode(file_bytes, 1)

        # 얼굴 블러 처리
        blurred_image = detect_and_blur_faces(image)

        # 블러 처리된 이미지를 Streamlit에 표시
        st.image(blurred_image, channels="BGR", caption="블러 처리된 이미지")

if __name__ == "__main__":
    main()