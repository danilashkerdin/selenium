from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestCaseItems:

    def test_cart_button_exists(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        browser.get(link)
        cart_button = WebDriverWait(browser, 10).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, '.btn.btn-lg.btn-primary.btn-add-to-basket')))
        assert cart_button, "No cart button!"
