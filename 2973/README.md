# 🏁 Maratona Brasileira de Comedores de Pipoca — Solução (Beecrowd 2973)

Este repositório contém duas implementações da solução para o problema [Beecrowd 2973 - Maratona Brasileira de Comedores de Pipoca](https://www.beecrowd.com.br/judge/pt/problems/view/2973), proposto na Maratona de Programação da SBC (2019):

- ✅ Versão em **Python 3**
- ✅ Versão em **C99**

---

## 🧠 Enunciado resumido

Uma equipe precisa comer N sacos de pipoca o mais rápido possível. Cada competidor da equipe:

- Só pode comer **sacos contíguos** de pipoca.
- Pode comer até **T pipocas por segundo**.
- Um saco só pode ser comido por um único competidor.

O objetivo é **minimizar o tempo total** em que todos os sacos serão consumidos, dividindo-os entre **C competidores**, que podem comer **em paralelo**.

---

## 📌 Lógica da solução

### 🔍 Abordagem principal: **Busca binária no tempo mínimo**

A ideia é aplicar **busca binária** para encontrar o menor tempo possível em que a divisão dos sacos entre os competidores ainda é válida.

Para cada tempo candidato `mid`:

1. Calculamos o **máximo de pipocas** que um competidor pode comer nesse tempo:  
   `max_pipocas = mid * T`

2. Percorremos os sacos e tentamos dividi-los em **blocos contíguos** para os competidores, sem ultrapassar `max_pipocas`.

3. Se for possível fazer essa divisão com `C` ou menos competidores, o tempo é viável, e tentamos reduzi-lo.

4. Se **algum saco for maior que `max_pipocas`**, ou forem necessários mais de `C` competidores, o tempo candidato é insuficiente.

Repetimos até encontrar o menor tempo viável.

---

---

## ▶️ Como executar

### 🐍 Python

```bash
python3 pipoca.py
```

### 📘 C99

```bash
gcc -std=c99 -o pipoca pipoca.c
./pipoca
```

---

## ✅ Exemplos de saída

| Entrada             | Saída |
| ------------------- | ----- |
| `5 3 4`             |  `4`  |
|  `5 8 3 10 7`       |       |

| Entrada             | Saída |
| ------------------- | ----- |
| `3 2 1`             |  `6`  |
| `1 5 1`             |       |


| Entrada             | Saída |
| ------------------- | ----- |
| `3 2 1`             |  `5`  |
| `1 1 5`             |       |
