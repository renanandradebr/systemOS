import os

def listar_arquivos(diretorio):
    arquivos = os.listdir(diretorio)
    for arquivo in arquivos:
        print(arquivo)

def criar_pasta(nome_pasta):
    try:
        os.mkdir(nome_pasta)
        print(f"Pasta '{nome_pasta}' criada com sucesso.")
    except FileExistsError:
        print(f"A pasta '{nome_pasta}' já existe.")

def interpretador_comandos():
    while True:
        comando = input("Digite um comando (listar/criar/sair): ").strip().lower()

        if comando == "listar":
            diretorio = input("Digite o diretório que deseja listar (ou deixe em branco para o diretório atual): ").strip() or "."
            listar_arquivos(diretorio)
        elif comando == "criar":
            nome_pasta = input("Digite o nome da pasta que deseja criar: ").strip()
            criar_pasta(nome_pasta)
        elif comando == "sair":
            print("Encerrando o interpretador de comandos...")
            break
        else:
            print("Comando inválido. Por favor, tente novamente.")

if __name__ == "__main__":
    interpretador_comandos()
