# idade = 30
# altura = 1.75
# nome = "Jose"
# is_estudante = True

# Lembrar da documentação do Python para programar que é sempre o melhor docs.python.org
# Legal da documentação (pesquisar Google sempre com final doc) é que você consulta por versão
# Python faz tipagem dinâmica, mas não precisa declarar o tipo da variável, diferente de Java, C, etc
# print(type(idade))
# print(type(altura))
# print(type(nome))
# print(type(is_estudante))
# Luciano pediu pra declararmos a partir de agora a tipagem pra ficar claro para outros devs
# O nome disso é TypeHint (engraçado que na prática não muda nada)
# Python tem tipagem forte

# idade: int = 30
# altura: float = 1.75
# nome: str = "Jose"
# is_estudante: bool = True

# Assim Python não soma 2 + "2"

nome_valido: bool = False
salario_valido: bool = False
bonus_valido: bool = False

while not nome_valido:
    try:
        nome: str = input("Digite seu nome: ")

        # Verifica se o nome está vazio
        if len(nome) == 0:
            raise ValueError("O nome não pode estar vazio.")
        # Verifica se há números no nome
        elif any(char.isdigit() for char in nome):
            raise ValueError("O nome não pode conter números.")
        else:
            print("Nome válido!", nome)
            nome_valido = True
    except ValueError as e:
        print(e)

# Lembrar que os tipos primitivos são bool, int, float, str
# Entrando agora em tipos complexos (listas e dicionários)
# Quando você acessa qualquer loja de venda e inclui produtos no carrinho, é uma lista

produto: str = "sapato"
produto_2: str = "camiseta"
produto_3: str = "bermuda"
produto_4: str = "meia"

produtos: list = []

produtos.append(produto)
produtos.append(produto_2)
produtos.append(produto_3)
produtos.append(produto_4)

print(produtos)

# Posso fazer com números também e não necessariamente usando append (adiciona item final da lista)
# Mas também com extend e range que insere uma sequência de números
# Extend adiciona um range, append adiciona um item
numeros = []
numeros.extend(range(0, 5))
print(numeros)

# Retirando produtos
# .pop() - Retira o último elemento da lista e é mais performático do que .remove()
produtos.pop()
print(produtos)

# No .remove() você informa o objeto a ser retirado
produtos.remove("camiseta")
print(produtos)

# No .del você informa o índice do objeto a ser retirado
del produtos[1]
print(produtos)

# Em dicionários nós temos chave valor, com a referência e o conteúdo e o valor
# nome = sapato
# quantidade = 39
# preco = 10.38
# disponibilidade = True

produto_1: dict = {
    "nome": "sapato",
    "quantidade": 39,
    "preco": 10.38,
    "disponibilidade": True,
}

produto_2: dict = {
    "nome": "camiseta",
    "quantidade": 39,
    "preco": 10.38,
    "disponibilidade": True,
}

# Veja que é uma chave ex. nome e um valor ex. camiseta
# No final é algo que se assemelha a uma planilha

# Quero criar um carrinho com lista vazia

carrinho: list = []

carrinho.append(produto_1)
carrinho.append(produto_2)

print(carrinho)

# Logo, posso adicionar dicionários dentro das minhas listas
# Json é o dicionário do JavaScript
