import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
import base64

st.set_page_config(page_title="PLANETA ROJO🪐", page_icon="👽", layout="wide")

# DEFINIR VARIABLES
modalidades = ['CEPREUNI', 'ORDINARIO', 'TRASLADO EXTERNO']
universidades = ['UNI']

# --- SECCIÓN 1: TEMARIO ---
st.write("---")
st.subheader("1. BUSCA TU TEMARIO")

seleccion_modalidad = st.selectbox("Selecciona la modalidad de admisión", modalidades, key="modalidad")

temarios = {
    'CEPREUNI': 'static/tcepreuni.pdf',
    'ORDINARIO': 'static/tordinario.pdf',
    'TRASLADO EXTERNO': 'static/ttraslado.pdf'
}

if seleccion_modalidad in temarios:
    ruta_pdf = temarios[seleccion_modalidad]
    try:
        with open(ruta_pdf, "rb") as f:
            pdf_bytes = f.read()
            base64_pdf = base64.b64encode(pdf_bytes).decode('utf-8')
            
            # Mostrar PDF embebido
            pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="600px" type="application/pdf"></iframe>'
            st.markdown(pdf_display, unsafe_allow_html=True)
            
            # Botón de descarga con estilo Streamlit
            nombre_archivo = ruta_pdf.split("/")[-1]
            col1,col2,col3 = st.columns([8,3,8])
            with col2:
                st.download_button(
                    label="📥 Descargar temario",
                    data=pdf_bytes,
                    file_name=nombre_archivo,
                    mime="application/pdf"
                )
    except FileNotFoundError:
        st.error("⚠️ El archivo no fue encontrado.")

# --- SECCIÓN 2: RECOMENDADOS ---
st.write("---")
st.subheader("2. RECOMENDADOS")

# Diccionario corregido
canales_recomendados = {
    "MATEMÁTICAS": {
        "imagen": "https://th.bing.com/th/id/OIP.LROh6BJXWrFcFDMO4xz8eAHaHa?rs=1&pid=ImgDetMain",
        "link": "https://www.youtube.com/@GrupoCienciasSanMarcos"
    },
    "QUÍMICA": {
        "imagen": "https://yt3.googleusercontent.com/Icqkmc-ACv7XqYkfOnQIskx1KmSv4wqM9yvRmZpUIz-GMqMGu1A9lye1jNcFqvMJIQgPus2d=s160-c-k-c0x00ffffff-no-rj",
        "link": "https://www.youtube.com/watch?v=iA_xphwDTNU&list=PLBl30C3P8uOWILiH-wm0HWpfHgm2uTWe1&ab_channel=MichiCiclero"
    },
    "FÍSICA": {
        "imagen": "https://yt3.googleusercontent.com/WrmKQSLQFoktaQPkZJbEwOhQ2bXUiLrVOy4Aa64J2NWFYUaDeLAWE_CLMdeykC6AVTFgkyr0rw=s160-c-k-c0x00ffffff-no-rj",
        "link": "https://www.youtube.com/c/F%C3%ADsicaPRE"
    },
    "Ciclo-Cepreuni": {
        "imagen": "https://th.bing.com/th/id/OIP.FVWGFchd6-8Jv95M1qD-4QHaHa?rs=1&pid=ImgDetMain",
        "link": "https://www.youtube.com/@bastet1490"
    }
}
    

# Estilo para imagen circular
css_circle = """
<style>
.circle-img {
    border-radius: 50%;
    width: 100px;
    height: 100px;
    object-fit: cover;
    transition: transform 0.3s ease;
}
.circle-img:hover {
    transform: scale(1.1);
}
</style>
"""
st.markdown(css_circle, unsafe_allow_html=True)

# Mostrar en columnas
cols = st.columns(3)
for col, (nombre, data) in zip(cols, canales_recomendados.items()):
    with col:
        # Imagen dentro del enlace
        st.markdown(
            f'<a href="{data["link"]}" target="_blank">'
            f'<img src="{data["imagen"]}" class="circle-img"></a>',
            unsafe_allow_html=True
        )
        # Título opcional
        st.markdown(f"**{nombre}**")



# --- SECCIÓN 3: CARRERAS ---
st.write("---")
st.subheader("3. CARRERAS")

df = pd.read_excel("data/datos_carreras.xlsx")
carrera_seleccionada = st.selectbox("Selecciona la carrera", df["CARRERA"], key="carrera")

if carrera_seleccionada:
    descripcion = df[df["CARRERA"] == carrera_seleccionada]["DESCRIPCION"].values[0]
    st.subheader("Descripción")
    st.write(descripcion)

    malla_curricular = df[df["CARRERA"] == carrera_seleccionada]["MALLA"].values[0]
    st.subheader("Malla curricular")
    st.code(malla_curricular)

# --- SECCIÓN 4: TUTORÍA ---
st.write("---")
st.subheader("4. TUTORÍA")

class ComunicateTutor:
    def __init__(self):
        self.nombre = ""
        self.whatsapp = ""
        self.carrera = ""
        self.universidad = ""
        self.mensaje = ""
        self.email = ""
    
    def mostrar_contenido(self):
        self.nombre = st.text_input("Identifícate", placeholder="Escribe tu Nombre completo", max_chars=60)
        self.whatsapp = st.text_input("WhatsApp",  placeholder="Número de teléfono", max_chars=9)
        self.universidad = st.selectbox("Escribe la universidad a postular", universidades, key="uni")
        self.carrera = st.text_input("¿Carrera?", placeholder="¿Carrera?", max_chars=40)
        self.mensaje = st.text_area("Detalles", placeholder="Ejemplo: Llevo dos ciclos intentando...", max_chars=500)
        self.email = st.text_input("Escribe tu email", max_chars=50)

formulario = ComunicateTutor()
formulario.mostrar_contenido()

if st.button("Enviar"):
    st.success("Gracias por comunicarte, contactaremos contigo lo más pronto posible.")
