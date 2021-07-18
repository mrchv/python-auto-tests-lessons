from selenium import webdriver
import math
import time


# автозаполнение формы с динамической капчей
try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/math.html")

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    chislo = calc(browser.find_element_by_id("input_value").text)
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
