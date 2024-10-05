# Transcrição de Áudio com Whisper

Este é um script em Python que extrai o áudio de um arquivo de vídeo ou áudio e realiza a transcrição do conteúdo falado usando o modelo [Whisper](https://github.com/openai/whisper) da OpenAI. O script gera um arquivo de texto com o resultado da transcrição.

Para a versão em inglês deste README, clique [aqui](README_EN.md).

## Requisitos

Para rodar este projeto, é necessário ter instalados:

- [Python 3.7+](https://www.python.org/downloads/)
- [ffmpeg](https://ffmpeg.org/download.html) (usado para manipulação de mídia)
- [PyTorch](https://pytorch.org/get-started/locally/)
- [Whisper](https://github.com/openai/whisper)

## Instalação

### 1. Instale o Whisper e outras dependências:
Você pode instalar o Whisper e o PyTorch diretamente pelo pip, além de instalar o `ffmpeg` no seu sistema. Execute os seguintes comandos:

```bash
pip install git+https://github.com/openai/whisper.git
pip install torch
```

### 2. Instale o `ffmpeg`:
Se estiver usando macOS, pode instalar via Homebrew:

```bash
brew install ffmpeg
```

Para outros sistemas operacionais, siga as instruções de instalação no site oficial do [FFmpeg](https://ffmpeg.org/download.html).

### 3. Clonar o projeto

Caso esteja utilizando este script em um repositório, clone o projeto:

```bash
git clone <url-do-repositorio>
cd <nome-do-diretorio>
```

## Uso

1. Coloque o arquivo de áudio ou vídeo que deseja transcrever na pasta `videoExtract/`.

2. Atualize o caminho do arquivo no script `audio_path` para corresponder ao nome do arquivo de áudio/vídeo.

3. Execute o script para iniciar a transcrição:

```bash
python main.py
```

O script irá carregar o modelo Whisper, transcrever o áudio e salvar a transcrição em um arquivo de texto localizado no diretório `textExtract/transcricao.txt`.

### Exemplo de Caminho

No script fornecido, o caminho para o arquivo de áudio é especificado da seguinte forma:

```python
audio_path = "videoExtract/videoExtract/nome_do_arquivo"
```

Altere esse caminho para o arquivo de áudio ou vídeo que deseja transcrever.

## Saída

A transcrição do áudio será salva no arquivo `textExtract/transcricao.txt`. 

O formato do arquivo será semelhante ao seguinte:

```
Este é um exemplo de transcrição gerado pelo modelo Whisper.
```

## Licença

Este projeto é licenciado sob a [MIT License](LICENSE).
