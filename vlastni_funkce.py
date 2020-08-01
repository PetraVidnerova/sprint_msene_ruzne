# 0
import random


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


# 5
def hod_kostkou():
    pocet_pokusu = 0
    while True:
        pocet_pokusu += 1
        hod = random.randint(1, 6)
        #        hod = random.randrange(1, 7)
        #        hod = random.randrange(start=1, end=7)
        print("Hozeno ", hod)
        if hod == 6:
            break
    return pocet_pokusu


# 6
