import streamlit as st

st.title("BMI 계산기")
l = st.number_input("키(cm)", value=0)
w = st.number_input("몸무게(kg)", value=0)
하하하하
if st.button("계산하기"):
    try:
        r = round(w/((l/100)**2), 2)
        st.write(f"BMI: {r}")
        if r <= 18:
            st.write("저체중 입니다.")
        if r > 18 and r <= 23:
            st.write("정상 입니다.")       
        if r > 23 and r <= 25:
            st.write("과체중 입니다.")       
        if r > 25 and r <= 30:
            st.write("비만 입니다.")
        if r > 30:
            st.write("고도비만 입니다.")
    except:
        st.error("오류 발생")
