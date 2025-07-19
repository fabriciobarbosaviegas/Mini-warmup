#include <stdio.h>

#define MAXN 10000

int main() {
    int N;
    int votos[MAXN];

    // Lê o número de candidatos.
    // Justificativa: "um total de N candidatos se inscreveram"
    scanf("%d", &N);

    // Lê os votos recebidos por cada candidato, na ordem de inscrição.
    // Justificativa: "relatório com N inteiros... em ordem de inscrição"
    for (int i = 0; i < N; i++) {
        scanf("%d", &votos[i]);
    }

    // Encontra o maior número de votos entre todos os candidatos.
    // Justificativa: "o mais votado será o novo bobo da corte"
    int maxVotos = votos[0];
    for (int i = 1; i < N; i++) {
        if (votos[i] > maxVotos) {
            maxVotos = votos[i];
        }
    }

    // Verifica se Carlos (primeiro inscrito, índice 0) tem o maior número de votos.
    if (votos[0] != maxVotos) {
        // Caso não tenha, ele não é eleito.
        printf("N\n");
    } else {
        // Caso esteja empatado ou tenha mais votos que os demais, ele vence por prioridade na inscrição.
        // Justificativa: "Caso haja empate entre um ou mais candidatos, 
        // aquele que tiver feito a inscrição primeiro é eleito."
        printf("S\n");
    }

    return 0;
}
