import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class MyTestCase(unittest.TestCase):

    def test_1(self):
        link = "http://suninjuly.github.io/registration1.html"
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

        self.assertEqual("Congratulations! You have successfully registered!", browser.find_element(By.TAG_NAME, "h1").text)

        time.sleep(5)
        browser.quit()

    def test_2(self):
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

        self.assertEqual("Congratulations! You have successfully registered!", browser.find_element(By.TAG_NAME, "h1").text)

        time.sleep(5)
        browser.quit()


if __name__ == "__main__":
    unittest.main()
