import streamlit as st
import plotly.express as px
import pandas as pd
from datetime import datetime
from streamlit_lottie import st_lottie  # la usaremos pronto
import requests

# Configuración
st.set_page_config(
    page_title="Dashboard Papá - Trompudo",
    page_icon="🐶",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Tema Mechanicus
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #0a1f3d 0%, #001529 100%);
    }
    .metric-card {
        background: rgba(0, 255, 180, 0.08);
        border: 1px solid rgba(0, 255, 180, 0.3);
        border-radius: 16px;
        padding: 20px;
    }
</style>
""", unsafe_allow_html=True)

st.title("⚙️ ADEPTUS MECHANICUS - Dashboard de Costos")
st.markdown("### Marzo 2026 • Para mi papá ❤️ • Despertando el Espíritu de la Máquina")

# ==================== SONIDOS ====================
st.sidebar.header("🔊 Sonidos del Omnissiah")

# Reemplaza esta URL con el enlace raw de tu archivo mp3 en GitHub
# Ejemplo: https://raw.githubusercontent.com/tuusuario/turepo/main/sounds/offworld_auspex_fragment.mp3
auspex_url = "https://raw.githubusercontent.com/TU_USUARIO/TU_REPO/main/sounds/offworld_auspex_fragment.mp3"  

if st.sidebar.button("🎵 Activar Sonido Offworld Auspex"):
    st.audio(auspex_url, format="audio/mpeg", start_time=0)
    st.success("Sonido del Omnissiah activado ⚙️")

# Sonido corto de dopamina (puedes reemplazar con un archivo propio)
if st.sidebar.button("🐾 Microdosis de Dopamina + Sonido"):
    st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3", format="audio/mpeg")  # ejemplo temporal
    st.balloons()

# ==================== CONTROLES ====================
with st.sidebar:
    st.header("🎛️ Controles del Omnissiah")
    
    collar_costo = st.slider("Costo estimado del collar isabelino / dona", 
                             min_value=15000, max_value=50000, value=25000, step=1000)

    proyeccion = st.selectbox("Selecciona período", 
                              ["Marzo 2026 (actual)", 
                               "Abril 2026 (proyección)", 
                               "Comparación Marzo vs Abril"])

# ==================== LÓGICA DE PROYECCIÓN (igual que antes) ====================
planilla = 406800
coomeva = 253000
cirugia = 3500000
inflacion_abril = 0.06

total_mensual_base = planilla + coomeva

if proyeccion == "Marzo 2026 (actual)":
    total_mensual = total_mensual_base
    cirugia_mes = cirugia
    mensaje_proyeccion = "Valores reales de marzo 2026"
    delta = None
elif proyeccion == "Abril 2026 (proyección)":
    total_mensual = int(total_mensual_base * (1 + inflacion_abril))
    cirugia_mes = cirugia
    mensaje_proyeccion = f"Proyección Abril 2026 (+{int(inflacion_abril*100)}%)"
    delta = f"+{int((total_mensual - total_mensual_base)/1000)}k"
else:
    total_mensual = total_mensual_base
    cirugia_mes = cirugia
    mensaje_proyeccion = "Comparación Marzo vs Abril"
    delta = None

total_general = total_mensual + cirugia_mes + collar_costo

# ==================== MÉTRICAS Y GRÁFICO (sin cambios) ====================
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
    st.metric("📋 Planilla", f"${planilla:,}")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
    st.metric("❤️ Prepagada Coomeva", f"${coomeva:,}")
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
    st.metric("🐕 Cirugía TPLO Trompudo", f"${cirugia:,}")
    st.markdown('</div>', unsafe_allow_html=True)

st.subheader(f"📈 {mensaje_proyeccion}")
t1, t2, t3 = st.columns(3)
with t1:
    st.metric("Costos Mensuales", f"${total_mensual:,}", delta)
with t2:
    st.metric("Cirugía + Collar", f"${cirugia_mes + collar_costo:,}")
with t3:
    st.metric("**TOTAL GENERAL**", f"${total_general:,}")

# Gráfico (mismo de antes)
data = pd.DataFrame({
    "Categoría": ["Planilla", "Coomeva", "Cirugía TPLO", "Collar"],
    "Monto": [planilla, coomeva, cirugia_mes, collar_costo]
})
fig = px.pie(data, names="Categoría", values="Monto", hole=0.45,
             color_discrete_sequence=["#00d4ff", "#00ffaa", "#0088cc", "#ffaa00"])
st.plotly_chart(fig, use_container_width=True)

# Incluye / No incluye (sin cambios)
col_inc, col_no = st.columns(2)
with col_inc:
    with st.expander("✅ INCLUYE la cirugía", expanded=True):
        st.write("- Laboratorios prequirúrgicos...")
        # ... resto igual

with col_no:
    with st.expander("❌ NO INCLUYE", expanded=True):
        st.write(f"- Collar isabelino/dona (**${collar_costo:,} COP**)")

st.caption(f"Actualizado: {datetime.now().strftime('%d de marzo de 2026')} • Hecho con cariño 🐶⚙️")