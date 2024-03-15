import unigestor


def test_hola():
    assert unigestor.hi() == "¡Hola!"


def test_hola_bis():
    assert unigestor.hi() is not "¡Hola!"
