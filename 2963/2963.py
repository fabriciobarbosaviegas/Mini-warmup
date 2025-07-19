# Lista para armazenar o número de votos de cada candidato,
# de acordo com a ordem de inscrição.
# Justificativa: "A urna eletrônica gera um relatório com N inteiros, 
# correspondentes ao número de votos de cada candidato, ordenados pela ordem de inscrição."
votos = []

for i in range(int(input())):
    votos.append(int(input()))

# Encontra o maior número de votos entre todos os candidatos.
# Justificativa: "o mais votado será o novo bobo da corte"
maxVotos = max(votos)

# Verifica se o jovem Carlos (que é o primeiro da lista, índice 0) 
# não está entre os que têm o maior número de votos.
# Se ele não tiver o maior número de votos, ele não foi eleito.
if votos[0] != maxVotos:
    print('N')

# Caso Carlos esteja empatado com o maior número de votos,
# ele é eleito por ter se inscrito primeiro.
# Justificativa: "Caso haja empate entre um ou mais candidatos, 
# aquele que tiver feito a inscrição primeiro é eleito."
else:
    print('S')
