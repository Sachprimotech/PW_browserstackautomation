from utilities.base_class import BaseClass

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from object.seleniumhelper import SeleniumHelper
import requests
import time


class Testone(BaseClass):
    
    def test_cssslector(self):
        log = self.getLogger()
        self.driver.get("https://www.physiciansweekly.com/")
        self.driver.maximize_window()
        window_size = self.driver.get_window_size()

        try:
            popup = self.driver.find_element(
                By.CSS_SELECTOR, "#onesignal-popover-container"
            )

            popup.click()
        except Exception:
            ()

        elements = self.driver.find_elements(
            By.CSS_SELECTOR,
            "#newsSection .et_pb_with_border",
        )

        fetched_css_properties = []

        for element in elements:

            d = ["margin-right", "padding-right", "border"]
            for i in d:
                fetched_css_properties.append(element.value_of_css_property(i))

        log.info(set(fetched_css_properties))
        log.info(window_size)
