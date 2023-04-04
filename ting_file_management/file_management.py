import sys


def txt_importer(path_file):
    if not path_file.endswith(".txt"):
        sys.stderr.write("Formato inválido")
    try:
        with open(
            path_file,
            mode="r",
        ) as file:
            data = file.readlines()
        data = [line.rstrip("\n") for line in data]
        return data
    except FileNotFoundError:
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")


# Referencia
# https://horadecodar.com.br/2021/03/13/como-ler-um-arquivo-linha-por-linha-em-uma-lista-python/
