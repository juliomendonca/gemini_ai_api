import os

import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
# Set the API key for Google Generative AI

# Certifique-se de que a variável de ambiente GEMINI_API_KEY esteja definida no arquivo .env
CHAVE_API_GOOGLE = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=CHAVE_API_GOOGLE)

# Modelo IA escolhido
MODELO_ESCOLHIDO = "gemini-1.5-flash"  # Modelo escolhido para a geração de texto

# Prompt para IA
prompt_sistema = "Liste apenas os nomes dos produtos, e ofereça uma breve descrição"

# Defina o prompt de entrada para o modelo
llm = genai.GenerativeModel(
    model_name=MODELO_ESCOLHIDO, system_instruction=prompt_sistema
)

pergunta = "Liste 3 produtos de moda sustentável para ir ao shopping"
print(f"Pergunta: {pergunta}")

resposta = llm.generate_content(pergunta)
print(f"Resposta: {resposta.text}")
