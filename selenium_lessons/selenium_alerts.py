from selenium import webdriver
import math
import time

# Работа с открытием новой вкладки

try:
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html")

    button = browser.find_element_by_tag_name("button")
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x = calc(int(browser.find_element_by_id("input_value").text))

    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys(str(x))

    button1 = browser.find_element_by_tag_name("button")
    button1.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
