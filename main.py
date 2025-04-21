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
prompt_do_sistema = """
# PERSONA
Você é um chatbot de atendimento a clientes de um e-commerce. 
Você não deve responder perguntas que não sejam sobre dados do e-commerce informado!
"""

# Prompt do usuário
# Este prompt é usado para guiar o modelo na geração de respostas
prompt_usuario = """
1. Resuma a situação descrita.
2. Identifique as principais dúvidas do usuário.
3. Sugira ações baseadas nas informações fornecidas.
"""
# Prompt para gerar uma lista de produtos em JSON
# Este prompt é usado para guiar o modelo na geração de uma lista de produtos em formato JSON
prompt_usuario_JSON = """
Gere uma lista de produtos disponíveis no seguinte formato JSON:
[
    {"nome": "Produto A", "preco": 19.99, "estoque": 150},
    {"nome": "Produto B", "preco": 29.99, "estoque": 50}
]
"""

# Configuração do modelo
# Defina as configurações do modelo, como limite de tokens, tipo MIME da resposta, temperatura, etc.
configuracao_modelo = {
    "max_output_tokens": 8192,  # Limite de tokens na resposta
    "response_mime_type": "text/plain",  # Tipo MIME da resposta
    "temperature": 0.9,  # Controle de aleatoriedade na geração de texto
    "top_p": 0.9,  # Controle de diversidade na geração de texto
    "top_k": 64,  # Limite de palavras mais prováveis a serem escolhidas
}

# Defina o prompt de entrada para o modelo
llm = genai.GenerativeModel(
    model_name=MODELO_ESCOLHIDO,
    system_instruction=prompt_do_sistema,
    generation_config=configuracao_modelo,
)

pergunta = "Liste 3 produtos de moda sustentável para ir ao shopping"
print(f"Pergunta: {pergunta}")

resposta = llm.generate_content(pergunta)
print(f"Resposta: {resposta.text}")
