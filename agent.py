from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
import os

# Configura tu API key
os.environ["OPENAI_API_KEY"] = ""
# Crear prompt
prompt = PromptTemplate(
    input_variables=["pregunta"],
    template="Responde de forma concisa: {pregunta}"
)

# Instanciar modelo
llm = ChatOpenAI(model="gpt-4o", temperature=0.3)

# Crear cadena moderna usando operadores funcionales
chain = prompt | llm

# Ejecutar
pregunta_usuario = "¿Cuál es la capital de Colombia?"
respuesta = chain.invoke({"pregunta": pregunta_usuario})

print("🤖 Respuesta del agente:", respuesta.content)
