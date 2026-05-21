import NFA

def test_accepts_aa():
    a = NFA.NFA("aa|b*")
    assert a.validate_string("aa") is True

def test_accepts_b():
    a = NFA.NFA("aa|b*")
    assert a.validate_string("b") is True


def test_accepts_ab():
    a = NFA.NFA("ab")
    assert a.validate_string("ab") is True

def test_accepts_many_bs():
    a = NFA.NFA("aa|b*")
    assert a.validate_string("bbbb") is True

def test_accepts_empty():
    a = NFA.NFA("aa|b*")
    assert a.validate_string("") is True

def test_rejects_c():
    a = NFA.NFA("aa|b*")
    assert a.validate_string("c") is False

def test_rejects_ab():
    a = NFA.NFA("aa|b*")
    assert a.validate_string("ab") is False