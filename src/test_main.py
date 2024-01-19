import main


def test_is_adult():
    age = 18
    result = main.is_adult(age)
    assert result
    assert main.is_adult(20)


def test_is_not_adult():
    assert not main.is_adult(17)
    assert not main.is_adult(19)
