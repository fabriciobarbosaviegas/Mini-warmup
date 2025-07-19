# Mini-warmup

---

Este repositório reúne soluções para os problemas realizados no Mini Warmup da UFPEL de 2025.

---

## 📁 Estrutura do Repositório

```
.
├── README.md               # Este arquivo de documentação geral
├── 2963                    # Problema Beecrowd 2963 - Bobo da Corte
│   ├── 2963.c              # Solução C99
│   ├── 2963.py             # Solução Python 3
|   └── README.md           # Descrição do problema
├── 2973                    # Problema Beecrowd 2973 - Maratona Brasileira de Comedores de Pipoca
│   ├── 2973.c              # Solução C99
│   ├── 2973.py             # Solução Python 3
|   └── README.md           # Descrição do problema
├── 3445                    # Problema Beecrowd 3445 - Passeios Cotidianos
│   ├── 3445.c              # Solução C99
│   ├── 3445.py             # Solução Python 3
|   └── README.md           # Descrição do problema

```

---

## 📜 Problemas e Descrição

### 1. [Bobo da Corte (2963)](https://www.beecrowd.com.br/judge/pt/problems/view/2963)  
Determinar se o jovem Carlos, que se inscreveu primeiro, foi eleito o bobo da corte após a contagem dos votos.

### 2. [Maratona Brasileira de Comedores de Pipoca (2973)](https://www.beecrowd.com.br/judge/pt/problems/view/2973)  
Dividir sacos de pipoca entre competidores para minimizar o tempo total para comer toda a pipoca, respeitando limites de consumo por segundo.

### 3. [Passeios Cotidianos (3445)](https://www.beecrowd.com.br/judge/pt/problems/view/3445)  
Simular a rotina de Bella levando guarda-chuvas entre casa e trabalho dependendo das condições climáticas e da disponibilidade local.

---

## 🧠 Lógica das Soluções

- **Bobo da Corte (2963)**: Verifica se o primeiro candidato (Carlos) tem o maior número de votos ou está empatado no topo para decidir a vitória.

- **Comedores de Pipoca (2973)**: Usa busca binária para encontrar o menor tempo possível para comer todas as pipocas, dividindo os sacos em sequências contíguas para os competidores.

- **Passeios Cotidianos (3445)**: Simula o transporte diário de guarda-chuvas entre casa e trabalho baseado na chuva e estoque atual, garantindo que Bella nunca fique sem guarda-chuva.