def is_palindrome_iterative(word):
    """Faça o código aqui."""
    if word == "":
        return False

    length = len(word)
    first = 0
    last = length - 1
    it_is = True
    while first < last:
        if word[first] == word[last]:
            first = first + 1
            last = last - 1
        else:
            it_is = False
            break
    return it_is
