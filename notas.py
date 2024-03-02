#for i in range(1, 5):
#    somaNota = int(input(f"Digite a {i}º nota: "))

# Verificação do Aluno
matricula = int(input("Digite a matrícula do aluno: "))
nome = input("Digite o nome do aluno: ")
idade = int(input("Digite a idade do aluno: "))
dataNascimento = input("Digite a data de nascimento do aluno (__/__/____): ")

# Lançamento de notas
nota1 = int(input("Digite a 1º nota: "))
nota2 = int(input("Digite a 2º nota: "))
nota3 = int(input("Digite a 3º nota: "))
nota4 = int(input("Digite a 4º nota: "))

# Verifica media final 
mediaFinal = (nota1 + nota2 + nota3 + nota4) / 4

# Verifica situação do aluno
if mediaFinal <= 5:
    situacao = "Reprovado"
else:
    situacao = "Aprovado"

# Cadastro dos dados do aluno, futuramente em um banco de dados
aluno = {
    "Matricula" : matricula,
    "Nome" : nome,
    "Idade" : idade,
    "Data de Nascimento" : dataNascimento,
    "Media Final" : mediaFinal,
    "Situação" : situacao

}

# Imprimir dados
print("====================")
for chave, valor in aluno.items():
    print(f"{chave}: {valor}")