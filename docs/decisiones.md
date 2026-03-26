# Decisiones Técnicas

1. **Modelo de Lenguaje (LLM)**: Se utilizó `llama-3.3-70b-versatile` a través de Groq por su altísima velocidad de inferencia y precisión para forzar salidas en formato JSON (necesario para el clasificador).
2. **Base de Datos Vectorial**: Se eligió `ChromaDB` (local) porque permite persistir los datos de forma rápida sin depender de servicios en la nube para este prototipo.
3. **Embeddings**: Se usó `all-MiniLM-L6-v2` de HuggingFace porque es un modelo open-source, gratuito y suficientemente preciso para la búsqueda de similitud en textos cortos como los tickets.
4. **Interfaz**: Se construyó con `Streamlit` para lograr un prototipo funcional, interactivo y visualmente agradable en tiempo récord.