# Referência:
# Rodrigo Coin Curvo: https://github.com/rodrigoccurvo
# github.com/tryber/sd-022-a-live-lectures/blob/lecture/cs/4.3/sorters/merge_sort.py
def merge_sort_string(string):
    """
    Divide string em substrings menores recursivamente até que
    possuam apenas 1 ou 0 caracteres e para cada uma das divisões
    chama função de ordenação
    """

    if len(string) <= 1:
        return string

    middle = len(string) // 2
    left = merge_sort_string(string[:middle])
    right = merge_sort_string(string[middle:])

    return merge(string, left, right)


def merge(string, left, right):
    """
    Recebe string e suas divisões, transforma-as em listas, faz ordenação
    de forma alfabética e retorna a string ordenada
    """
    print(f"string: {string}")

    left_index, right_index = 0, 0
    left_list, right_list, string_list = list(left), list(right), list(string)

    while left_index < len(left_list) and right_index < len(right_list):
        if left_list[left_index] <= right_list[right_index]:
            string_list[left_index + right_index] = left_list[left_index]
            left_index += 1
        else:
            string_list[left_index + right_index] = right_list[right_index]
            right_index += 1

    for left_index in range(left_index, len(left_list)):
        string_list[left_index + right_index] = left_list[left_index]

    for right_index in range(right_index, len(right_list)):
        string_list[left_index + right_index] = right_list[right_index]

    return "".join(string_list)


def is_anagram(first_string, second_string):
    if not first_string and not second_string:
        return (first_string, second_string, False)

    sorted_first = merge_sort_string(first_string.lower())
    sorted_second = merge_sort_string(second_string.lower())
    eqaul = sorted_first == sorted_second

    return (sorted_first, sorted_second, eqaul)
