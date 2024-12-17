# 📜 **Sorteador de Apostas Aleatórias**

## 📌 **Descrição do Projeto**
Este script em **Python** realiza um sorteio aleatório de 11 números (e seus respectivos apostadores) a partir de um arquivo de entrada. Ele foi desenvolvido para auxiliar um grupo de apostadores, majoritariamente do **TL**, a organizar e visualizar seus resultados.

---

## ⚙️ **Como o Script Funciona**

1. **Leitura do Arquivo**  
   O script lê um arquivo de texto contendo os números e os nomes dos apostadores.

2. **Seleção Aleatória**  
   Utiliza a função `random.sample()` para escolher 11 linhas aleatórias, sem repetição.

3. **Exibição dos Resultados**  
   Os números sorteados e os respectivos apostadores são exibidos no terminal.

4. **Salvar em Arquivo**  
   Os resultados também são salvos em um novo arquivo chamado **`resultado_apostas.txt`** no mesmo diretório.

---

## 📂 **Formato do Arquivo de Entrada**

O arquivo de entrada deve conter uma lista com números e os nomes dos apostadores, separados por um hífen (`-`). Cada linha representa uma aposta.

### **Exemplo:**
```plaintext
11 - Alice
07 - Bob
13 - Carol
34 - David
57 - Eve
38 - Frank
15 - Grace
10 - Heidi
18 - Ivan
28 - Judy
42 - Kevin
16 - Larry
46 - Mallory
17 - Neil
37 - Oscar
26 - Peggy
04 - Quentin
24 - Ruth
```

---

## 📊 **Formato dos Dados Apresentados**

### **Exibição no Terminal**
Após a execução, os dados serão apresentados no terminal da seguinte forma:

```plaintext
Números sorteados e apostadores escolhidos:
11 - Alice
34 - David
07 - Bob
28 - Judy
42 - Kevin
10 - Heidi
46 - Mallory
04 - Quentin
38 - Frank
17 - Neil
15 - Grace

Os resultados foram salvos no arquivo 'resultado_apostas.txt'.
```

### **Arquivo Gerado (`resultado_apostas.txt`)**
Os mesmos resultados exibidos no terminal serão salvos em um arquivo para referência futura:

```plaintext
Números sorteados e apostadores escolhidos:
11 - Alice
34 - David
07 - Bob
28 - Judy
42 - Kevin
10 - Heidi
46 - Mallory
04 - Quentin
38 - Frank
17 - Neil
15 - Grace
```

---

## 🚀 **Execução do Script**

1. Salve o arquivo de entrada como **`apostas.txt`**.
2. Execute o script Python no terminal:

   ```bash
   python sorteador_apostas.py
   ```

3. Verifique os resultados no terminal e no arquivo **`resultado_apostas.txt`**.

---