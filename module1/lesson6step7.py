from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def main():
    lorem_ipsum = "pellentesque elit ullamcorper dignissim cras tincidunt lobortis feugiat vivamus at augue eget arcu dictum varius duis at consectetur lorem donec massa sapien faucibus et molestie ac feugiat sed lectus vestibulum mattis ullamcorper velit sed ullamcorper morbi tincidunt ornare massa eget egestas purus viverra accumsan in nisl nisi scelerisque eu ultrices vitae auctor eu augue ut lectus arcu bibendum at varius vel pharetra vel turpis nunc eget lorem dolor sed viverra ipsum nunc aliquet bibendum enim facilisis gravida neque convallis a cras semper auctor neque vitae tempus quam pellentesque nec nam aliquam sem et tortor consequat id porta nibh venenatis cras"

    try:
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/huge_form.html")
        elements = browser.find_elements(By.XPATH, "//input")
        for element, word in zip(elements, lorem_ipsum.split(" ")):
            element.send_keys(word)

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

    finally:
        time.sleep(30)
        browser.quit()


if __name__ == "__main__":
    main()