def uhodni_pohlavi(jmeno):
    if jmeno[-1] == "á":
        return "žena"
    else:
        return "muž"


def cenzuruj(ciselny_retezec):
    delka_x = len(ciselny_retezec) - 4
    return "X" * delka_x + ciselny_retezec[-4:]


def pocet_K(pisen):
    return pisen.upper().count('K')


def ano_nebo_ne(otazka):
    while True:
        odpoved = input(otazka)
        odpoved = odpoved.strip().lower()
        if odpoved in ('ano', 'a'):
            return True
        elif odpoved in ('ne', 'n'):
            return False
        else:
            print('Nerozumím! Odpověz "ano" nebo "ne".')


def vyhodnot(pole):
    if "xxx" in pole:
        return "x"

    if "ooo" in pole:
        return "o"

    if "-" not in pole:
        return "!"

    return "-"


# dalsi testy uz existujou
