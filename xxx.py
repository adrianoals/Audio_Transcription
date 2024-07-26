import os

# Defina o caminho da pasta
pasta = "/Users/adriano/Documents/SUPABASE/SUPABASE_VÍDEOS"

# Lista para armazenar os nomes dos arquivos
lista_arquivos = []

# Iterar sobre os arquivos na pasta
for nome_arquivo in os.listdir(pasta):
    # Verifica se é um arquivo (ignora diretórios)
    if os.path.isfile(os.path.join(pasta, nome_arquivo)):
        lista_arquivos.append(nome_arquivo)

# Exibe a lista de arquivos no console
for arquivo in lista_arquivos:
    print(arquivo)

print()
print(lista_arquivos)