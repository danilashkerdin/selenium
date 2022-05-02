import os
import time

import selenium
from selenium.webdriver.common.by import By


def main():
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'Hello-world.txt')
    print(path)

    browser = selenium.webdriver.Firefox()
    try:
        browser.get("http://suninjuly.github.io/file_input.html")
        firstname = browser.find_element(By.CSS_SELECTOR, "input.form-control[required=\"\"][name=\"firstname\"]")
        lastname = browser.find_element(By.CSS_SELECTOR, "input.form-control[required=\"\"][name=\"lastname\"]")
        email = browser.find_element(By.CSS_SELECTOR, "input.form-control[required=\"\"][name=\"email\"]")
        file = browser.find_element(By.ID, "file")

        firstname.send_keys("Danila")
        lastname.send_keys("Shkerdin")
        email.send_keys("danil@mail.ru")
        file.send_keys(path)

        browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()
    finally:
        time.sleep(20)
        browser.quit()


if __name__ == "__main__":
    main()
