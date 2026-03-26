import json
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

load_dotenv()

class TicketClassifier:
    def __init__(self):
        # Usamos el modelo Llama 3 70b, temperatura 0 para que no invente cosas, y forzamos formato JSON
        self.llm = ChatGroq(
            model="llama3-70b-8192", 
            temperature=0, 
            model_kwargs={"response_format": {"type": "json_object"}}
        )
        
        # Leemos tus instrucciones
        with open("prompts/classifier_prompt.txt", "r", encoding="utf-8") as f:
            template = f.read()
            
        self.prompt = PromptTemplate(template=template, input_variables=["ticket_description"])
        
        # Conectamos las instrucciones con el cerebro de la IA
        self.chain = self.prompt | self.llm

    def classify(self, description: str) -> dict:
        try:
            # Le enviamos el texto y convertimos la respuesta a un diccionario de Python
            response = self.chain.invoke({"ticket_description": description})
            return json.loads(response.content)
        except Exception as e:
            return {"error": f"Hubo un problema: {str(e)}"}
