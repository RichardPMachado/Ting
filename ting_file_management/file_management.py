import sys


def txt_importer(file_path):
    try:
        if not file_path.endswith(".txt"):
            raise ValueError("Formato inválido")

        with open(file_path, "r") as file:
            lines = file.read().split("\n")
            return lines

    except FileNotFoundError:
        print(f"Arquivo {file_path} não encontrado", file=sys.stderr)

    except ValueError as e:
        print(str(e), file=sys.stderr)
