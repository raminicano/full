import streamlit as st

st.title("스트림릿의 체크 박스 사용 예")

checked1 = st.checkbox("Checkbox 1")
st.write("Checkbox 1 Status:", checked1)

if checked1:
    st.write("Checkbox 1 Checked")
else:
    st.write("Checkbox 1 Not Checked")

checked2 = st.checkbox("Checkbox 2")
st.write("Checkbox 2 Status:", checked2)

if checked2:
    st.write("Checkbox 2 Checked")
else:
    st.write("Checkbox 2 Not Checked")