from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def main():

    try:
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        first_name = browser.find_element(By.CSS_SELECTOR, "input.first[required=\"\"]")
        last_name = browser.find_element(By.CSS_SELECTOR, "input.second[required=\"\"]")
        email = browser.find_element(By.CSS_SELECTOR, "input.third[required=\"\"]")

        first_name.send_keys("Danila")
        last_name.send_keys("Shkerdin")
        email.send_keys("danila.shkerdin.01@mail.ru")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(1)
        assert "Congratulations! You have successfully registered!" == browser.find_element(By.TAG_NAME, "h1").text

    except Exception as e:
        print(e)

    finally:
        time.sleep(10)
        browser.quit()


if __name__ == "__main__":
    main()
