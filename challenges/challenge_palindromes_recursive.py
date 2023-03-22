def is_palindrome_recursive(word, low_index, high_index):
    """
    Retorna True caso palavra seja palíndromo e False caso não
    """
    if not word:
        return False

    if low_index >= high_index:
        return True

    if word[low_index] != word[high_index]:
        return False

    return is_palindrome_recursive(word, low_index+1, high_index-1)
