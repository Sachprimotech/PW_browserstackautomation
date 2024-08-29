# busines-right.et_pb_code_inner.busines-doctor a
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
import asyncio


class Testone(BaseClass):
    @pytest.mark.run(order=27)
    @pytest.mark.dependency(depends=["test_Bomrsidebar"])
    def test_Bomdoctorvoice(self):
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
            self.driver.execute_script("window.scrollBy(0, 500)")
            try:
                popup = self.driver.find_element(
                    By.CSS_SELECTOR,
                    "#onesignal-slidedown-dialog .primary.slidedown-button",
                )
                popup.click()
            except Exception:
                ()

            log.info("start")

            selectors = ["#busines-right.et_pb_code_inner.busines-doctor a"]
            asyncio.run(SeleniumHelper.verify_links_async(self, selectors))
            log.info("All links verified successfully")

        elif window_size["width"] > 767 and window_size["width"] < 981:

            log.info("start")

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

            selectors = ["#busines-right.et_pb_code_inner.busines-doctor a"]
            asyncio.run(SeleniumHelper.verify_links_async(self, selectors))
            log.info("All links verified successfully")

        elif window_size["width"] <= 767:

            log.info("start")

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

            selectors = ["#busines-right.et_pb_code_inner.busines-doctor a"]
            asyncio.run(SeleniumHelper.verify_links_async(self, selectors))
            log.info("All links verified successfully")
