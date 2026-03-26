import streamlit as st

st.set_page_config(page_title="Dashboard Papá", page_icon="🐶", layout="centered")

st.title("💙 Dashboard de Costos - Marzo 2026")
st.markdown("### Para mi papá ❤️")

# Costos Mensuales
st.subheader("📊 Costos Mensuales")

col1, col2 = st.columns(2)

with col1:
    st.metric("Planilla (Seguridad, Salud y Pensión)", "$406.800", "✅")

with col2:
    st.metric("Salud Prepagada Coomeva", "$253.000", "✅")

st.success("**Total Mensual:** $659.800 COP")

# Cirugía Trompudo
st.subheader("🐕 Cirugía Trompudo - TPLO (Ligamento Cruzado Derecho)")

st.metric("Costo del procedimiento", "$3.500.000", "APROBADO ✅")

col_inc, col_no = st.columns(2)

with col_inc:
    st.markdown("**✅ INCLUYE**")
    st.write("- Laboratorios prequirúrgicos")
    st.write("- Anestesia inhalada + TIVA")
    st.write("- Medicación del día")
    st.write("- Insumos ortopédicos")
    st.write("- 1 día de hospitalización")
    st.write("- Radiografías pre y post")
    st.write("- Control en 12 días")

with col_no:
    st.markdown("**❌ NO INCLUYE**")
    st.write("- Medicación postquirúrgica")
    st.write("- Días hospitalización extras")
    st.write(f"- Collar isabelino o dona (**estimado $25.000 COP**)")
    st.write("- Controles radiográficos posteriores")
    st.write("- Fisioterapias")

st.info("**Total estimado con collar:** $3.525.000 COP")

# Totales finales
st.subheader("📈 Costos Totales del Mes")
total_mensual = 659800
cirugia = 3500000
gran_total = total_mensual + cirugia

st.metric("Total Mensual", f"${total_mensual:,}")
st.metric("Cirugía Trompudo", f"${cirugia:,}")
st.metric("**TOTAL GENERAL**", f"${gran_total:,}", delta="Todo bajo control 💙")

st.caption("Hecho con cariño en Python + Streamlit para mi papá 🐶")