res = []

# Leitura da entrada: N = número de dias, H = guarda-chuvas em casa, W = guarda-chuvas no trabalho
N, H, W = [int(i) for i in input().split()]

for _ in range(N):
    aux = []
    dia = input().split()

    # PRIMEIRA VIAGEM: de casa para o trabalho (Bella está em casa)
    if dia[0] == 'Y':
        # "se estiver chovendo, ela leva um guarda-chuva"
        if H > 0:
            H -= 1          # Bella leva um guarda-chuva de casa
            W += 1          # e o deixa no trabalho
        aux.append('Y')

    elif dia[0] == 'N':  
        # "caso contrário, se não houver guarda-chuvas em seu destino (no trabalho)... leva por precaução"
        if W == 0 and H > 0:
            H -= 1
            W += 1
            aux.append('Y')  # leva por precaução
        else:
            aux.append('N')  # "caso contrário, ela não leva guarda-chuva"

    # SEGUNDA VIAGEM: do trabalho para casa (Bella está no trabalho agora)
    if dia[1] == 'Y':
        # "se estiver chovendo, ela leva um guarda-chuva"
        if W > 0:
            W -= 1          # Bella leva um guarda-chuva do trabalho
            H += 1          # e o deixa em casa
        aux.append('Y')

    elif dia[1] == 'N':
        # "caso contrário, se não houver guarda-chuvas em seu destino (em casa)... leva por precaução"
        if H == 0 and W > 0:
            W -= 1
            H += 1
            aux.append('Y')  # leva por precaução
        else:
            aux.append('N')  # "caso contrário, ela não leva guarda-chuva"

    # Adiciona os resultados das duas viagens do dia
    res.append(aux)

# Imprime os resultados
for i in res:
    print(f'{i[0]} {i[1]}')
