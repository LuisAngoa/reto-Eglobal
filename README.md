# Asistente Inteligente para Service Desk - Reto E-global

## Descripción
Este proyecto es un asistente inteligente que clasifica automáticamente tickets de soporte y permite hacer consultas sobre tickets históricos usando RAG.

## Instalación
1. Clona este repositorio o descomprime el archivo ZIP.
2. Crea un entorno virtual: `py -m venv venv`
3. Activa el entorno virtual: `.\venv\Scripts\activate` (Windows)
4. Instala las dependencias: `pip install -r requirements.txt`
5. Renombra el archivo `.env.example` a `.env` y coloca tu API Key de Groq.

## Ejecución
Ejecuta el siguiente comando en la terminal:
`streamlit run src/app.py`