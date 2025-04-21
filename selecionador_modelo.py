import os

import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# Carregar a chave da API do arquivo .env
CHAVE_API_GEMINI = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=CHAVE_API_GEMINI)

# Definindo o modelo padrão
modelo = "gemini-1.5-flash"


# Definindo o limite de tokens para o modelo flash
def carrega(nome_do_arquivo):
    """
    Carrega o conteúdo de um arquivo e retorna como string.
    :param nome_do_arquivo: Caminho do arquivo a ser lido."""
    try:
        with open(nome_do_arquivo, "r") as arquivo:
            dados = arquivo.read()
            return dados
    except IOError as e:
        print(f"Erro: {e}")


# Prompt do sistema
prompt_sistema = """
Identifique o perfil de compra para cada cliente a seguir.

O formato de saída deve ser:

cliente - descreva o perfil do cliente em 3 palavras
"""

# Carregar os dados do arquivo CSV
prompt_usuario = carrega("dados\lista_de_compras_100_clientes.csv")

# Contagem de tokens para o modelo flash
modelo_flash = genai.GenerativeModel(f"models/{modelo}")
qtd_tokens = modelo_flash.count_tokens(prompt_usuario)

# Definindo o limite de tokens para o modelo pro
LIMITE_TOKENS = 3000

# Verifica se a contagem de tokens ultrapassa o limite
if qtd_tokens.total_tokens >= LIMITE_TOKENS:
    modelo = "gemini-1.5-pro"
print(f"O modelo selecionado foi: {modelo}")

# Carregar o modelo com o nome selecionado
llm = genai.GenerativeModel(model_name=modelo, system_instruction=prompt_sistema)

# Contagem de tokens para o modelo pro
resposta = llm.generate_content(prompt_usuario)
print(f"Resposta: {resposta.text}")
