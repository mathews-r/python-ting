from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    for path in instance._data:
        if path_file in path["nome_do_arquivo"]:
            return None

    dict_path = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(txt_importer(path_file)),
        "linhas_do_arquivo": txt_importer(path_file),
    }

    instance.enqueue(dict_path)
    print(dict_path, file=sys.stdout)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
