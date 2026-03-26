import streamlit as st
import plotly.express as px
import pandas as pd
from datetime import datetime

# Configuración de página y tema oscuro azul
st.set_page_config(
    page_title="Dashboard Papá - Trompudo",
    page_icon="🐶",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Tema personalizado (azules oscuros)
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #0a1f3d 0%, #001529 100%);
    }
    .metric-card {
        background: rgba(255,255,255,0.08);
        border-radius: 16px;
        padding: 20px;
        border: 1px solid rgba(0,212,255,0.2);
    }
</style>
""", unsafe_allow_html=True)

st.title("💙 Dashboard de Costos - Marzo 2026")
st.markdown("### Para mi papá ❤️ • Hecho en Python + Streamlit")

# Sidebar para controles interactivos
with st.sidebar:
    st.header("🎛️ Controles")
    collar_costo = st.slider("Costo estimado del collar isabelino / dona", 
                             min_value=15000, max_value=50000, value=25000, step=1000)
    st.markdown(f"**Collar seleccionado:** ${collar_costo:,} COP")
    
    meses_simulacion = st.selectbox("Ver costos para", 
                                    ["Marzo 2026 (actual)", "Abril 2026 (proyección)", "Comparación 2 meses"])
    
    st.caption("Los cambios se aplican automáticamente 💡")

# Datos base
planilla = 406800
coomeva = 253000
total_mensual = planilla + coomeva
cirugia = 3500000

# Totales con collar
total_con_collar = total_mensual + cirugia + collar_costo
ahorro_mensaje = "¡Excelente control!" if total_con_collar < 4500000 else "Revisar opciones de pago"

# Layout principal con columnas
col1, col2, col3 = st.columns([1, 1, 1])

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

# Totales grandes
st.divider()
st.subheader("📈 Totales del Mes")
t1, t2, t3 = st.columns(3)
with t1:
    st.metric("Costos Mensuales", f"${total_mensual:,}")
with t2:
    st.metric("Cirugía + Collar", f"${cirugia + collar_costo:,}")
with t3:
    st.metric("**TOTAL GENERAL**", f"${total_con_collar:,}", delta=ahorro_mensaje, delta_color="normal")

# Gráfico interactivo de distribución de costos
st.subheader("📊 Distribución de Costos")
data = pd.DataFrame({
    "Categoría": ["Planilla", "Prepagada Coomeva", "Cirugía TPLO", "Collar Estimado"],
    "Monto": [planilla, coomeva, cirugia, collar_costo]
})

fig = px.pie(data, names="Categoría", values="Monto", 
             color_discrete_sequence=["#00d4ff", "#00aaff", "#0088cc", "#ffaa00"],
             hole=0.4, title="¿Cómo se distribuyen los $4.1M aprox.?")

fig.update_traces(textinfo="percent+label", hovertemplate="%{label}: $%{value:,}<extra></extra>")
st.plotly_chart(fig, use_container_width=True)

# Sección Incluye / No Incluye con expanders
col_inc, col_no = st.columns(2)

with col_inc:
    with st.expander("✅ Qué INCLUYE la cirugía", expanded=True):
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
        st.write(f"- Collar isabelino/dona (**estimado ${collar_costo:,}**)")
        st.write("- Controles radiográficos posteriores")
        st.write("- Fisioterapias")

# Bonus: Simulación simple
st.divider()
st.subheader("🔮 Simulador rápido")
if st.button("¿Qué pasa si agregamos 2 días extra de hospitalización ($300.000)?"):
    st.success(f"Nuevo total sería: **${total_con_collar + 300000:,} COP**")
    st.info("¡Puedes ajustar el slider del collar para ver diferentes escenarios!")

st.caption(f"Actualizado: {datetime.now().strftime('%d de marzo de 2026')} • Hecho con mucho cariño en Python 🐶💙")

# Botón de dopamina (confetti simple con Streamlit)
if st.button("¡Microdosis de dopamina! 🐾"):
    st.balloons()
    st.success("¡Todo bajo control papá! Eres el mejor.")