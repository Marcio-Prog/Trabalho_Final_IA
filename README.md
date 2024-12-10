# Contador de Veículos com OpenCV

Este projeto é um contador de veículos que utiliza visão computacional para detectar e contar carros que passam por uma linha horizontal em um vídeo. 

O sistema usa a técnica de subtração de fundo para identificar os objetos em movimento e processa cada contorno detectado para determinar se corresponde a um veículo.

## Funcionalidades

- Detecção de veículos em movimento em um vídeo.
- Contagem de veículos ao cruzarem uma linha horizontal definida.
- Visualização em tempo real do vídeo processado, incluindo:
  - Máscara da subtração de fundo.
  - Retângulos em volta dos veículos detectados.
  - Linha de contagem e número total de veículos na tela.

## Requisitos

- Python 3.x
- OpenCV

Para instalar o OpenCV, execute:

```bash
pip install opencv-python opencv-python-headless
```

## Parâmetros Principais

- **`MIN_AREA_CARRO`**: Define a área mínima para que um contorno seja considerado um veículo.
- **`LINHA_DETECTORA`**: Posição vertical (em pixels) da linha de contagem.
- **`OFFSET`**: Tolerância de interseção com a linha de contagem.
- **`CARROS_CONTADOS`**: Contador que armazena o número total de veículos detectados.

## Arquivo de Vídeo

Substitua `rodovia.mov` pelo caminho do seu vídeo.

## Como Executar

1. Certifique-se de ter instalado todas as dependências.
2. Substitua o caminho do vídeo em `video_path` para o arquivo desejado.
3. Execute o script com o comando:

   ```bash
   python contador_de_veiculos.py
   ```

4. Pressione `q` para encerrar a execução.

## Funções Principais

### `calcula_centroide(x, y, w, h)`

Calcula o ponto central de um retângulo baseado nas coordenadas e dimensões fornecidas.

### `desenha_info(frame, carros)`

Desenha a linha de contagem e exibe o número de veículos detectados no vídeo.

### `main()`


Função principal que:

- Carrega o vídeo.
- Aplica a subtração de fundo para segmentação.
- Identifica e processa contornos para detectar veículos.
- Atualiza e exibe as informações de contagem.

## Observações

- Para melhorar a precisão, ajuste os parâmetros de área mínima (`MIN_AREA_CARRO`) e a tolerância (`OFFSET`) conforme necessário.
- O código foi testado em vídeos de estradas e pode precisar de ajustes para cenários diferentes.

## Exemplo de Saída

- Uma janela exibindo o vídeo com:
  - Veículos identificados em tempo real.
  - Linha de contagem horizontal.
  - Número total de veículos detectados.
- Outra janela exibindo a máscara de subtração de fundo.

## Link para o video
https://drive.google.com/file/d/1BLfvjqj5O3fBjWBtE75EP8aVxeeL4Rmn/view?usp=sharing

