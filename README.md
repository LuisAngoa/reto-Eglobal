# 🤖 Asistente Inteligente para Service Desk 

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.55-red)
![LangChain](https://img.shields.io/badge/LangChain-Classic-green)
![Groq](https://img.shields.io/badge/Groq-Llama_3.3-orange)

Este proyecto es una prueba de concepto (PoC) desarrollada para el Reto Técnico de E-global. Consiste en un asistente inteligente impulsado por IA capaz de automatizar la atención y gestión de tickets en un Service Desk.

## ✨ Características Principales

1. **🏷️ Clasificador Automático de Tickets:**
   Utiliza Inteligencia Artificial para leer la descripción de un incidente en lenguaje natural y extraer automáticamente:
   * **Severidad** (Crítica, Alta, Media, Baja).
   * **Área responsable** (Aplicaciones, Infraestructura, Redes, etc.).
   * **Nivel de confianza** de la predicción y una **justificación** lógica.

2. **🔍 Consultas Históricas con RAG (Retrieval-Augmented Generation):**
   Permite a los analistas hacer preguntas en lenguaje natural sobre tickets pasados. El sistema busca semánticamente en una base de datos vectorial (ChromaDB) y responde basándose estrictamente en el contexto histórico, citando el número de ticket de referencia.

## 🛠️ Stack Tecnológico

* **Frontend:** Streamlit
* **Framework IA:** LangChain (Classic)
* **LLM:** `llama-3.3-70b-versatile` vía API de Groq (Elegido por su altísima velocidad y precisión en formato JSON).
* **Embeddings:** `all-MiniLM-L6-v2` vía HuggingFace (Modelo Open Source ligero y eficiente).
* **Base de Datos Vectorial:** ChromaDB (Local).

## 🚀 Ejemplo de Uso

### Clasificación de un Nuevo Ticket
Si un usuario reporta una caída crítica, la IA procesa el texto y lo estructura automáticamente para el sistema.

**Entrada del usuario:**
> "El sistema de pagos en producción está caído desde hace 5 minutos. Los clientes no pueden realizar transacciones."

**Salida generada por la IA (JSON):**
```json
{
  "severidad": "Crítica",
  "area": "Aplicaciones",
  "confianza": 0.9,
  "justificacion": "El sistema de pagos en producción está caído, lo que afecta directamente la capacidad de los clientes para realizar transacciones, impactando significativamente en la operación del negocio."
}

### 🚀 Ejemplo de Uso

Aquí puedes ver la interfaz en acción clasificando un ticket en tiempo real:

![Ejemplo del Clasificador de Tickets](Clasificador ejemplo.png)