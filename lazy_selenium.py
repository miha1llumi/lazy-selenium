from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class LazyWebDriver:
    __isinstance = False

    def __new__(cls, *args, **kwargs):
        cls.__isinstance = super().__new__(cls) if not cls.__isinstance else cls.__isinstance
        return cls.__isinstance

    def __init__(self, driver):
        self.driver = driver

    def press_enter(self):
        ActionChains(self.driver) \
            .send_keys(Keys.ENTER) \
            .perform()

    def click_and_hold(self, element):
        ActionChains(self.driver) \
            .click_and_hold(element) \
            .perform()

    def click_and_release(self, element):
        ActionChains(self.driver) \
            .click(element) \
            .perform()

    def context_click(self, element):
        ActionChains(self.driver) \
            .context_click(element) \
            .perform()

    def click_and_clear_text(self, element):
        element.click()
        ActionChains(self.driver) \
            .send_keys(Keys.CONTROL + "A" + Keys.BACKSPACE) \
            .perform()
