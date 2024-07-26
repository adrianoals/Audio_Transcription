# pip install git+https://github.com/openai/whisper.git
# pip install torch
# brew install ffmpeg

import os
import whisper

# Carregar o modelo Whisper
modelo = whisper.load_model("medium")

# Lista de arquivos de áudio
arquivos = [
    "1 - O que é Supabase.mp4",
    "2 - Criando uma conta gratuita no Supabase.mp4",
    "3 - Criando nosso primeiro projeto.mp4",
    "4 - Painel de controle do Supabase.mp4",
    "5 - Relacionamento entre tabelas.mp4",
    "6 - Importância dos relacionamentos para otimização de dados.mp4",
    "7 - Tipos de Dados Aceitos pelo Supabase.mp4",
    "8 - Tipos Numéricos.mp4",
    "9 - Tipos de Texto.mp4",
    "10 - Tipos de Dados Temporais.mp4",
    "11 - Tipos de Dados Estruturados ou Semi-Estruturados.mp4",
    "12 - Tipos Lógicos e Outros Tipos.mp4",
    "13 - Criando nossa primeira tabela.mp4",
    "14 - Editando a tabela pelo Supabase.mp4",
    "15 - Inserindo manualmente, registros na tabela.mp4",
    "16 - Inserindo registros na tabela via Importação CSV.mp4",
    "17 - Modificando registros na tabela.mp4",
    "18 - Deletando registros na tabela.mp4",
    "19 - Desafio - Replique a Estrutura de Dados da Aula.mp4",
    "20 - Implementando Relacionamentos entre tabelas.mp4",
    "21 - Validando a Implementação dos Relacionamentos.mp4",
    "22 - Exclusão de Relacionamentos para Manutenção de Campos em Tabelas.mp4",
    "23 - O que são Views em um banco de dados relacional.mp4",
    "24 - Criando nossa Primeira View Chat GPT.mp4",
    "25 - Criando views que respeitem as regras de segurança (RLS).mp4",
    "26 - Encapsulamento de Cálculos e Transformações de Dados.mp4",
    "27 - Como Excluir uma View.mp4",
    "28 - Administração de Usuários no Supabase.mp4",
    "29 - Criar a tabela users espelho para o Schema Public.mp4",
    "30 - Cadastro de usuários Via API.mp4",
    "31 - Criar user em public - Manualmente.mp4",
    "32 - Deslogar o usuário.mp4",
    "33 - Login de usuário.mp4",
    "34 - Templates de E-mails para Administração de Usuários.mp4",
    "35 - Confirmar a criação de Conta por E-mail.mp4",
    "36 - Configurações SMTP para e-mails transacionais.mp4"
]

# Caminho para a pasta dos arquivos de áudio
caminho_pasta = "/Users/adriano/Documents/SUPABASE/SUPABASE_VÍDEOS"

# Caminho para salvar os arquivos de texto
output_dir = "textExtract"
os.makedirs(output_dir, exist_ok=True)

# Função para transcrever o áudio e salvar o texto
def transcrever_audio(arquivo_audio):
    print(f"Transcrevendo {arquivo_audio}, isso pode levar algum tempo...")
    resposta = modelo.transcribe(os.path.join(caminho_pasta, arquivo_audio), verbose=True)
    nome_arquivo_txt = os.path.splitext(arquivo_audio)[0] + ".txt"
    output_file = os.path.join(output_dir, nome_arquivo_txt)
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(resposta["text"])
    print(f"Transcrição concluída e salva em {output_file}")

# Iterar sobre os arquivos e transcrever o áudio
for arquivo in arquivos:
    transcrever_audio(arquivo)

