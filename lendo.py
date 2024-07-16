def contar_caracteres(arquivo):
    try:
        with open(arquivo, 'r', encoding='utf-8') as file:
            conteudo = file.read()
            numero_caracteres = len(conteudo)
            return numero_caracteres
    except Exception as e:
        return f"Erro ao ler o arquivo: {e}"

# Exemplo de uso:
arquivo_txt = 'textExtract/transcricao_Havai_1.txt'
numero_caracteres = contar_caracteres(arquivo_txt)
print(f"O número de caracteres no arquivo é: {numero_caracteres}")


def dividir_arquivo(arquivo, tamanho_parte=4000):
    try:
        with open(arquivo, 'r', encoding='utf-8') as file:
            conteudo = file.read()
            partes = [conteudo[i:i+tamanho_parte] for i in range(0, len(conteudo), tamanho_parte)]
            for idx, parte in enumerate(partes):
                with open(f'parte_{idx+1}.txt', 'w', encoding='utf-8') as parte_arquivo:
                    parte_arquivo.write(parte)
            print(f"Arquivo dividido em {len(partes)} partes.")
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")

# Exemplo de uso:
arquivo_txt = 'textExtract/transcricao_Havai_1.txt'
dividir_arquivo(arquivo_txt)
