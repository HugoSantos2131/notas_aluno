#Listas são coleções de elementos ordenaveis e mutaveis

lista_1 = [1, 2, 3, 4, 5]

#Exibir a Lista Completa
print("Minha Lista de Exempl0 -> ", lista_1)

#Exibir Elementos da da lista
print(lista_1[1])

#Outros Métodos de Lista
lista_1[1] = "python é bom"
print(lista_1[1])

#Método append(): Adiciona um elemento ao final da lista
lista_1.append(6)
print(lista_1)

#Método index: retorna o indisse doS elemento 
print(lista_1.index(6))

#Método insert => Insere um elemento em um índice específico
lista_1.insert(1, 10)
print("Adicionando", lista_1)

#Método pop: Remove o indisse anterior ao solicitado
lista_1.pop(2)
print("removendo ", lista_1)

#Método remove: Remove algo 
lista_1.remove(1)
print("Removendo com remove \n", lista_1 )

#Método sort: organiza a lista em ordem crescente
lista_1.sort()
print("Utilizando 'sort'", lista_1)