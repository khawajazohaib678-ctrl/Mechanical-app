import streamlit as st

# PAGE CONFIG
st.set_page_config(page_title="Mechanical Unit Converter", layout="centered")

# --- STUDENT INFORMATION ---
st.error("### Student Information")
st.title("👤 Name: Khawaja Zohaib Rasheed")
st.subheader("🆔 Roll Number: 25-ME-215")
st.markdown("---")

st.title("🛠️ Mechanical Unit Converter & Density Checker")

# --- Section 1: Unit Converter ---
st.header("1. Unit Converter")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Pressure")
    bar = st.number_input("Enter Bar:", value=1.0, key="press")
    pa = bar * 100000
    st.info(f"**{bar} Bar** = **{pa:,} Pa**")

with col2:
    st.subheader("Temperature")
    celsius = st.number_input("Enter Celsius (°C):", value=0.0, key="temp")
    kelvin = celsius + 273.15
    st.info(f"**{celsius}°C** = **{kelvin} K**")

# --- Section 2: Material Density ---
st.markdown("---")
st.header("2. Material Density Checker")
densities = {
    "Steel": "7,850 kg/m³",
    "Aluminum": "2,700 kg/m³",
    "Copper": "8,960 kg/m³",
    "Cast Iron": "7,200 kg/m³",
    "Water": "1,000 kg/m³"
}
selected_material = st.selectbox("Select a Material:", list(densities.keys()))
st.success(f"The density of **{selected_material}** is **{densities[selected_material]}**")

st.markdown("---")
st.caption("Developed for ICT Activity - Lecture 12")
