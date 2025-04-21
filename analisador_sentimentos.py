import os

import google.generativeai as genai
from dotenv import load_dotenv
from google.api_core.exceptions import NotFound

load_dotenv()

# Carregar a chave da API do arquivo .env
CHAVE_API_GEMINI = os.getenv("GEMINI_API_KEY")

# Configurar a chave da API
genai.configure(api_key=CHAVE_API_GEMINI)

# Definindo o modelo padrão
modelo = "gemini-1.5-flash"


# Definindo o limite de tokens para o modelo flash
def carrega(nome_do_arquivo):
    """
    Carrega o conteúdo de um arquivo e retorna como string.

    Args:
        nome_do_arquivo (_type_): _description_

    Returns:
        _type_: _description_
    """
    try:
        with open(nome_do_arquivo, "r") as arquivo:
            dados = arquivo.read()
            return dados
    except IOError as e:
        print(f"Erro: {e}")


# Prompt do sistema
def salva(nome_do_arquivo, conteudo):
    """
    Salva o conteúdo em um arquivo.
    :param nome_do_arquivo: Caminho do arquivo a ser salvo.
    Args:
        nome_do_arquivo (_type_): _description_
        conteudo (_type_): _description_
    """
    try:
        with open(nome_do_arquivo, "w", encoding="utf-8") as arquivo:
            arquivo.write(conteudo)
    except IOError as e:
        print(f"Erro ao salvar arquivo: {e}")


# Prompt do sistema
# O prompt do sistema é uma instrução que define o comportamento do modelo de linguagem.
def analisador_sentimentos(nome_produto, modelo="gemini-1.5-flash"):
    """
    Função para analisar sentimentos de avaliações de produtos."""
    prompt_sistema = """
            Você é um analisador de sentimentos de avaliações de produtos.
            Escreva um parágrafo com até 50 palavras resumindo as avaliações e 
            depois atribua qual o sentimento geral para o produto.
            Identifique também 3 pontos fortes e 3 pontos fracos identificados a partir das avaliações.

            # Formato de Saída

            Nome do Produto:
            Resumo das Avaliações:
            Sentimento Geral: [utilize aqui apenas Positivo, Negativo ou Neutro]
            Ponto fortes: lista com três bullets
            Pontos fracos: lista com três bullets
        """

    # Carregar os dados do arquivo de avaliações
    prompt_usuario = carrega(f"dados/avaliacoes-{nome_produto}.txt")

    # Contagem de tokens para o modelo flash
    print(f"Iniciando a análise de sentimentos do produto: {nome_produto}")
    try:
        # Contagem de tokens para o modelo flash
        llm = genai.GenerativeModel(
            model_name=modelo, system_instruction=prompt_sistema
        )

        # Contagem de tokens para o modelo flash
        resposta = llm.generate_content(prompt_usuario)
        texto_resposta = resposta.text

        # Salvar a resposta em um arquivo
        salva(f"dados/resposta-{nome_produto}", texto_resposta)
    except NotFound as e:
        modelo = "gemini-1.5-flash"
        print(f"Erro no nome do modelo: {e}")
        analisador_sentimentos(nome_produto, modelo)


def main():
    lista_de_produtos = [
        "Camisetas de algodão orgânico",
        "Jeans feitos com materiais reciclados",
        "Maquiagem mineral",
    ]

    for um_produto in lista_de_produtos:
        analisador_sentimentos(um_produto)


if __name__ == "__main__":
    main()
