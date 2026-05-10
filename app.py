import streamlit as st

# Personal Info Section
st.set_page_config(page_title="Mechanical Helper", layout="centered")
st.title("🛠️ Mechanical Unit Converter & Density Checker")
st.markdown("---")
st.sidebar.header("Student Information")
st.sidebar.write("**Name:** Khawaja Zohaib")
st.sidebar.write("**Roll Number:** [Apna Roll No. Likhen]") # <--- Yahan Roll No likhen

# --- Section 1: Unit Converter ---
st.header("1. Unit Converter")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Pressure")
    bar = st.number_input("Enter Bar:", value=1.0)
    pa = bar * 100000
    st.write(f"**{bar} Bar** = **{pa:,} Pa**")

with col2:
    st.subheader("Temperature")
    celsius = st.number_input("Enter Celsius (°C):", value=0.0)
    kelvin = celsius + 273.15
    st.write(f"**{celsius}°C** = **{kelvin} K**")

# --- Section 2: Material Density ---
st.markdown("---")
st.header("2. Material Density Checker")
densities = {
    "Steel": "7,850 kg/m³",
    "Aluminum": "2,700 kg/m³",
    "Copper": "8,960 kg/m³",
    "Cast Iron": "7,200 kg/m³",
    "Titanium": "4,500 kg/m³",
    "Water": "1,000 kg/m³"
}
selected_material = st.selectbox("Select a Material:", list(densities.keys()))
st.info(f"The density of **{selected_material}** is **{densities[selected_material]}**")

st.markdown("---")
st.caption("Submitted for ICT Activity - Lecture 12")
