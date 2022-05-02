import math
import selenium
from selenium.webdriver.common.by import By
import time


def main():
    browser = selenium.webdriver.Firefox()
    browser.get("http://suninjuly.github.io/find_link_text")
    browser.find_element(By.LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e)*10000))).click()
    try:

        inputs = browser.find_elements(By.TAG_NAME, "input")
        inputs[0].send_keys("Danila")
        inputs[1].send_keys("Shkerdin")
        inputs[2].send_keys("Orel")
        inputs[3].send_keys("Russia")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

    finally:
        time.sleep(30)
        browser.quit()


if __name__ == "__main__":
    main()
