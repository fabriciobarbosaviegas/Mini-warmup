#include <stdio.h>

int main() {
    int N, H, W;
    scanf("%d %d %d", &N, &H, &W);

    // Para cada dia, ler as condições das duas viagens (casa->trabalho, trabalho->casa)
    for (int i = 0; i < N; i++) {
        char viagem1, viagem2;
        scanf(" %c %c", &viagem1, &viagem2);

        // PRIMEIRA VIAGEM: casa para trabalho
        if (viagem1 == 'Y') {
            // "se estiver chovendo, ela leva um guarda-chuva"
            if (H > 0) {
                H--;    // leva guarda-chuva de casa
                W++;    // deixa guarda-chuva no trabalho
            }
            printf("Y ");
        } else { // chuva == 'N'
            // "se não houver guarda-chuvas no destino (trabalho), leva por precaução"
            if (W == 0 && H > 0) {
                H--;
                W++;
                printf("Y ");
            } else {
                // "caso contrário, não leva guarda-chuva"
                printf("N ");
            }
        }

        // SEGUNDA VIAGEM: trabalho para casa
        if (viagem2 == 'Y') {
            // "se estiver chovendo, ela leva um guarda-chuva"
            if (W > 0) {
                W--;    // leva guarda-chuva do trabalho
                H++;    // deixa guarda-chuva em casa
            }
            printf("Y\n");
        } else { // chuva == 'N'
            // "se não houver guarda-chuvas no destino (casa), leva por precaução"
            if (H == 0 && W > 0) {
                W--;
                H++;
                printf("Y\n");
            } else {
                // "caso contrário, não leva guarda-chuva"
                printf("N\n");
            }
        }
    }

    return 0;
}
