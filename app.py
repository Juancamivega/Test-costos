import streamlit as st
import plotly.express as px
import pandas as pd
from datetime import datetime

# Configuración de página
st.set_page_config(
    page_title="Dashboard Papá - Trompudo",
    page_icon="🐶",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Tema oscuro con toques Mechanicus (verde cian)
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

# Sidebar
with st.sidebar:
    st.header("🎛️ Controles del Omnissiah")
    
    collar_costo = st.slider("Costo estimado del collar isabelino / dona", 
                             min_value=15000, max_value=50000, value=25000, step=1000,
                             help="Ajusta según el modelo que elijas")
    
    proyeccion = st.selectbox("Selecciona período", 
                              ["Marzo 2026 (actual)", 
                               "Abril 2026 (proyección)", 
                               "Comparación Marzo vs Abril"],
                              help="La proyección incluye un ajuste estimado")

# ==================== DATOS Y LÓGICA DE PROYECCIÓN ====================
planilla = 406800
coomeva = 253000
cirugia = 3500000
inflacion_abril = 0.06   # 6% estimado - puedes cambiar este valor

total_mensual_base = planilla + coomeva

# Variables que siempre se definen (evita NameError)
if proyeccion == "Marzo 2026 (actual)":
    total_mensual = total_mensual_base
    cirugia_mes = cirugia
    mensaje_proyeccion = "Valores reales de marzo 2026"
    delta = None
    delta_color = "normal"

elif proyeccion == "Abril 2026 (proyección)":
    total_mensual = int(total_mensual_base * (1 + inflacion_abril))
    cirugia_mes = cirugia
    mensaje_proyeccion = f"Proyección Abril 2026 (+{int(inflacion_abril*100)}%)"
    delta = f"+{int((total_mensual - total_mensual_base)/1000)}k"
    delta_color = "normal"

else:  # Comparación
    total_mensual = total_mensual_base
    cirugia_mes = cirugia
    mensaje_proyeccion = "Comparación Marzo vs Abril"
    delta = None
    delta_color = "normal"

total_general = total_mensual + cirugia_mes + collar_costo

# ==================== MÉTRICAS PRINCIPALES ====================
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
    st.metric("📋 Planilla", f"${planilla:,}", "Seguridad + Pensión + Salud")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
    st.metric("❤️ Prepagada Coomeva", f"${coomeva:,}", "Por 253")
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
    st.metric("🐕 Cirugía TPLO Trompudo", f"${cirugia:,}", "Aprobado ✅")
    st.markdown('</div>', unsafe_allow_html=True)

# Totales con proyección
st.subheader(f"📈 {mensaje_proyeccion}")
t1, t2, t3 = st.columns(3)
with t1:
    st.metric("Costos Mensuales", f"${total_mensual:,}", delta, delta_color=delta_color)
with t2:
    st.metric("Cirugía + Collar", f"${cirugia_mes + collar_costo:,}")
with t3:
    st.metric("**TOTAL GENERAL**", f"${total_general:,}", "💙 Espíritu de la Máquina despierto")

# Gráfico
st.subheader("📊 Distribución de Costos")
data = pd.DataFrame({
    "Categoría": ["Planilla", "Coomeva", "Cirugía TPLO", "Collar"],
    "Monto": [planilla, coomeva, cirugia_mes, collar_costo]
})

fig = px.pie(data, names="Categoría", values="Monto",
             color_discrete_sequence=["#00d4ff", "#00ffaa", "#0088cc", "#ffaa00"],
             hole=0.45)
fig.update_traces(textinfo="percent+label")
st.plotly_chart(fig, use_container_width=True)

# Incluye / No incluye
col_inc, col_no = st.columns(2)
with col_inc:
    with st.expander("✅ INCLUYE la cirugía", expanded=True):
        st.write("- Laboratorios prequirúrgicos (hemático, ALT, Creatinina)")
        st.write("- Anestesia inhalada + TIVA")
        st.write("- Medicación analgésica y antibiótico del día")
        st.write("- Insumos ortopédicos")
        st.write("- 1 día de hospitalización (24h)")
        st.write("- Radiografías pre y post-quirúrgicas")
        st.write("- Control en 12 días (retiro de puntos)")

with col_no:
    with st.expander("❌ NO INCLUYE", expanded=True):
        st.write("- Medicación postquirúrgica en casa")
        st.write("- Días adicionales de hospitalización")
        st.write(f"- Collar isabelino/dona (**${collar_costo:,} COP**)")
        st.write("- Controles radiográficos posteriores")
        st.write("- Fisioterapias")

# Botón dopamina
if st.button("¡Activar Microdosis de Dopamina! 🐾⚙️"):
    st.balloons()
    st.success("¡El Espíritu de la Máquina aprueba! Todo bajo control papá ❤️")

st.caption(f"Actualizado: {datetime.now().strftime('%d de marzo de 2026')} • Hecho con cariño 🐶")