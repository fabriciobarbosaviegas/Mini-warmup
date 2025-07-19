# Lê os valores de entrada: 
# N = número de sacos de pipoca
# C = número de competidores
# T = limite de pipocas por segundo por competidor
N, C, T = [int(i) for i in input().split()]
P = [int(i) for i in input().split()]  # Lista com a quantidade de pipocas em cada saco

# Busca binária no tempo mínimo possível.
# Limite inferior: 1 segundo (mínimo possível)
# Limite superior: tempo necessário se um único competidor comer tudo (sum(P) // T + 1)
# Justificativa: "O objetivo da competição é comer todas as pipocas no menor tempo possível"
left, right = 1, sum(P) // T + 1

while left < right:
    mid = (left + right) // 2  # Testa um tempo "candidato"
    max_pipocas = mid * T      # Quantidade máxima de pipocas que um competidor pode comer nesse tempo
                               # Justificativa: "cada competidor poderá comer, no máximo, T pipocas por segundo"

    competidores = 1  # Começamos com o primeiro competidor
    pipocas_atual = 0  # Acumulador de pipocas da sequência contígua atual

    for pipoca in P:
        # Se um saco tem mais pipocas do que o permitido no tempo atual, esse tempo é inviável
        # Justificativa: "Todas as pipocas de um mesmo saco devem ser comidas por um único competidor"
        if pipoca > max_pipocas:
            left = mid + 1
            break

        # Se adicionar esse saco excede o limite de pipocas para o competidor atual,
        # passamos para o próximo competidor e reiniciamos o acumulador
        if pipocas_atual + pipoca > max_pipocas:
            competidores += 1
            pipocas_atual = pipoca

            # Se precisamos de mais competidores do que temos disponíveis, o tempo é insuficiente
            # Justificativa: "Cada competidor da equipe deverá comer uma sequência contígua de sacos de pipoca"
            if competidores > C:
                left = mid + 1
                break
        else:
            pipocas_atual += pipoca  # Ainda cabe no competidor atual

    else:
        # Se foi possível dividir entre <= C competidores com esse tempo, tentamos reduzir
        right = mid

# Quando os ponteiros se encontram, encontramos o menor tempo possível
print(left)
