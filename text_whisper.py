# pip install git+https://github.com/openai/whisper.git
# pip install torch
# brew install ffmpeg

import whisper
import os

# Carregar o modelo Whisper
modelo = whisper.load_model("base")

# Caminho para o arquivo de áudio
audio_path = "caminho/para/seu_audio.wav"  # Substitua pelo caminho do seu arquivo de áudio

# Transcrever o arquivo de áudio
print("Transcrevendo áudio, isso pode levar algum tempo...")

# Transcrever o áudio com verbose para ver o progresso
resposta = modelo.transcribe(audio_path, verbose=True)

# Caminho para salvar o arquivo de texto
output_dir = "textExtract"
os.makedirs(output_dir, exist_ok=True)
output_file = os.path.join(output_dir, "transcricao.txt")

# Salvar o texto transcrito em um arquivo .txt
with open(output_file, "w", encoding="utf-8") as f:
    f.write(resposta["text"])

print(f"Transcrição concluída e salva em {output_file}")

