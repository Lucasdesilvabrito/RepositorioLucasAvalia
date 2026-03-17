from Processamento import calcularMedia, alunosRecuperacao, MelhorAluno, notasAusentes, gerarRelatorio


print("Sistema organizacional escolar")
print("-"*100)

dados = [
    ("Lucas", [8, 7, 9, 10, 6]),
    ("Ligia", [5, 6]),
    ("Fernando", []),
    ("Rodrigo Tadeu", [10,10,10,10,10])
]

for i in range(len(dados)): #aqui o sistema ta lendo o nome e as notas de cada um
    nome = dados[i][0]
    notas = dados[i][1]

    if len(notas) == 0:
        print(f"A lista de notas de {nome} está vazia, adicione as notas")
    
    adicionar = notasAusentes(nome,notas) #adicionar notas que nao tem na lista

    media = calcularMedia(notas) #media

    print(f"O aluno {nome} fechou o semestre com nota média de: {media}")
