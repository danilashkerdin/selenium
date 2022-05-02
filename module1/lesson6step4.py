from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def main():
    link = "http://suninjuly.github.io/simple_form_find_task.html"
    browser = webdriver.Firefox()

    try:
        browser.get(link)

        inputs = browser.find_elements(By.TAG_NAME,"input")
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
