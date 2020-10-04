


from hello import speak
from hello import add

def test_hello():
    assert "harsha" in speak("harsha")
    assert "vardhana" not in speak("harsha")


def test_add():
    assert 2 == add(1,1)
