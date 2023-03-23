def is_palindrome_iterative(word):
    """
    Retorna True caso palavra seja palíndromo e False caso não
    """
    if not word:
        return False

    for i in range(int(len(word) / 2)):
        if word[i] != word[len(word) - (1 + i)]:
            return False

    return True
