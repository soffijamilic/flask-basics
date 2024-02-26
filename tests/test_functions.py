import src.functions as f

def test_factorize():
    assert f.factorize(75) == [3, 5, 5]
    assert f.factorize(1) == []
    