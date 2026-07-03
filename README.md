# calculo-linha-estimulo
# Cálculo de Linhas de Estímulo de Redução de Velocidade (LRV)

Este projeto em Python automatiza o cálculo geométrico para a implantação de **Linhas de Estímulo de Redução de Velocidade (LRV)**, um tipo de sinalização horizontal utilizada para induzir o condutor a desacelerar de forma natural.

## 📌 Como o Cálculo Funciona

O script utiliza conceitos físicos e normas de trânsito para determinar:
1. **Quantidade total de linhas** necessárias para o trecho.
2. **Largura ideal das faixas** (0,20m, 0,30m ou 0,40m) com base na velocidade regulamentada da via.
3. **Espaçamento acumulado ($E_i$)** de cada linha até o início do trecho.
4. **Distância entre linhas consecutivas**, que vai encurtando para dar a ilusão de ganho de velocidade.

## 🚀 Como Executar

1. Certifique-se de ter o Python instalado no seu computador.
2. Clone este repositório ou baixe o arquivo `lrv.py`.
3. Execute o script:
   ```bash
   python lrv.py
