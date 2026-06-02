# Vou repetir a função que criei em outro arquivo (reuse) para mostrar como funciona
# imports = usar código que foi escrito em outros arquivos

from funcoes import ordenar_lista_de_numeros

lista = [3, 5, 10, -1, 3804]

nova_lista = ordenar_lista_de_numeros(numeros=lista)
print(nova_lista)
