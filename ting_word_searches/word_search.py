def exists_word(word, instance):
    results = list()

    for file in range(len(instance)):
        file = instance.search(file)

        file_obj = {
                "palavra": word,
                "arquivo": file["nome_do_arquivo"],
                "ocorrencias": list(),
            }

        for index, line in enumerate(file["linhas_do_arquivo"]):
            if word.lower() in line.lower():
                file_obj["ocorrencias"].append({"linha": index + 1})

        if file_obj["ocorrencias"]:
            results.append(file_obj)

    return results


def search_by_word(word, instance):
    result = []
    for index in range(len(instance)):
        file = instance.search(index)
        lines = file["linhas_do_arquivo"]
        occurrences = [{"linha": line_num, "conteudo": line}
                       for line_num, line in enumerate(lines, start=1) if word
                       .lower() in line.lower()]
        if occurrences:
            result.append({
                "palavra": word,
                "arquivo": file["nome_do_arquivo"],
                "ocorrencias": occurrences
            })
    return result
