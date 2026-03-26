import streamlit as st
from classifier import TicketClassifier
from rag import RAGAssistant

# Configuración básica de la página
st.set_page_config(page_title="Service Desk AI - E-global", page_icon="🤖", layout="wide")

# Caché para no recargar la IA cada vez que hacemos clic en un botón
@st.cache_resource
def load_models():
    return TicketClassifier(), RAGAssistant()

classifier, rag = load_models()

st.title("🤖 Asistente Inteligente para Service Desk")
st.markdown("Desarrollado para el Reto Técnico de E-global")

# Creamos dos pestañas de navegación
tab1, tab2 = st.tabs(["📑 Clasificador de Tickets", "🔍 Consultas Históricas (RAG)"])

with tab1:
    st.header("Clasificar un Nuevo Ticket")
    descripcion = st.text_area("Describe el incidente o solicitud que reporta el usuario:", height=150)
    
    if st.button("Clasificar Ticket con IA", type="primary"):
        if descripcion:
            with st.spinner("Analizando severidad y área..."):
                resultado = classifier.classify(descripcion)
                st.json(resultado) # Muestra el resultado bonito en formato JSON
        else:
            st.warning("Por favor, ingresa una descripción primero.")

with tab2:
    st.header("Consultar Base de Conocimiento")
    pregunta = st.text_input("Haz una pregunta sobre los tickets históricos (ej. '¿Qué pasó con la VPN?'):")
    
    if st.button("Consultar Historial", type="primary"):
        if pregunta:
            with st.spinner("Buscando en la base de datos vectorial..."):
                respuesta = rag.ask(pregunta)
                st.success("Respuesta encontrada:")
                st.write(respuesta)
        else:
            st.warning("Por favor, ingresa una pregunta.")