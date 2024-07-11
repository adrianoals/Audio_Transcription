import openai

# Defina sua chave de API diretamente no código
openai.api_key = 'sk-proj-uyJlz1Ivup52SlHTA82bT3BlbkFJhMOzh4WHblRgiGEASDVW'

# Função para transcrever o áudio
def transcribe(audio_file_path):
    with open(audio_file_path, "rb") as audio_file:
        transcription = openai.Audio.transcriptions.create(
            model="whisper-1",
            file=audio_file,
            response_format="text"
        )
    return transcription['text']

# Função para corrigir a transcrição usando GPT-4
def generate_corrected_transcript(temperature, system_prompt, transcribed_text):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        temperature=temperature,
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": transcribed_text
            }
        ]
    )
    return response['choices'][0]['message']['content']

# Caminho para o arquivo de áudio
audio_file_path = "audioExtract/extraido_audio.wav"

# Realizar a transcrição
transcribed_text = transcribe(audio_file_path)
print("Transcrição Original:\n", transcribed_text)

# Prompt para o GPT-4
system_prompt = (
    "You are a helpful assistant for the company ZyntriQix. Your task is to correct any spelling discrepancies "
    "in the transcribed text. Make sure that the names of the following products are spelled correctly: ZyntriQix, "
    "Digique Plus, CynapseFive, VortiQore V8, EchoNix Array, OrbitalLink Seven, DigiFractal Matrix, PULSE, RAPT, "
    "B.R.I.C.K., Q.U.A.R.T.Z., F.L.I.N.T. Only add necessary punctuation such as periods, commas, and capitalization, "
    "and use only the context provided."
)

# Corrigir a transcrição usando GPT-4
corrected_text = generate_corrected_transcript(0, system_prompt, transcribed_text)
print("Transcrição Corrigida:\n", corrected_text)

# Salvar a transcrição corrigida em um arquivo de texto
output_text_path = "textExtract/corrected_transcription.txt"
with open(output_text_path, "w", encoding="utf-8") as text_file:
    text_file.write(corrected_text)
