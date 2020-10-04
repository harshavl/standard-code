


from hello import speak
from hello import add, compare_names

def test_hello():
    assert "harsha" in speak("harsha")
    assert "vardhana" not in speak("harsha")


def test_add():
    assert 2 == add(1,1)


def test_compare_names():
    assert True == compare_names("harsha", "harsha" )

