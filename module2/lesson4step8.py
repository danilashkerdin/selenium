import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


def calc(x):
    return math.log(abs(12 * math.sin(x)))


def main():
    try:
        browser = webdriver.Firefox()
        browser.get("http://suninjuly.github.io/explicit_wait2.html")

        browser.implicitly_wait(5)
        button = WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable((By.ID, "book")))
        WebDriverWait(browser, 10).until(expected_conditions.text_to_be_present_in_element((By.ID, "price"), "$100"))
        button.click()

        x = int(browser.find_element(By.ID, "input_value").text)
        y = calc(x)
        browser.find_element(By.ID, "answer").send_keys(str(y))
        browser.find_element(By.ID, "solve").click()
    finally:
        time.sleep(40)
        browser.quit()


if __name__ == '__main__':
    main()
