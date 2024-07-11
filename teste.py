import openai

# Defina sua chave de API diretamente no código
openai.api_key = 'sk-proj-uyJlz1Ivup52SlHTA82bT3BlbkFJhMOzh4WHblRgiGEASDVW'

# Abra o arquivo de áudio
audio_file = open("audioExtract/extraido_audio.wav", "rb")

# Faça a transcrição do áudio usando o modelo "whisper-1"
transcription = openai.Audio.transcriptions.create(
    model="whisper-1",
    file=audio_file
)

# Imprima o texto transcrito
print(transcription['text'])


# from openai import OpenAI
# client = OpenAI()

# audio_file= open("/audioExtract/extraido_audio.wav", "rb")
# transcription = client.audio.transcriptions.create(
#   model="whisper-1", 
#   file=audio_file
# )
# print(transcription.text)