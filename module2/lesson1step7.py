import time
import math
import selenium
from selenium.webdriver.common.by import By


def calc(x):
    return math.log(abs(12 * math.sin(x)))


def main():
    link = "http://suninjuly.github.io/get_attribute.html"

    browser = selenium.webdriver.Firefox()
    try:
        browser.get(link)
        x = int(browser.find_element(By.ID, "treasure").get_attribute("valuex"))
        y = str(calc(x))
        browser.find_element(By.ID, "answer").send_keys(y)
        browser.find_element(By.ID, "robotCheckbox").click()
        browser.find_element(By.ID, "robotsRule").click()
        browser.find_element(By.CSS_SELECTOR, ".btn.btn-default").click()

    finally:
        time.sleep(30)
        browser.quit()


if __name__ == "__main__":
    main()
