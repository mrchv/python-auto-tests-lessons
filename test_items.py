import time

def test_basket_for_different_languages(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(10)
    basket_button = browser.find_element_by_class_name("btn-add-to-basket").text
    assert basket_button is not None, "Ошибочка вышла"
