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


def categorizar_produto(nome_do_produto, lista_de_categorias):
    """
    Função para categorizar um produto com base em uma lista de categorias fornecida.
    """
    prompt_do_sistema = f"""
        Você é um categorizados de produtos.
        Você deve assumir as categorias a seguir:

        # Lista de Categorias: 
            {lista_de_categorias}

        #Formato de Saída
            Produto: Nome do Produto
            Categoria:; apresente a categoria do produto escolhida entre as categorias acima.

        # Exemplo de Saída:
            Produto: Escova de dentes de bambu
            Categoria: Higiene e cuidados pessoais

    """

    llm = genai.GenerativeModel(
        model_name=MODELO_ESCOLHIDO,
        system_instruction=prompt_do_sistema,
        generation_config={
            "max_output_tokens": 8192,  # Limite de tokens na resposta
            "response_mime_type": "text/plain",  # Tipo MIME da resposta
            "temperature": 0.9,  # Controle de aleatoriedade na geração de texto
            "top_p": 0.9,  # Controle de diversidade na geração de texto
            "top_k": 64,  # Limite de palavras mais prováveis a serem escolhidas
        },
    )

    return (llm.generate_content(nome_do_produto)).text


def main():
    """# Exemplo de uso da função categorizar_produto
    # Defina a lista de categorias disponíveis
    """
    lista_de_categorias = [
        "Moda sustentável",
        "Higiene e cuidados pessoais",
        "Tecnologia e gadgets",
        "Eletrônicos",
        "Casa e decoração",
        "Esportes e atividades ao ar livre",
        "Saúde e beleza",
        "Alimentos e bebidas",
        "Livros e papelaria",
        "Brinquedos e jogos",
        "Acessórios de moda",
        "Produtos para pets",
    ]

    while True:
        produto = input(
            "Informe o produto a ser categorizado (ou pressione Enter para sair): "
        ).strip()
        if not produto:
            print("Encerrando o programa. Até mais!")
            break

        try:
            resposta = categorizar_produto(produto, lista_de_categorias)
            print(f"\nProduto: {produto}")
            print(f"Categoria sugerida: {resposta}\n")
        except Exception as e:
            print(f"Erro ao categorizar o produto: {e}\n")


if __name__ == "__main__":
    main()
