# Aula de funções
lista_de_numeros: list = [40, 50, 60, 70, 0, -408593, 1, 50]

# [40,50,60,70,0,-408593,1,50]
# [50,60,700,-408593,1,50]


# Vou empacotar a função com def (def = definindo uma função)
# Então recebo uma lista e retorno uma lista ordenada
def ordenar_lista_de_numeros(numeros: list) -> list:
    nova_lista_de_numeros = numeros.copy()

    for i in range(len(nova_lista_de_numeros)):
        for j in range(i + 1, len(nova_lista_de_numeros)):
            if nova_lista_de_numeros[i] > nova_lista_de_numeros[j]:
                nova_lista_de_numeros[i], nova_lista_de_numeros[j] = (
                    nova_lista_de_numeros[j],
                    nova_lista_de_numeros[i],
                )

    return nova_lista_de_numeros


nova_lista = ordenar_lista_de_numeros(lista_de_numeros)
print(nova_lista)

# Você provavelmente nunca usará a função acima, pois já existe a função "sort" do Python que faz isso
# Mas é bom para aprender como funciona
# Os engenheiros costumam usar funções para empacotar coisas que precisam fazer muitas vezes
