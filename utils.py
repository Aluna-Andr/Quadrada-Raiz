# utils.py

def salvar_em_arquivo(nome_arquivo, dados):
    with open(nome_arquivo, 'w') as f:
        for item in dados:
            f.write(f"{item}\n")

