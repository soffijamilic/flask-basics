import src.functions as f

def test_factorize():
    assert f.factorize(75) == [3, 5, 5]
    assert f.factorize(1) == []

def test_number_of_digits():
    assert f.number_of_digits(75) == 2
    assert f.number_of_digits(1) == 1
    assert f.number_of_digits(0) == 0