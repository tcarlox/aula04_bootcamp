import csv

# Caminho para o arquivo CSV (Está dentro da própria pasta)
caminho_do_arquivo: str = "exemplo.csv"

# Iniciando a lista vazia que irá armazenar os dados do arquivo
arquivo_csv: list = []

# Usa o gerenciador de contexto "with" para abrir e ler o arquivo .CSV.
# With vai abrir e fechar o arquivo. mode="r" é apenas leitura do arquivo.
# Encoding="utf-8" é para garantir que o arquivo seja lido corretamente e parece ser padrão.
# Arquivo no final é onde vai salvar
with open(file=caminho_do_arquivo, mode="r", encoding="utf-8") as arquivo:
    # Cria um objeto leitor de CSV o DictReader é função do módulo import CSV
    leitor_csv = csv.DictReader(arquivo)

    # Iterando sobre as linhas do arquivo CSV
    # Como o leitor_csv acima ainda não é um dicionário, vou ter que incluir para cada linha um dicionário.
    for linha in leitor_csv:
        arquivo_csv.append(linha)

print(arquivo_csv)

# Arquivo CSV lido agora como dicionário
