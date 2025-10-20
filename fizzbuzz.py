def _label(i: int) -> str:
    if i % 15 == 0:
        return "FrisBee"
    if i % 3 == 0:
        return "Fizz"
    if i % 5 == 0:
        return "Buzz"
    return str(i)

def affiche(*args) -> str:
    if len(args) == 0:
        start, end = 1, 100
    elif len(args) == 1:
        n = int(args[0])
        start, end = 1, n
    elif len(args) == 2:
        start, end = int(args[0]), int(args[1])
    else:
        raise TypeError("affiche() accepte 0, 1 ou 2 paramètres")

    return "".join(_label(i) for i in range(start, end + 1))