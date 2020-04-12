import time
from selenium.webdriver.common.by import By

url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_guest_should_see_basket_link(browser):
    browser.get(url)
#    time.sleep(10)
    buttons = browser.find_elements(By.CSS_SELECTOR,
            '#add_to_basket_form > button.btn-add-to-basket')

    assert len(buttons) > 0, 'There is no "Add to basket" button on the page'
