def exists_word(word, instance, search_by_word=False):
    result = list()

    for item in instance._data:
        ocorrencias = list()

        for count, row in enumerate(item["linhas_do_arquivo"], start=1):

            if word.lower() in row.lower():
                ocorrencias.append(
                    {"linha": count, "conteudo": row}
                    if search_by_word
                    else {"linha": count}
                )

        if len(ocorrencias) > 0:
            result.append(
                {
                    "palavra": word,
                    "arquivo": item["nome_do_arquivo"],
                    "ocorrencias": ocorrencias,
                }
            )
    return result


def search_by_word(word, instance):
    return exists_word(word, instance, True)
