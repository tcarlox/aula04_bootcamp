# Crie um dicionário para armazenar informações de um livro
# Inclua título, autor e ano de lançamento
# Imprima todos os valores do dicionário
# Só pra ficar interessante vamos incluir typing para dizer quais tipos de variáveis estamos usando (Dict, Any)
# Any aceita praticamente tudo

from typing import Dict, Any

livro: Dict[str, Any] = {
    "Titulo": "O Codigo Da Vinci",
    "Autor": "Dan Brown",
    "Ano": 2003,
}

print(livro)

# Se eu quiser linha a linha faço o seguinte
# Assim vou precisar transformar cada um em uma lista

from typing import Dict, Any

livro_1: Dict[str, Any] = {
    "Titulo": "O Codigo Da Vinci",
    "Autor": "Dan Brown",
    "Ano": 2003,
}

lista_de_elementos: list = livro.items()
for elemento in lista_de_elementos:
    print(elemento)

# Adicionando livros

livro_2: Dict[str, Any] = {
    "Titulo": "Ataque Hacker",
    "Autor": "Kevin Mitnick",
    "Ano": 1993,
}

# Se eu quiser, posso adicionar dicionários dentro de dicionários

lista_de_livros = []

lista_de_livros.append(livro_1)
lista_de_livros.append(livro_2)

print(lista_de_livros)

lista_de_livros_usando_dict: Dict = {
    "livro_1": {
        "Titulo": "O Codigo Da Vinci",
        "Autor": "Dan Brown",
        "Ano": 2003,
    },
    "livro_2": {
        "Titulo": "Ataque Hacker",
        "Autor": "Kevin Mitnick",
        "Ano": 1993,
    },
}

print(lista_de_livros_usando_dict.get("livro_1"))

# O get serve justamente pra isso, pra facilitar o acesso a um valor,
# no caso o valor de uma chave, sem que eu precise usar os colchetes [].
# E também me permite colocar um valor padrão caso a chave não exista.

print(lista_de_livros_usando_dict.get("livro_3", "Livro nao encontrado"))

# Vamos adicionar mais um item ao dicionário

lista_de_livros_usando_dict["livro_3"] = {
    "Titulo": "A Espera de um Milagre",
    "Autor": "Stephen King",
    "Ano": 1996,
}

print(lista_de_livros_usando_dict)
