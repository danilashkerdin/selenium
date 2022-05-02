import time
import math
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def main():
    link = "http://suninjuly.github.io/selects1.html"

    browser = selenium.webdriver.Firefox()
    try:
        browser.get(link)
        x = int(browser.find_element(By.ID, "num1").text)
        y = int(browser.find_element(By.ID, "num2").text)
        select = Select(browser.find_element(By.ID, "dropdown"))
        select.select_by_value(str(x+y))
        browser.find_element(By.CSS_SELECTOR, ".btn.btn-default").click()

    finally:
        time.sleep(30)
        browser.quit()


if __name__ == "__main__":
    main()
