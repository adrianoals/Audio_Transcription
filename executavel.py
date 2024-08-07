import whisper
import os
from tkinter import Tk, filedialog

def transcrever_audio():
    # Inicializar a janela do Tkinter
    root = Tk()
    root.withdraw()  # Esconder a janela principal

    # Abrir o diálogo para selecionar o arquivo de áudio
    audio_path = filedialog.askopenfilename(title="Selecione o arquivo de áudio")

    # Verificar se o arquivo foi selecionado
    if not audio_path:
        print("Nenhum arquivo selecionado.")
        return

    # Carregar o modelo Whisper
    modelo = whisper.load_model("medium")

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

if __name__ == "__main__":
    transcrever_audio()
