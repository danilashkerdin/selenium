from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def main():

    try:
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        first_name = browser.find_element(By.CSS_SELECTOR, "input.first[required=\"\"]")
        last_name = browser.find_element(By.CSS_SELECTOR, "input.second[required=\"\"]")
        email = browser.find_element(By.CSS_SELECTOR, "input.third[required=\"\"]")

        first_name.send_keys("Danila")
        last_name.send_keys("Shkerdin")
        email.send_keys("email@mail.ru")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(1)
        assert "Congratulations! You have successfully registered!" == browser.find_element(By.TAG_NAME, "h1").text

    finally:
        time.sleep(10)
        browser.quit()


if __name__ == "__main__":
    main()
