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
import pytest


class Testone(BaseClass):
    @pytest.mark.run(order=24)
    @pytest.mark.dependency(depends=["test_Business_of_Medicine"])
    def test_Bompodcastcoloumn(self):
        wait = WebDriverWait(self.driver, 20)
        name = self.driver.name

        log = self.getLogger()
        log.info(name)
        helper = SeleniumHelper(self.driver)

        window_size = self.driver.get_window_size()
        if window_size["width"] > 980:

            try:
                popup = self.driver.find_element(
                    By.CSS_SELECTOR,
                    "#onesignal-slidedown-dialog .primary.slidedown-button",
                )
                popup.click()
            except Exception:
                ()
            self.driver.get(
                "https://www.physiciansweekly.com/category/business-of-medicine/"
            )
            try:
                popup = self.driver.find_element(
                    By.CSS_SELECTOR,
                    "#onesignal-slidedown-dialog .primary.slidedown-button",
                )
                popup.click()
            except Exception:
                ()
            self.driver.execute_script("window.scrollBy(0, 500)")

            log.info("start")

            selectors = ["#filter-podcast-cstm a"]
            additional_links = [
                "https://www.physiciansweekly.com/category/business-of-medicine/"
            ]
            expected_link_count = 14

            log.info("Verifying links for multiple selectors")
            helper.verify_links(selectors, additional_links, expected_link_count)
            log.info("All links verified successfully")

        elif window_size["width"] > 767 and window_size["width"] < 981:

            log.info("start")

            self.driver.get(
                "https://www.physiciansweekly.com/category/business-of-medicine/"
            )
            self.driver.execute_script("window.scrollBy(0, 500)")
            log.info("start")

            selectors = ["#recent-colnm-one a"]
            additional_links = [
                "https://www.physiciansweekly.com/category/business-of-medicine/"
            ]
            expected_link_count = 40

            log.info("Verifying links for multiple selectors")
            helper.verify_links(selectors, additional_links, expected_link_count)
            log.info("All links verified successfully")

        elif window_size["width"] <= 767:

            log.info("start")

            self.driver.get(
                "https://www.physiciansweekly.com/category/business-of-medicine/"
            )
            self.driver.execute_script("window.scrollBy(0, 500)")
            log.info("start")

            selectors = ["#recent-colnm-one a"]
            additional_links = [
                "https://www.physiciansweekly.com/category/business-of-medicine/"
            ]
            expected_link_count = 40

            log.info("Verifying links for multiple selectors")
            helper.verify_links(selectors, additional_links, expected_link_count)
            log.info("All links verified successfully")
