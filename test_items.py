from selenium.webdriver.common.by import By


class TestCaseItems:

    def test_add_to_cart_button_exists(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        browser.get(link)
        assert browser.find_element(By.CSS_SELECTOR, '.btn.btn-lg.btn-primary.btn-add-to-basket'), "No cart button!"
