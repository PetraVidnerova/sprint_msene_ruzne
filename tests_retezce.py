from functools import partial
import pytest
import flexmock
import builtins

from retezce import *


# 0 nejde testovat
@pytest.mark.parametrize(["jmeno", "zena"],
                         [("Novák", False),
                          ("Nováková", True),
                          ("Brabenec", False),
                          ("Hrončok", False),
                          ("Nová", True)]
                         )
def test_uhodni_pohlavi(jmeno, zena):
    ret = uhodni_pohlavi(jmeno)
    assert ret in ("žena", "muž"), "Platná odpověď je pouze žena nebo muž."
    assert ret == "žena" or not zena


# 1
@pytest.mark.parametrize(["vstup", "vystup"],
                         [("8856022083", "XXXXXX2083"),
                          ("1234", "1234"),
                          ("12345", "X2345")]
                         )
def test_cenzuruj(vstup, vystup):
    assert cenzuruj(vstup) == vystup


@pytest.mark.parametrize(["text", "pocet"],
                         [("", 0),
                          ("Píseň bez hledaného písmene.", 0),
                          ("Píseň obsahující jedno K.", 1),
                          ("Píseň obsahující jedno k.", 1),
                          ("Pan Kaplan v kapli plakal.\n Od poklopu do poklopu Kyklop kouli koulí.", 9)]
                         )
def test_pocet_K(text, pocet):
    assert pocet_K(text) == pocet


@pytest.mark.parametrize(["vstup", "vystup"],
                         [("ano", True),
                          ("a", True),
                          ("Ano", True),
                          (" ano ", True),
                          ("aNo ", True),
                          ("ne", False),
                          ("n", False),
                          ("Ne", False),
                          ("NE", False),
                          (" nE ", False)]
                         )
def test_ano_nebo_ne(vstup, vystup):
    flexmock(builtins, input=lambda *args: vstup)
    assert ano_nebo_ne("otazka") == vystup


@pytest.mark.parametrize(["vstup", "vystup"],
                         [(["ano", "nen", "no", "xxx"], True),
                          (["NE", "nen", "no", "xxx"], False),
                          (["a", "...", "nen", "no", "xxx"], True)
                          ]
                         )
def test_ano_nebo_ne_nevim(vstup, vystup):

    def faked_input(*args, **kwargs):
        answers = kwargs["answers"]
        assert len(answers) > 0, "Vypadá to zacykleně."
        return answers.pop()

    flexmock(builtins, input=partial(faked_input, answers=vstup))
    assert ano_nebo_ne("otazka") == vystup
