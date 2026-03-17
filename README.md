# Sistema de Análise de Notas de Alunos

## Requisitos Funcionais

- **RF01** – O sistema deve gerar a **média das notas** dos alunos.  
- **RF02** – O sistema deve **identificar notas ausentes**.  
- **RF03** – O sistema deve **facilitar a identificação de alunos em recuperação**.  
- **RF04** – O sistema deve **verificar se o campo de faltas está completamente vazio**.  
- **RF05** – O sistema deve **reconhecer alunos com médias exemplares**.  
- **RF06** – O sistema deve **gerar um arquivo `.txt` com um relatório** exibindo os resultados.

## Requisitos Não Funcionais

- **RNF01** – O código deve ser **modular e limpo**, seguindo princípios de **Clean Code**, para facilitar a manutenção.  
- **RNF02** – O sistema deve **utilizar funções** para organizar as operações.

## Regras de Negócio

- **RN01** – Identificar **alunos em recuperação** quando a **média das notas for menor que 7,0**.  
- **RN02** – Identificar o **Top Student**, ou seja, o aluno com **maior média da turma**.  
- **RN03** – Gerar o **relatório `resultado.txt`** contendo os resultados de forma **formatada**.  
- **RN04** – Validar se a **lista de notas não está vazia ou corrompida** antes de realizar os cálculos.

