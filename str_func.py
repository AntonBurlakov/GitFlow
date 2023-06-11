def func(word):
    """
    13213
    """

    return word.upper()


def func_2(word):
    """

    :param word:
    :return:
    """
    words_list = word.split()
    result = []
    for word in words_list:
        result.append(word.capitallize())
    return ' '.join(result)
