import streamlit as st

st.set_page_config(page_title="PLANETA ROJO🪐", page_icon="👽", layout="wide")

noticias = [
    {
        "titulo": "ADMISIÓN UNI 2025-2",
        "descripcion": "Inscríbete y postula ...",
        "imagen": "https://admision.uni.edu.pe/wp-content/uploads/2025/03/1920x640-1024x341.jpg",
        "link": "https://admision.uni.edu.pe/admision2025/"

    },
    {
        "titulo": "ADMISIÓN UNMSM 2026-1",
        "descripcion": "Se parte de la decada de america ....",
        "imagen": "https://admision.unmsm.edu.pe/portal/wp-content/uploads/2025/02/SLIDER_74-CARRERAS-1-scaled.jpg",
        "link": "https://unmsm.edu.pe/"
    },
    {
        "titulo": "ADMISIÓN UNFV 2025-1",
        "descripcion": "Incribete aquí ....",
        "imagen": "https://www.unfv.edu.pe/oca/images/sliders/2025/Slider_Admision2025d.jpg",
        "link": "https://www.unfv.edu.pe/oca/index.php/pregrado"
    },

]


# Mostrar noticias
for noticia in noticias:
    with st.container():
        st.markdown(
            f"""
            <a href="{noticia['link']}" target="_blank">
                <img src="{noticia['imagen']}" style="width:100%; border-radius:10px;" />
            </a>
            """,
            unsafe_allow_html=True
        )
        st.subheader(noticia["titulo"])
        st.write(noticia["descripcion"])
        st.markdown("---")
