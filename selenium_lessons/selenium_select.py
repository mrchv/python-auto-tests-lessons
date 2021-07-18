from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

# поиск значение в выпадающем списке

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/selects2.html")

    num1 = int(browser.find_element_by_id("num1").text)
    num2 = int(browser.find_element_by_id("num2").text)
    chislo = num1 + num2
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(str(chislo))

    # Отправляем заполненную форму
    button = browser.find_element_by_tag_name("button")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()