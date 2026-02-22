import streamlit as st
import numpy as np

st.markdown("""
<style>
h1, h2, h3, h4 {
    color: black !important;
    font-weight: 700;
}

label {
    color: black !important;
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)

st.title("Chronic Kidney Disease Prediction")

# PAGE CONFIG
st.set_page_config(
    page_title="Kidney Disease Prediction System",
    layout="wide",
    page_icon="🩺"
)

# CSS
st.markdown("""
<style>
.stApp {
    background: linear-gradient(to right, #e3f2fd, #ffffff);
}

.title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    color: black;
}

.card {
    background: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.2);
}

.good {
    color: #2e7d32;
    font-weight: bold;
}

.bad {
    color: #c62828;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)


# TITLE
st.markdown(
    '<div class="title">🩺 Chronic Kidney Disease Prediction</div>',
    unsafe_allow_html=True
)

st.markdown("---")

#  INPUT SECTION
st.subheader("🩺 Patient Medical Details")

col1, col2, col3 = st.columns(3)

with col1:
    age = st.slider("Age", 1, 100, 45)
    bp = st.slider("Blood Pressure", 50, 180, 80)
    sg = st.selectbox(
        "Specific Gravity",
        [1.005, 1.010, 1.015, 1.020, 1.025]
    )
    al = st.slider("Albumin", 0, 5, 1)
    su = st.slider("Sugar", 0, 5, 0)

with col2:
    rbc = st.selectbox("Red Blood Cells", ["normal", "abnormal"])
    pc = st.selectbox("Pus Cell", ["normal", "abnormal"])
    pcc = st.selectbox("Pus Cell Clumps", ["present", "notpresent"])
    ba = st.selectbox("Bacteria", ["present", "notpresent"])
    bgr = st.slider("Blood Glucose Random", 70, 500, 120)

with col3:
    bu = st.slider("Blood Urea", 10, 200, 40)
    sc = st.slider("Serum Creatinine", 0.4, 15.0, 1.2)
    sod = st.slider("Sodium", 110, 160, 135)
    pot = st.slider("Potassium", 2.0, 7.0, 4.5)
    hemo = st.slider("Haemoglobin", 3.0, 17.0, 12.0)

st.markdown("---")

col4, col5, col6 = st.columns(3)

with col4:
    htn = st.selectbox("Hypertension", ["yes", "no"])
    dm = st.selectbox("Diabetes Mellitus", ["yes", "no"])

with col5:
    cad = st.selectbox("Coronary Artery Disease", ["yes", "no"])
    appet = st.selectbox("Appetite", ["good", "poor"])

with col6:
    pe = st.selectbox("Pedal Edema", ["yes", "no"])
    ane = st.selectbox("Anemia", ["yes", "no"])

# RULE-BASED LOGIC
risk_score = 0
if sc > 1.5: risk_score += 2
if bu > 50: risk_score += 1
if hemo < 11: risk_score += 1
if bp > 140: risk_score += 1
if dm == "yes": risk_score += 1
if htn == "yes": risk_score += 1
if ane == "yes": risk_score += 1

# RESULT
st.markdown("---")
st.subheader("🩺 Prediction Result")

if st.button("🩺 Predict Kidney Disease"):
    if risk_score >= 4:
        st.markdown("""
        <div class="card bad">
        🩺 <b>High Risk of Chronic Kidney Disease</b><br>
        Immediate medical consultation recommended.
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="card good">
        🩺 <b>Low Risk of Chronic Kidney Disease</b><br>
        Patient condition appears normal.
        </div>
        """, unsafe_allow_html=True)

# FOOTER
st.markdown("""
<br>
<center>
<b>End-to-End CKD Classification Project</b><br>
Data Science & Machine Learning
</center>
""", unsafe_allow_html=True)
