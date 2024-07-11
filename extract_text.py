from functions import audio_to_text_in_chunks
import os

if __name__ == "__main__":
    audio_path = os.path.join("audioExtract", "extraido_audio.wav")
    output_text_path = os.path.join("textExtract", "extracted_text.txt")
    
    # Converter áudio em texto por partes
    print("Convertendo áudio em texto...")
    texto = audio_to_text_in_chunks(audio_path, output_text_path, chunk_length_ms=120000, overlap_length_ms=5000)
    if texto:
        print("Conversão concluída com sucesso.")
        print(f"Texto salvo em {output_text_path}.")
    else:
        print("A conversão falhou ou não foi possível entender o áudio.")
