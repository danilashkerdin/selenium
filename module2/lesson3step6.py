import math
import time
import selenium
from selenium.webdriver.common.by import By


def calc(x):
    return math.log(abs(12 * math.sin(x)))


def main():
    browser = selenium.webdriver.Firefox()

    try:
        browser.get("http://suninjuly.github.io/redirect_accept.html")
        browser.find_element(By.CSS_SELECTOR, ".trollface.btn.btn-primary").click()

        browser.switch_to.window(browser.window_handles[1])
        browser.refresh()

        x = int(browser.find_element(By.ID, "input_value").text)
        y = calc(x)
        browser.find_element(By.ID, "answer").send_keys(str(y))
        browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()

        alert = browser.switch_to.alert
        alert_text = str(alert.text)
        answer = alert_text.split(": ")[-1]
        alert.accept()
        print(answer)

        # browser.switch_to.window(browser.window_handles[1])
        # browser.get("https://stepik.org/lesson/184253/step/6")
        # browser.switch_to.window(browser.window_handles[2])
        # browser.find_element(By.ID, "textarea").send_keys(answer)
        # browser.find_element(By.CLASS_NAME, "submit-submission").click()

    finally:
        time.sleep(20)
        browser.quit()


if __name__ == "__main__":
    main()
