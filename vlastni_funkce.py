# 0
def pocet_vterin(minuty, vteriny):
    return 60 * minuty + vteriny


# 1
def maximum_tri_cisel():
    a = input()
    b = input()
    if a > b:
        max = a
    else:
        max = b
    c = input()
    if c > max:
        max = c
    return max


# 2
def kolik_vratit(cena, hotovost):
    return hotovost - cena


# 4
def nakresli_obrazec():
    N = 6
    for radek in range(N):
        for sloupec in range(N):
            if (radek == 0 or radek == N-1 or sloupec == 0 or sloupec == N-1):
                print("X", end="")
            else:
                print(" ", end="")
        print()
