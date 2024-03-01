from main import change_morse


def test_change():
    assert change_morse('TANISHQ') == ' - .- -. .. ... .... --.-'
    assert change_morse('12345') == ' .---- ..--- ...-- ....- .....'
