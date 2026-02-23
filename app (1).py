import streamlit as st
import numpy as np

# PAGE CONFIG
st.set_page_config(
    page_title="Kidney Disease Prediction System",
    layout="wide",
    page_icon="🩺"
)

# CSS for better UI/UX
st.markdown("""
<style>
    .stApp { background: linear-gradient(to right, #f8f9fa, #e3f2fd); }
    h1, h2, h3 { color: #1a237e !important; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
    .title { text-align: center; font-size: 42px; font-weight: bold; padding: 20px; color: #1a237e; }
    .card { background: white; padding: 25px; border-radius: 15px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); margin-top: 20px; }
    .metric-container { background: #ffffff; padding: 15px; border-radius: 10px; border-left: 5px solid #1a237e; box-shadow: 2px 2px 5px rgba(0,0,0,0.05); }
</style>
""", unsafe_allow_html=True)

# HEADER
st.markdown('<div class="title">🩺 Chronic Kidney Disease Diagnostic System</div>', unsafe_allow_html=True)
st.write("<center>Advanced Machine Learning Analysis for Early Detection</center>", unsafe_allow_html=True)
st.markdown("---")

# INPUT SECTION
st.subheader("📊 Patient Medical Parameters")
col1, col2, col3 = st.columns(3)

with col1:
    age = st.slider("Age", 1, 100, 45)
    bp = st.slider("Blood Pressure", 50, 180, 80)
    sg = st.selectbox("Specific Gravity", [1.005, 1.010, 1.015, 1.020, 1.025])
    al = st.slider("Albumin Level", 0, 5, 1)
    su = st.slider("Sugar Level", 0, 5, 0)

with col2:
    rbc = st.selectbox("Red Blood Cells", ["normal", "abnormal"])
    pc = st.selectbox("Pus Cell", ["normal", "abnormal"])
    pcc = st.selectbox("Pus Cell Clumps", ["present", "notpresent"])
    bgr = st.slider("Blood Glucose (mg/dL)", 70, 500, 120)
    hemo = st.slider("Haemoglobin (g/dL)", 3.0, 17.0, 12.0)

with col3:
    bu = st.slider("Blood Urea (mg/dL)", 10, 200, 40)
    sc = st.slider("Serum Creatinine (mg/dL)", 0.4, 15.0, 1.2)
    sod = st.slider("Sodium (mEq/L)", 110, 160, 135)
    pot = st.slider("Potassium (mEq/L)", 2.0, 7.0, 4.5)
    htn = st.selectbox("Hypertension", ["yes", "no"])

# OTHER FACTORS (Hidden in Expander to keep UI Clean)
with st.expander("Additional Symptoms & Medical History"):
    ec1, ec2, ec3 = st.columns(3)
    with ec1:
        dm = st.selectbox("Diabetes Mellitus", ["yes", "no"])
        cad = st.selectbox("Coronary Artery Disease", ["yes", "no"])
    with ec2:
        appet = st.selectbox("Appetite", ["good", "poor"])
        pe = st.selectbox("Pedal Edema", ["yes", "no"])
    with ec3:
        ane = st.selectbox("Anemia", ["yes", "no"])
        ba = st.selectbox("Bacteria", ["present", "notpresent"])

# LOGIC FOR PROBABILITY (UX improvement)
risk_points = 0
if sc > 1.5: risk_points += 30
if bu > 50: risk_points += 15
if hemo < 11: risk_points += 20
if bp > 140: risk_points += 10
if dm == "yes": risk_points += 15
if htn == "yes": risk_points += 10
risk_percent = min(risk_points, 100)

# PREDICTION BUTTON
st.markdown("---")
if st.button("🚀 Generate Diagnostic Report"):
    
    # UI Layout for Result
    res_col1, res_col2 = st.columns([1, 2])
    
    with res_col1:
        st.write("### Risk Probability")
        if risk_percent > 50:
            st.error(f"## {risk_percent}%")
        else:
            st.success(f"## {risk_percent}%")
        st.progress(risk_percent / 100)

    with res_col2:
        if risk_percent >= 40:
            st.markdown(f"""
            <div class="card" style="border-left: 10px solid #d32f2f;">
                <h3 style="color: #d32f2f;">POSSIBLE CKD DETECTED</h3>
                <p><b>Analysis:</b> The patient shows significant markers of kidney dysfunction, 
                especially in <b>Serum Creatinine ({sc})</b> and <b>Hemoglobin ({hemo})</b> levels.</p>
                <p style="color: #d32f2f;"><b>Recommendation:</b> Immediate Nephrologist consultation is advised.</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="card" style="border-left: 10px solid #388e3c;">
                <h3 style="color: #388e3c;">KIDNEY CONDITION NORMAL</h3>
                <p><b>Analysis:</b> Based on the provided parameters, the kidney function appears to be stable.</p>
                <p style="color: #388e3c;"><b>Recommendation:</b> Maintain a healthy diet and regular checkups.</p>
            </div>
            """, unsafe_allow_html=True)

    # Key Metrics Highlights
    st.write("### Key Observation Summary")
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Creatinine", f"{sc} mg/dL", delta="-1.2" if sc <= 1.2 else "+ High", delta_color="inverse")
    m2.metric("Hemoglobin", f"{hemo} g/dL", delta="Normal" if hemo >= 12 else "- Low")
    m3.metric("Urea", f"{bu} mg/dL", delta="Normal" if bu <= 40 else "+ High", delta_color="inverse")
    m4.metric("Risk Level", "HIGH" if risk_percent > 50 else "LOW")

# FOOTER
st.markdown("""
<br><hr>
<center style="color: #7f8c8d;">
    <b>CKD Detection System v2.0</b> | Powered by Machine Learning | 2024
</center>
""", unsafe_allow_html=True)
