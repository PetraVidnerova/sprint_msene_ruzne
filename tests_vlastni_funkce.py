import pytest
import flexmock
import builtins
import io
from functools import partial
import random

from vlastni_funkce import pocet_vterin, maximum_tri_cisel, kolik_vratit, nakresli_obrazec, hod_kostkou

# 0


@pytest.mark.parametrize(['cena', 'hotovost', 'vysledek'],
                         [(942, 950, 8),
                          (997, 1000, 3),
                          (494, 500, 6)]
                         )
def test_kolik_vratit(cena, hotovost, vysledek):
    return kolik_vratit(cena, hotovost) == vysledek

# 1


@pytest.mark.parametrize(['minuty', 'vteriny', 'vysledek'],
                         [(10, 0, 600),
                          (0, 0, 0),
                          (0, 10, 10),
                          (3, 5, 185)]
                         )
def test_pocet_vterin(minuty, vteriny, vysledek):
    vraceno = pocet_vterin(minuty, vteriny)
    assert vraceno == vysledek


# 2
@pytest.mark.parametrize(['values', 'result'],
                         [([5, 8, 6], 8),
                          ([1, 2, 3], 3),
                          ([6, 5, 4], 6)]
                         )
def test_maximum_tri_cisel(values, result):
    flexmock(builtins, input=values.pop)
    assert maximum_tri_cisel() == result

# 3
# NO TESTS

# 4


def test_nakresli_obrazec():
    N = 6
    kraje = ("X X X X X X", "XXXXXX")
    vnitrek = ("X         X", "X    X")
    vytvoreny_retezec = io.StringIO()
    flexmock(builtins, print=partial(print, file=vytvoreny_retezec))
    nakresli_obrazec()
    radky = list(vytvoreny_retezec.getvalue().split("\n"))
    assert len(radky) > 0
    assert radky[0].rstrip() in kraje, f"'{radky[0]}' by mělo obsahovat 6 X"
    assert radky[N-1].rstrip() in kraje, f"'{radky[N-1]}' by mělo obsahovat 6 X"
    for r in range(1, N-1):
        assert radky[r].rstrip() in vnitrek, f"{radky[r]} (radek {r}) má obsahovat X jen na konci nebo na začátku"
    for r in range(1, N):
        assert len(radky[r-1].rstrip()) == len(radky[r].rstrip())
    for r in range(N, len(radky)):
        assert radky[r].strip() == ""


# 5
@pytest.mark.parametrize('result', [1, 2, 5, 6, 8, 9])
def hod_kostkou(result):
    pocet_hodu = result

    def my_random(name=None, *args, **kwargs):
        result = result - 1
        if result == 0:
            return 6
        else:
            return random.randrange(1, 6)

    flexmock(random, randrange=partial(my_random, name="randrange"))
    flexmock(random, randint=partial(my_random, name="randint"))

    odpoved = hod_kostkou()
    assert odpoved == result
