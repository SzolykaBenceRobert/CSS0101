import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    driver = webdriver.Chrome()  # Vagy bármely más WebDriver
    driver.get("path_to_your_html_file.html")  # Az elérési út a HTML fájlhoz
    yield driver
    driver.quit()

def test_first_sentence_is_small_caps(driver):
    first_paragraph = driver.find_elements_by_tag_name("p")[0]
    style = first_paragraph.value_of_css_property("font-variant")
    assert style == "small-caps"

def test_second_sentence_is_underlined(driver):
    second_paragraph = driver.find_elements_by_tag_name("p")[1]
    style = second_paragraph.value_of_css_property("text-decoration")
    assert "underline" in style

def test_third_sentence_font_size(driver):
    third_paragraph = driver.find_elements_by_tag_name("p")[2]
    font_size = third_paragraph.value_of_css_property("font-size")
    assert font_size == "20px"

def test_fourth_sentence_font_color(driver):
    fourth_paragraph = driver.find_elements_by_tag_name("p")[3]
    color = fourth_paragraph.value_of_css_property("color")
    assert color == "rgb(128, 0, 128)"  # #800080

def test_fifth_sentence_is_bold(driver):
    fifth_paragraph = driver.find_elements_by_tag_name("p")[4]
    font_weight = fifth_paragraph.value_of_css_property("font-weight")
    assert font_weight == "700"  # Bold font weight

def test_sixth_sentence_first_letter_is_cursive(driver):
    sixth_paragraph = driver.find_elements_by_tag_name("p")[5]
    first_letter_style = sixth_paragraph.find_element_by_css_selector("::first-letter").value_of_css_property("font-family")
    assert first_letter_style == "cursive"

def test_last_sentence_has_text_shadow(driver):
    last_paragraph = driver.find_elements_by_tag_name("p")[-1]
    text_shadow = last_paragraph.value_of_css_property("text-shadow")
    assert "2px 2px 4px" in text_shadow
