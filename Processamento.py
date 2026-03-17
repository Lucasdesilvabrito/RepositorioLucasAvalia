def calcularMedia(notas):
    soma = 0
    if len(notas) == 0:
        return 0
  
    else:
        for n in notas:
            soma += n

        return soma / len(notas)
    


def alunosRecuperacao(dados):
    recuperacao = []

    for aluno in dados:
        nome = aluno[0]
        notas = aluno[1]

        if len(notas) == 5:
            soma = 0
            for n in notas:
                soma += n

            media = soma / 5

            if media < 7:
                recuperacao.append(nome)

    return recuperacao


def MelhorAluno(dados):
    melhorAluno = ""
    maiorMedia = 0

    for aluno in dados:
        nome = aluno[0]
        notas = aluno[1]

        # Só calcula se tiver 5 notas
        if len(notas) == 5:
            soma = 0
            for n in notas:
                soma += n

            media = soma / 5

            # Verifica se é a maior média
            if media > maiorMedia:
                maiorMedia = media
                melhorAluno = nome

    return melhorAluno, maiorMedia



def notasAusentes(nome, notas):
    if len(notas) < 5:
        faltam = 5 - len(notas)
        print(f"O aluno {nome} está com {faltam} notas ausentes, impossível calcular média")

        for i in range(faltam):
            novanota = int(input(f"Adicione a {i+1}º nota faltante para {nome}: "))
            notas.append(novanota)



def gerarRelatorio(dados):
    with open("relatorio.txt", "w") as arquivo:
        arquivo.write("Relatório Acadêmico\n")
        arquivo.write("-"*40 + "\n")
        
        # percorre todos os alunos e escreve notas e médias
        for aluno in dados:
            nome = aluno[0]
            notas = aluno[1]
            media = calcularMedia(notas)
            status = "Recuperação" if media < 7 else "Aprovado"
            
            arquivo.write(f"{nome} - Notas: {notas} - Média: {media} - {status}\n")
        
        # escreve a lista de alunos em recuperação
        rec = alunosRecuperacao(dados)
        if len(rec) > 0:
            arquivo.write("\nAlunos em recuperação:\n")
            for nome_rec in rec:
                arquivo.write(f"{nome_rec}\n")
        
        # escreve o top aluno
        topAluno = MelhorAluno(dados)
        arquivo.write(f"\nMelhor aluno: {topAluno[0]} com média: {topAluno[1]}\n")
