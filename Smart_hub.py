import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Smart Life Hub", page_icon="🏠", layout="wide")

st.markdown("""
<style>
.big-card {background-color: #f0f2f6; padding: 20px; border-radius: 15px; border-left: 5px solid #4CAF50;}
.alert-card {background-color: #ffebee; padding: 20px; border-radius: 15px; border-left: 5px solid #f44336;}
</style>
""", unsafe_allow_html=True)

st.title("🏠 SMART LIFE HUB - Complete Mini Expert System")
st.subheader("نظام خبير متكامل للبيت الذكي | 4 أنظمة في نظام واحد")

system = st.sidebar.selectbox("اختاري النظام الخبير:", 
    ["Dashboard الرئيسي", "1. Air Conditioner Expert", "2. Fire Alarm Expert", "3. Water Tank Expert", "4. Light & Security Expert"])

if system == "Dashboard الرئيسي":
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("حرارة الغرفة", "29°C", "حر")
    col2.metric("مستوى الخزان", "20%", "فاضي")
    col3.metric("الدخان", "لا يوجد", "آمن")
    col4.metric("الحركة", "لا يوجد", "مفيش حد")
    st.info("👈 اختاري من الجنب أي نظام عشان تشوفي ذكاءه")
    st.balloons()

elif system == "1. Air Conditioner Expert":
    st.header("❄️ خبير التكييف")
    temp = st.slider("درجة حرارة الغرفة:", 10, 45, 29)
    humidity = st.slider("نسبة الرطوبة:", 10, 90, 60)
    people = st.selectbox("هل يوجد أشخاص؟", ["نعم", "لا"])
    if people == "لا":
        st.warning("💡 القرار: اطفاء التكييف - مفيش حد في الأوضة لتوفير الكهرباء")
    elif temp >= 30:
        st.markdown('<div class="big-card"><h3>القرار: تشغيل التكييف على بارد 22° + تشغيل المروحة</h3><p>السبب: IF Temp > 30 THEN Cooling ON</p></div>', unsafe_allow_html=True)
    elif temp >= 26:
        st.markdown('<div class="big-card"><h3>القرار: تشغيل التكييف على 24° Eco Mode</h3></div>', unsafe_allow_html=True)
    elif temp <= 18:
        st.markdown('<div class="big-card"><h3>القرار: تشغيل التدفئة على 24°</h3></div>', unsafe_allow_html=True)
    else:
        st.success("القرار: الجو لطيف - افتحي الشباك أحسن")

elif system == "2. Fire Alarm Expert":
    st.header("🔥 خبير الحريق")
    smoke = st.selectbox("هل يوجد دخان؟", ["لا", "خفيف", "كثيف"])
    heat = st.slider("درجة الحرارة من الحساس:", 20, 100, 45)
    gas = st.checkbox("يوجد رائحة غاز؟")
    if (smoke == "كثيف" and heat > 60) or gas:
        st.markdown('<div class="alert-card"><h1>🚨 خطر حريق !!!</h1><h3>1. تشغيل السرينة 2. فتح رشاشات المياه 3. الاتصال بالمطافي 4. قطع الغاز</h3></div>', unsafe_allow_html=True)
    elif smoke == "خفيف" and heat > 45:
        st.warning("⚠️ تحذير: احتمال بداية حريق - افحصي المطبخ")
    else:
        st.success("✅ الوضع آمن - لا يوجد حريق")

elif system == "3. Water Tank Expert":
    st.header("💧 خبير خزان المياه")
    level = st.slider("مستوى المياه في الخزان %:", 0, 100, 20)
    if level < 20:
        st.error("القرار: IF Level < 20% THEN Motor ON - الخزان فاضي، سيتم تشغيل الموتور الآن")
        st.progress(20)
    elif level > 95:
        st.success("القرار: IF Level > 95% THEN Motor OFF - الخزان مليان، سيتم ايقاف الموتور")
        st.progress(100)
    else:
        st.info(f"القرار: المستوى {level}% - الوضع مستقر")

elif system == "4. Light & Security Expert":
    st.header("💡 خبير الإضاءة والأمان")
    motion = st.selectbox("هل يوجد حركة؟", ["يوجد حركة", "لا يوجد حركة"])
    time = st.slider("الساعة الآن:", 0, 23, 22)
    is_dark = st.checkbox("الدنيا ضلمة؟")
    if motion == "لا يوجد حركة" and time >= 23:
        st.warning("القرار: اطفاء كل الأنوار + تفعيل وضع الحراسة الليلية")
    elif motion == "يوجد حركة" and is_dark:
        st.success("القرار: تشغيل النور أوتوماتيك")
    else:
        st.info("القرار: إبقاء الوضع الحالي")

st.sidebar.markdown("---")
st.sidebar.write(f"Made for Final Project | {datetime.now().year}")