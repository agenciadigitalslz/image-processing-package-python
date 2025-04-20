# Image Processing Package in Python for DIO

## Descrição
O pacote `image_processing_dio` é usado para:
- Processamento de imagens digitais utilizando Skimage
- Módulo de Utils: carregamento, salvamento e visualização de imagens
- Módulo de Processing: corresponde ao processamento de imagens, como:
  - Transformação de imagens (redimensionamento)
  - Combinação de imagens (diferença estrutural, transferência de histograma)

## Instalação

Use o gerenciador de pacotes [pip](https://pip.pypa.io/en/stable/) para instalar image_processing_dio

```bash
pip install image_processing_dio
```

## Uso

```python
# Importando funções de processamento de imagens
from image_processing.processing.transformation import resize_image
from image_processing.processing.combination import find_difference, transfer_histogram

# Importando utilitários para manipulação de imagens
from image_processing.utils.io import read_image, save_image
from image_processing.utils.plot import plot_image, plot_result, plot_histogram

# Exemplo de uso
imagem = read_image('caminho/para/imagem.jpg')
imagem_redimensionada = resize_image(imagem, 0.5)
plot_image(imagem_redimensionada)
```

## Autor
André Lopes

## Licença
[MIT](https://choosealicense.com/licenses/mit/)