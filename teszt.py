from feladatok import egyedi_betuk

def test_egyedi_betuk():
    assert egyedi_betuk("abc") == ['a', 'b', 'c']
    assert egyedi_betuk("sikerült") == ['e', 'i', 'k', 'l', 'r', 's', 't', 'ü']
    assert egyedi_betuk("Helo, Világ!") == ['e', 'g', 'h', 'i', 'l', 'v', 'á', 'ó']
    assert egyedi_betuk("Python 3.12") == ['h', 'n', 'o', 'p', 't', 'y']
    assert egyedi_betuk("Árvíztűrő tükörfúrógép") == ['f', 'g', 'k', 'p', 'r', 't', 'v', 'z', 'á', 'é', 'í', 'ó', 'ö', 'ú', 'ü', 'ő', 'ű']
    assert egyedi_betuk("") == []
    print("Minden teszt lefutott")


test_egyedi_betuk()
