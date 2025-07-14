import streamlit as st

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def bmi_category(bmi):
    if bmi < 18.5:
        return "น้ำหนักน้อย (ผอม)"
    elif 18.5 <= bmi < 24.9:
        return "น้ำหนักปกติ"
    elif 25 <= bmi < 29.9:
        return "น้ำหนักเกิน"
    else:
        return "อ้วน"

def advice_for_bmi(bmi):
    if bmi < 18.5:
        return "ควรรับประทานอาหารให้ครบ 5 หมู่ และตรวจสอบภาวะโภชนาการ"
    elif 18.5 <= bmi < 24.9:
        return "คุณมีน้ำหนักปกติ ควรรักษาระดับนี้ไว้ด้วยการออกกำลังกายและกินอาหารที่มีประโยชน์"
    elif 25 <= bmi < 29.9:
        return "ควรเริ่มควบคุมอาหารและออกกำลังกายอย่างสม่ำเสมอ"
    else:
        return "ควรปรึกษาแพทย์ และเริ่มแผนการลดน้ำหนักอย่างจริงจัง"

# Web App ด้วย Streamlit
st.title("💪 โปรแกรมคำนวณดัชนีมวลกาย (BMI)")
st.write("ใส่น้ำหนักและส่วนสูงของคุณเพื่อดูว่า BMI อยู่ในเกณฑ์ใด")

weight = st.number_input("น้ำหนัก (กิโลกรัม)", min_value=1.0, max_value=500.0, step=0.1)
height = st.number_input("ส่วนสูง (เมตร)", min_value=0.5, max_value=3.0, step=0.01)

if st.button("คำนวณ BMI"):
    bmi = calculate_bmi(weight, height)
    category = bmi_category(bmi)
    advice = advice_for_bmi(bmi)

    st.success(f"BMI ของคุณคือ: {bmi:.2f}")
    st.info(f"อยู่ในเกณฑ์: {category}")
    st.warning(f"คำแนะนำ: {advice}")
