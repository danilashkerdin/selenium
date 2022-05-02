from selenium import webdriver
from selenium.webdriver.common.by import By
import math


def calc(x):
    return math.log(abs(12 * math.sin(x)))


browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
x = int(browser.find_element(By.ID, "input_value").text)
y = str(calc(x))
browser.find_element(By.ID, "answer").send_keys(y)
button = browser.find_element(By.TAG_NAME, "button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)

browser.find_element(By.ID, "robotCheckbox").click()
browser.find_element(By.ID, "robotsRule").click()

button.click()
