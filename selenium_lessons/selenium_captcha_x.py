from selenium import webdriver
import math
import time

# автозаполнение формы с поиском значения по атрибуту
try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/get_attribute.html")

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    sunduk = browser.find_element_by_tag_name("img")
    x_sunduk = int(sunduk.get_attribute("valuex"))
    chislo = calc(x_sunduk)
    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys(str(chislo))

    # Отмечаем чекбокс
    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()

    option2 = browser.find_element_by_id("robotsRule")
    option2.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_tag_name("button")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
