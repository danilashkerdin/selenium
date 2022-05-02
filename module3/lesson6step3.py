import math
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

params = ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"]


def calc():
    return math.log(int(time.time()))


class TestCase:

    @pytest.mark.parametrize('param', params)
    def test_(self, browser, param):
        browser.get(f"https://stepik.org/lesson/{param}/step/1")

        waiter = WebDriverWait(browser, 10)

        answer_input = waiter.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, ".ember-text-area.ember-view.textarea.string-quiz__textarea")))
        answer_input.send_keys(calc())
        browser.find_element(By.CLASS_NAME, "submit-submission").click()
        text = waiter.until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, "smart-hints__hint"))).text
        assert "Correct!" == text, text
