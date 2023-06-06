import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for index in range(len(instance)):
        if instance.search(index)["nome_do_arquivo"] == path_file:
            return None

    lines = txt_importer(path_file)

    data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(lines),
        "linhas_do_arquivo": lines
    }
    instance.enqueue(data)
    sys.stdout.write(str(data))


def remove(instance):
    try:
        information = instance.dequeue()
    except IndexError:
        print("Não há elementos", file=sys.stdout)
    else:
        path_file = information["nome_do_arquivo"]
        print(f"Arquivo {path_file} removido com sucesso", file=sys.stdout)


def file_metadata(instance, position):
    try:
        file = instance.search(position)
        print(file, file=sys.stdout)
    except IndexError:
        print("Posição inválida", file=sys.stderr)
