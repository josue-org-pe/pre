import streamlit as st
st.set_page_config(page_title="PLANETA ROJO🪐", page_icon="👽", layout="wide")
universidades = ['UNI', 'UNMSM', 'UNAP']
facultades_uni = ['FIIS','FC','FAUA', 'FIC', 'FIEECS', 'FIGMM','FIEE','FIM','FIQT','FIP','FIA']
facultades_unmsm = ["FM", "FFB", "FO", "FP", "FCS", "FDCP", "FCA", "FCC", "FCE", "FLCH", "FE", "FQIQ", "FCF", "FCB", "FCM", "FIGMMG", "FII", "FIEE", "FISI", "FMV"]
facultades_unap = ["FCA", "FMVZ", "FIE", "FCCA", "FE", "FTS", "FCS", "FIM", "FCJP", "FIQ", "FCB", "FCE", "FIGMM", "FEEI", "FIC", "FIA", "FCSAL", "FIMHEES", "FMH", "FCAH"]
class ComunicateTutor:
    def __init__(self) -> None:
        self.nombre = ""
        self.whatsapp = ""
        self.carrera = ""
        self.universidad = ""
        self.mensaje = ""
        self.email = ""
    
    def mostrar_contenido(self):
        self.nombre = st.text_input("Identifícate", placeholder="Escribe tu Nombre completo", max_chars=60)
        self.whatsapp = st.text_input("WhatsApp", placeholder="Número de teléfono", max_chars=9)
        col1, col2  =st.columns([2,2])
        with col1 : 
            self.universidad = st.selectbox("Escribe la universidad a postular", universidades)
        with col2:
        # Mostrar las facultades dependiendo de la universidad seleccionada
            if self.universidad == 'UNMSM':
                self.carrera = st.selectbox("Selecciona tu facultad", facultades_unmsm)
            elif self.universidad == 'UNAP':
                self.carrera = st.selectbox("Selecciona tu facultad", facultades_unap)
            elif self.universidad == 'UNI':
                self.carrera = st.selectbox("Selecciona tu facultad", facultades_uni)

        self.mensaje = st.text_input("Detalles", placeholder="Ejemplo: Llevo dos ciclos intentando...", max_chars=500)
def formulario():
    st.subheader("2. TUTORIA")
    formulario = ComunicateTutor()
    formulario.mostrar_contenido()
    
    if st.button("Enviar"):
        st.success("Gracias por comunicarte, contactaremos contigo lo más pronto posible.")

if __name__ == "__main__":
    formulario()

st.write("---")
st.subheader("  CONTACTO ")
col1, col2, col3, col4 = st.columns(4)

# Definir los enlaces a tus redes sociales
enlace_youtube = "https://www.youtube.com/channel/UCee5pfQ3b43EZUYHTm7U8HQ"
enlace_whatsapp = "https://wa.link/fgu2s7"
enlace_github = "https://github.com/josue-org-pe"

# Agregar logotipos con enlaces
logo_youtube = '<a href="{0}"><img src="https://img.icons8.com/color/48/000000/youtube-play.png"/></a>'.format(enlace_youtube)
logo_whatsapp = '<a href="{0}"><img src="https://img.icons8.com/color/48/000000/whatsapp--v4.png"/></a>'.format(enlace_whatsapp)
logo_github = '<a href="{0}"><img src="https://img.icons8.com/fluent/48/000000/github.png"/></a>'.format(enlace_github)

col1.markdown(logo_youtube, unsafe_allow_html=True)
col2.markdown(logo_whatsapp, unsafe_allow_html=True)
col3.markdown(logo_github, unsafe_allow_html=True)