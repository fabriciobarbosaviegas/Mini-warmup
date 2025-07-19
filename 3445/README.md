# ☔ Passeios Cotidianos — Solução (Beecrowd 3445)

Este repositório contém soluções para o problema [Beecrowd 3445 - Passeios Cotidianos](https://www.beecrowd.com.br/judge/pt/problems/view/3445), apresentado na Maratona de Programação SBC – ICPC Latin American Regional 2022.

---

## 📜 Enunciado resumido

Bella tem uma rotina simples e vai para o trabalho de ônibus, levando guarda-chuvas de casa para o trabalho ou vice-versa, dependendo das condições climáticas.

Para cada viagem (casa → trabalho e trabalho → casa) e para cada dia:

- Se estiver **chovendo**, Bella leva um guarda-chuva.
- Se não estiver chovendo, mas no **destino não houver guarda-chuvas**, Bella leva um por precaução.
- Caso contrário, Bella não leva guarda-chuva.

Sabendo o número inicial de guarda-chuvas em casa e no trabalho, e a sequência de chuvas para cada viagem ao longo de N dias, determine se Bella levou guarda-chuva em cada viagem.

---

## 🧠 Lógica da solução

Para cada dia e para cada viagem, avaliamos:

1. Se está chovendo:  
   Bella **leva um guarda-chuva** do local atual para o destino.  
   Atualizamos a quantidade de guarda-chuvas em casa e no trabalho.

2. Se não está chovendo:  
   Verificamos se no **destino** há guarda-chuvas.  
   - Se não houver, Bella leva um para evitar ficar sem guarda-chuva no futuro.  
   - Se houver, Bella não leva.

3. Imprimimos `Y` se Bella levou guarda-chuva e `N` caso contrário para cada viagem.

---

## ▶️ Como executar

### 🐍 Python

```bash
python3 passeios.py
```

### 📘 C99

```bash
gcc -std=c99 -o passeios passeios.c
./passeios
```