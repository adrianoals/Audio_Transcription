import moviepy.editor as mp
import speech_recognition as sr
from pydub import AudioSegment
import os

def extract_audio_from_video(video_path, audio_path):
    if not os.path.isfile(video_path):
        raise FileNotFoundError("O arquivo de vídeo não foi encontrado.")
    
    supported_formats = ['mp4', 'avi', 'mov', 'mkv', 'flv', 'wmv', 'mpeg']
    if not video_path.split('.')[-1] in supported_formats:
        raise ValueError("Formato de vídeo não suportado.")
    
    video = mp.VideoFileClip(video_path)
    video.audio.write_audiofile(audio_path)


def audio_to_text(audio_path):
    recognizer = sr.Recognizer()
    audio = AudioSegment.from_file(audio_path)
    audio.export("temp.wav", format="wav")
    
    with sr.AudioFile("temp.wav") as source:
        audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data, language="pt-BR")
        return text

if __name__ == "__main__":
    video_path = "1 - O que é Supabase.mp4"
    audio_path = "extraido_audio.wav"
    
    
    # Extrair áudio do vídeo
    extract_audio_from_video(video_path, audio_path)
    
    # Converter áudio em texto
    texto = audio_to_text(audio_path)
    print(texto)
