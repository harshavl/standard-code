


from hello import speak



def test_hello():
    assert "harsha" in speak("harsha")
    assert "vardhana" not in speak("harsha")

