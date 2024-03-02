# Dicionário é uma coleção não ordenada de pares, chave e valor

# Criando um dicionário
pessoa = {
    "nome": "Hugo",
    "idade": 19,
    "cidade": "Manaus"
}

# Acessando valores por chave
print("Nome: ", pessoa["nome"])
print("Idade: ", pessoa["idade"])
print("Cidade: ", pessoa["cidade"])

# Exibindo dicionário completo 
print("Meu dicionário de exemplo: ", pessoa)

# Removendo um par chave-valor
del pessoa["cidade"]
print(pessoa)

# Métodos: keys[], values[], itens[]
print("Chaves: ", list(pessoa.keys()))
print("Valores: ", list(pessoa.values()))
print("Itens: ", list(pessoa.items()))
