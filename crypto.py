import string

TABLE = string.ascii_letters + string.punctuation + string.digits + " "

def _shift_char(c: str, pas: int) -> str:
    if c not in TABLE:
        return c
    i = TABLE.index(c)
    return TABLE[(i + pas) % len(TABLE)]

def crypt(message: str, pas: int | None = None) -> str:
    """
    A) crypt(message) : décale de 1, pas de suffixe.
    B) crypt(message, pas) avec 1<=pas<=9 : décale de pas et concatène pas à la fin.
    """
    if pas is None:
        res = "".join(_shift_char(c, 1) for c in message)
        return res
    if not (1 <= int(pas) <= 9):
        raise ValueError("pas doit être un entier entre 1 et 9")
    res = "".join(_shift_char(c, int(pas)) for c in message)
    return f"{res}{int(pas)}"