import streamlit as st

st.title("🎴 我的學習名片")
st.subheader("歡迎來到我的個人學習空間！")


name = st.text_input("請輸入姓名：")
st.write("Ex. 創作者姓名")

interest = st.text_input("感興趣的資訊主題：")
st.write("Ex. Python Web App 開發")

if st.button("建立我的學習名片"):
    if name.strip() == "" or interest.strip() == "":
        st.warning("請輸入完整的資訊！")
    else:
        st.success("學習名片已建立！")
        st.write("姓名：" + name)
        st.write("感興趣的資訊主題：" + interest)
        st.write("我正在學習 Python ")
        st.write(f"學習名片已建立！\n姓名：{name}\n感興趣的資訊主題：{interest}")