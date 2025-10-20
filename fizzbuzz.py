def affiche(n: int = 100) -> str:
    s = ""
    for i in range(1, n + 1):
        if i % 15 == 0:
            s += "FrisBee"
        elif i % 3 == 0:
            s += "Fizz"
        elif i % 5 == 0:
            s += "Buzz"
        else:
            s += str(i)
    return s
