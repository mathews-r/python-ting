def exists_word(word, instance):
    result = list()

    for item in instance._data:
        ocorrencias = list()
        for count, row in enumerate(item["linhas_do_arquivo"], start=1):
            if word.lower() in row.lower():
                ocorrencias.append({"linha": count})

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
    result = list()

    for item in instance._data:
        ocorrencias = list()
        for count, row in enumerate(item["linhas_do_arquivo"], start=1):
            if word.lower() in row.lower():
                ocorrencias.append({"linha": count, "conteudo": row})

        if len(ocorrencias) > 0:
            result.append(
                {
                    "palavra": word,
                    "arquivo": item["nome_do_arquivo"],
                    "ocorrencias": ocorrencias,
                }
            )
    return result
