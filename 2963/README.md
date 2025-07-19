# 🎭 Bobo da Corte — Solução (Beecrowd 2963)

Este repositório contém soluções para o problema [Beecrowd 2963 - Bobo da Corte](https://www.beecrowd.com.br/judge/pt/problems/view/2963), proposto na Maratona de Programação da SBC (2019).

---

## 📜 Enunciado resumido

Carlos, um jovem comediante, deseja ser eleito o novo **bobo da corte** no Reino dos Emparelhamentos.  
Após a votação popular, os votos de cada candidato são contabilizados na **ordem de inscrição**.

Carlos foi o primeiro a se inscrever, então:
- Se ele tiver o **maior número de votos**, mesmo que empatado com outros, ele vence.
- Se **outro candidato tiver mais votos que ele**, Carlos perde.

---

## 🧠 Lógica da Solução

### ✅ Objetivo:
Verificar se **Carlos (o primeiro da lista)** teve o maior número de votos.  
Se sim → imprimir `'S'` (sim, ele foi eleito).  
Se não → imprimir `'N'`.

### 🔍 Etapas:
1. Ler o número de candidatos `N`.
2. Ler `N` números inteiros representando os votos de cada candidato, na **ordem de inscrição**.
3. Determinar o maior valor entre esses votos.
4. Comparar os votos de Carlos (posição `0`) com o maior valor:
   - Se Carlos **tem o maior valor (ou está empatado)** → `'S'`
   - Caso contrário → `'N'`

---

## ▶️ Como Executar

### 🐍 Python

```bash
python3 bobo.py
```

### 📘 C99

```bash
gcc -std=c99 -o bobo bobo.c
./bobo
```

---

## 💡 Exemplos de Entrada e Saída

| Entrada                | Saída |
| ---------------------- | ----- |
| `3`                    |  `S`  |
| `1000`                 |       |
| `1000`                 |       |
| `1000`                 |       |

| Entrada                | Saída |
| ---------------------- | ----- |
| `5`                    |  `N`  |
| `1`                    |       |
| `2`                    |       |
| `3`                    |       |
| `4`                    |       |
| `5`                    |       |

| Entrada                | Saída |
| ---------------------- | ----- |
| `4`                    |  `S`  |
| `200`                  |       |
| `100`                  |       |
| `200`                  |       |
| `50`                   |       |

| Entrada                | Saída |
| ---------------------- | ----- |
| `3`                    |  `N`  |
| `10`                   |       |
| `20`                   |       |
| `10`                   |       |