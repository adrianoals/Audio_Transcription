# https://www.hashtagtreinamentos.com/como-transcrever-audio-com-python
# pip install tqdm - Biblioteca para barra de progresso
# import whisper
# modelo = whisper.load_model("small")
# resposta = modelo.transcribe("audioExtract/extraido_audio.wav")
# print(resposta['text'])

import whisper
from tqdm import tqdm
import os

# Carregar o modelo Whisper
modelo = whisper.load_model("medium")

# Caminho para o arquivo de áudio
audio_path = "audioExtract/extraido_audio.wav"

# Transcrever o arquivo de áudio com barra de progresso
print("Transcrevendo áudio, isso pode levar algum tempo...")

# Carregar e processar o áudio
resposta = modelo.transcribe(audio_path, verbose=True)

# Caminho para salvar o arquivo de texto
output_dir = "textExtract"
os.makedirs(output_dir, exist_ok=True)
output_file = os.path.join(output_dir, "transcricao.txt")

# Salvar o texto transcrito em um arquivo .txt
with open(output_file, "w", encoding="utf-8") as f:
    f.write(resposta["text"])

print(f"Transcrição concluída e salva em {output_file}")
