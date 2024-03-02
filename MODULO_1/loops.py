# Loops, para tarefas repetitivas
# for para interar uma sequencia de elementos

lista = ['Hugo', 'Quezia', 'Neidson']
for elemento in lista:
    print(elemento)


for i in range(1, 6):
    print(i) 

pessoas = {
    "nome" : "Hugo",
    "idade" : 19,
    "cidade" : "cidade"
}

for chave, valor in pessoas.items():
    print(f"{chave}: {valor}")