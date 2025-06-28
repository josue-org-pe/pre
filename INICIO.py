import streamlit as st
import sentry_sdk

sentry_sdk.init(
    dsn=st.secrets["sentry"]["dsn"]
)

st.set_page_config(page_title="PLANETA ROJO🪐", page_icon="👽", layout="wide")
#definicion de VARIABLES 

def lanzar_errores():
    if st.button(" Error 1: división por cero"):
        try:
            1 / 0
        except Exception as e:
            sentry_sdk.capture_exception(e)
            st.error("Error 1 lanzado: división por cero")

    if st.button(" Error 2: acceso a índice fuera de rango"):
        try:
            lista = [1, 2, 3]
            x = lista[5]
        except Exception as e:
            sentry_sdk.capture_exception(e)
            st.error("Error 2 lanzado: índice fuera de rango")

    if st.button(" Error 3: variable no definida"):
        try:
            print(valor_no_definido)
        except Exception as e:
            sentry_sdk.capture_exception(e)
            st.error("Error 3 lanzado: variable no definida")

    if st.button(" Error 4: error personalizado"):
        try:
            raise RuntimeError("🧪 Error personalizado lanzado manualmente")
        except Exception as e:
            sentry_sdk.capture_exception(e)
            st.error("Error 4 lanzado: RuntimeError personalizado")
lanzar_errores()
universidades = ['UNI', 'UNMSM', 'UNAP']

facultades_uni = ['FIIS','FC','FAUA', 'FIC', 'FIEECS', 'FIGMM','FIEE','FIM','FIQT','FIP','FIA']
facultades_unmsm = ["FM", "FFB", "FO", "FP", "FCS", "FDCP", "FCA", "FCC", "FCE", "FLCH", "FE", "FQIQ", "FCF", "FCB", "FCM", "FIGMMG", "FII", "FIEE", "FISI", "FMV"]
facultades_unap = ["FCA", "FMVZ", "FIE", "FCCA", "FE", "FTS", "FCS", "FIM", "FCJP", "FIQ", "FCB", "FCE", "FIGMM", "FEEI", "FIC", "FIA", "FCSAL", "FIMHEES", "FMH", "FCAH"]

with st.container():
    st.header("¡Hola !")
    st.title("Te brindamos lo que necesitas para tu próxima admisión...")
    st.write("---")
#TUTORIA
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
#SECCION DE COMPARTE MATERIAL
with st.container():
    col1, col2 = st.columns([1, 3])
    col1.subheader("1. COMPARTE TU MATERIAL")
    documento = col2.file_uploader("Sube aquí tu material", type=["pdf"], accept_multiple_files=False)
    
if documento is not None:
    with open(documento.name, "wb") as f:
        f.write(documento.getbuffer())
    col2.success("Archivo guardado exitosamente")
else:
    col2.write("No se ha subido ningún archivo todavía.")

st.write("---")
def MATERIAL():
    st.subheader("2. TUTORIA")
    formulario = ComunicateTutor()
    formulario.mostrar_contenido()
    
    if st.button("Enviar"):
        st.success("Gracias por comunicarte, contactaremos contigo lo más pronto posible.")

if __name__ == "__main__":
    MATERIAL()
# SECCION DE CONTACTO 
st.write("---")
st.subheader("CONTACTO")
col1, col2, col3 = st.columns([1,1,1])

enlace_youtube = "https://www.youtube.com/channel/UCee5pfQ3b43EZUYHTm7U8HQ"
enlace_whatsapp = "https://wa.link/fgu2s7"
enlace_github = "https://github.com/josue-org-pe"

logo_youtube = '<a href="{0}"><img src="https://img.icons8.com/color/48/000000/youtube-play.png"/></a>'.format(enlace_youtube)
logo_whatsapp = '<a href="{0}"><img src="https://img.icons8.com/color/48/000000/whatsapp--v4.png"/></a>'.format(enlace_whatsapp)
logo_github = '<a href="{0}"><img src="https://img.icons8.com/fluent/48/000000/github.png"/></a>'.format(enlace_github)

col1.markdown(logo_youtube, unsafe_allow_html=True)
col2.markdown(logo_whatsapp, unsafe_allow_html=True)
col3.markdown(logo_github, unsafe_allow_html= True)
