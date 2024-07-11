# functions.py

import moviepy.editor as mp
import speech_recognition as sr
from pydub import AudioSegment
from pydub.utils import make_chunks
import os

def extract_audio_from_video(video_path, audio_path):
    if not os.path.isfile(video_path):
        raise FileNotFoundError("O arquivo de vídeo não foi encontrado.")
    
    supported_formats = ['mp4', 'avi', 'mov', 'mkv', 'flv', 'wmv', 'mpeg']
    if not video_path.split('.')[-1] in supported_formats:
        raise ValueError("Formato de vídeo não suportado.")
    
    video = mp.VideoFileClip(video_path)
    os.makedirs(os.path.dirname(audio_path), exist_ok=True)
    video.audio.write_audiofile(audio_path)

def audio_to_text_in_chunks(audio_path, output_text_path, chunk_length_ms=120000, overlap_length_ms=5000):
    recognizer = sr.Recognizer()
    audio = AudioSegment.from_file(audio_path)
    chunks = make_chunks(audio, chunk_length_ms - overlap_length_ms)
    
    full_text = ""
    for i, chunk in enumerate(chunks):
        if i > 0:
            chunk = chunks[i-1][-overlap_length_ms:] + chunk
        
        chunk_filename = f"chunk{i}.wav"
        chunk.export(chunk_filename, format="wav")
        
        with sr.AudioFile(chunk_filename) as source:
            audio_data = recognizer.record(source)
            try:
                text = recognizer.recognize_google(audio_data, language="pt-BR")
                full_text += text + " "
            except sr.RequestError as e:
                print(f"Erro na requisição ao serviço de reconhecimento de fala: {e}")
            except sr.UnknownValueError:
                print("Não foi possível entender o áudio.")
            except Exception as e:
                print(f"Ocorreu um erro inesperado: {e}")
        
        # Remover chunk temporário para economizar espaço em disco
        os.remove(chunk_filename)
    
    # Escrever o texto completo em um arquivo .txt
    os.makedirs(os.path.dirname(output_text_path), exist_ok=True)
    with open(output_text_path, "w", encoding="utf-8") as text_file:
        text_file.write(full_text)
    
    return full_text
