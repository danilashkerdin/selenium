import math
import time
import selenium
from selenium.webdriver.common.by import By


def calc(x):
    return math.log(abs(12 * math.sin(x)))


def main():
    browser = selenium.webdriver.Firefox()

    try:
        browser.get("http://suninjuly.github.io/alert_accept.html")
        browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()
        prompt = browser.switch_to.alert
        prompt.accept()

        time.sleep(2)
        browser.refresh()

        x = int(browser.find_element(By.ID, "input_value").text)
        y = calc(x)
        browser.find_element(By.ID, "answer").send_keys(str(y))
        browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()

    finally:
        time.sleep(20)
        browser.quit()


if __name__ == "__main__":
    main()
