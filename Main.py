from Processamento import calcularMedia, alunosRecuperacao, MelhorAluno, notasAusentes, gerarRelatorio


print("Sistema organizacional escolar")
print("-"*100)

dados = [
    ("Lucas", [8, 7, 9, 10, 6]),
    ("Ligia", [5, 6]),
    ("Fernando", []),
    ("Rodrigo Tadeu", [10,10,10,10,10])
]

rec = alunosRecuperacao(dados)
if len(rec) > 0:
    print(f"Os alunos a seguir estão de recuperação: {rec}")

else:
    print("Nao existem alunos de recuperação")
