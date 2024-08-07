#%%
import pandas as pd
import re

def parse_highlights(file_path):
    # Função para extrair destaques do arquivo de texto
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    highlights = []
    pattern = re.compile(r'^(.*?)\((.*?)\)\n- Seu destaque ou posição (.*?) \| Adicionado: .*?\n\n(.*?)\n==========$', re.MULTILINE | re.DOTALL)

    for match in pattern.findall(text):
        book_title, author, position, highlight = match
        highlights.append([book_title.strip(), author.strip(), position.strip(), highlight.strip()])

    return pd.DataFrame(highlights, columns=['Book Title', 'Author', 'Position', 'Highlight'])

def update_highlights(new_file_path, existing_df_path):
    # Ler os novos destaques
    new_highlights_df = parse_highlights(new_file_path)
    
    try:
        # Ler o DataFrame existente
        existing_df = pd.read_csv(existing_df_path)
    except FileNotFoundError:
        # Se o arquivo não existir, cria um DataFrame vazio
        existing_df = pd.DataFrame(columns=['Book Title', 'Author', 'Position', 'Highlight'])

    # Concatenar os DataFrames e remover duplicatas
    combined_df = pd.concat([existing_df, new_highlights_df]).drop_duplicates(subset=['Book Title', 'Author', 'Position', 'Highlight'])

    # Salvar o DataFrame combinado
    combined_df.to_csv(existing_df_path, index=False)

    return combined_df

# Exemplo de uso
file_path = 'clippings.txt'
existing_df_path = 'highlights.csv'
#%%
# Atualizar os destaques
df = update_highlights(file_path, existing_df_path)
df

# %%
df.to_csv('highlights.csv')
# %%
