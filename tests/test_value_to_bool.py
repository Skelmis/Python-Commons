from commons import value_to_bool


def test_value_to_bool():
    assert value_to_bool("True") is True
    assert value_to_bool("False") is False
    assert value_to_bool("0") is False
    assert value_to_bool("1") is True
    assert value_to_bool(False) is False
    assert value_to_bool(0) is False
    assert value_to_bool(None) is False
    assert value_to_bool("") is False
    assert value_to_bool(1) is True
