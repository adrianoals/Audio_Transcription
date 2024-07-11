from functions import extract_audio_from_video
import os

if __name__ == "__main__":
    video_path = os.path.join("videoExtract", "1 - O que é Supabase.mp4")
    audio_path = os.path.join("audioExtract", "extraido_audio.wav")
    
    # Extrair áudio do vídeo
    print("Extraindo áudio do vídeo...")
    extract_audio_from_video(video_path, audio_path)
    print(f"Áudio extraído com sucesso e salvo em {audio_path}.")
