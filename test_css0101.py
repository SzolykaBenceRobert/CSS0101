import pytest
from bs4 import BeautifulSoup

@pytest.fixture
def load_html():
    with open("CSS0101.html", "r", encoding="utf-8") as file:
        return BeautifulSoup(file, "html.parser")

def test_small_caps(load_html):
    first_sentence = load_html.find("span", class_="small-caps")
    assert first_sentence is not None, "Az első mondat nincs kiskapitálisra állítva."

def test_underlined(load_html):
    second_sentence = load_html.find("span", class_="underlined")
    assert second_sentence is not None, "A második mondat nincs aláhúzva."

def test_large_text(load_html):
    third_sentence = load_html.find("span", class_="large-text")
    assert third_sentence is not None, "A harmadik mondat betűmérete nem 20 pixel."

def test_purple_text(load_html):
    fourth_sentence = load_html.find("span", class_="purple-text")
    assert fourth_sentence is not None, "A negyedik mondat betűszíne nem #800080."

def test_bold_text(load_html):
    fifth_sentence = load_html.find("span", class_="bold-text")
    assert fifth_sentence is not None, "Az ötödik mondat nincs félkövérre állítva."

def test_cursive_first_letter(load_html):
    sixth_sentence = load_html.find("span", class_="cursive-first-letter")
    assert sixth_sentence is not None, "A hatodik mondat első betűje nincs cursive-re állítva."

def test_shadowed_text(load_html):
    last_sentence = load_html.find("span", class_="shadowed-text")
    assert last_sentence is not None, "Az utolsó mondat betűi nincsenek árnyékolva."

def test_text_indent(load_html):
    paragraph = load_html.find("p")
    assert paragraph is not None, "A bekezdés nem létezik."
    assert "text-indent: 32px" in load_html.style.text, "A bekezdés első sora nem 32 pixeles behúzású."
