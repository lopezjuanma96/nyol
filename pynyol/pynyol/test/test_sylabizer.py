from pynyol.sylabizer import sylabize

def test_sylable(sylable, validation):
    if len(sylables) != len(validation):
        return False
    return all([v == s for v, s in zip(validation, sylables)])

def test_sylabize(text, validation, **kwargs):
    return test_sylable(sylabize(text, **kwargs), validation)

if __name__ == "__main__":
    text = "mi mamá me mima, mi mamá me ama"
    validation = ["mi", "ma", "má", "me", "mi", "ma", ",", "mi", "ma", "má", "me", "a", "ma"]
    assert test_sylabize(text, validation), f"Error in sylabize: {sylabize(text)}"
