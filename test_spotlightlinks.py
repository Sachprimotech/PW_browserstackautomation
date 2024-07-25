from utilities.base_class import BaseClass

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from object.seleniumhelper import SeleniumHelper
import requests
import time
import platform


class Testone(BaseClass):
    def test_Meetingsbriefprogramelinks(self):
        wait = WebDriverWait(self.driver, 20)
        name = self.driver.name

        log = self.getLogger()
        log.info(name)
        helper = SeleniumHelper(self.driver)
        opened_links = [
            "https://www.physiciansweekly.com/deep-dives/spotlight/endometrial-cancer/",
            "https://www.physiciansweekly.com/deep-dives/spotlight/iron-deficiency-heart-failure/",
        ]
        main_window = self.driver.current_window_handle
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
            for url in opened_links:
                self.driver.get(url)
                try:
                    popup = self.driver.find_element(
                        By.CSS_SELECTOR,
                        "#onesignal-slidedown-dialog .primary.slidedown-button",
                    )
                    popup.click()
                except Exception:
                    ()
                log.info("start")
                try:
                    selectors = [
                        "div#cat-relevant.sub-cat-section .et_pb_row.cat-section.column-list-items a"
                    ]
                    additional_links = ["url"]
                    expected_link_count = 10

                    log.info("Verifying links for multiple selectors")
                    helper.verify_links(
                        selectors, additional_links, expected_link_count
                    )
                    log.info("All links verified successfully")
                except NoSuchElementException and TimeoutException:
                    self.driver.close()
                for handle in self.driver.window_handles:
                    if handle != main_window:
                        self.driver.switch_to.window(handle)
                        self.driver.close()

                # Switch back to the main window
                self.driver.switch_to.window(main_window)

            # work is pending for programme pages

        elif window_size["width"] > 767 and window_size["width"] < 981:

            log.info("start")

            for url in opened_links:
                self.driver.get(url)
                try:
                    popup = self.driver.find_element(
                        By.CSS_SELECTOR,
                        "#onesignal-slidedown-dialog .primary.slidedown-button",
                    )
                    popup.click()
                except Exception:
                    ()
                log.info("start")
                try:
                    selectors = [
                        "div#cat-relevant.sub-cat-section .et_pb_row.cat-section.column-list-items a"
                    ]
                    additional_links = ["url"]
                    expected_link_count = 21

                    log.info("Verifying links for multiple selectors")
                    helper.verify_links(
                        selectors, additional_links, expected_link_count
                    )
                    log.info("All links verified successfully")
                except Exception:
                    self.driver.close()
                for handle in self.driver.window_handles:
                    if handle != main_window:
                        self.driver.switch_to.window(handle)
                        self.driver.close()

                # Switch back to the main window
                self.driver.switch_to.window(main_window)

        elif window_size["width"] <= 767:

            for url in opened_links:
                self.driver.get(url)
                try:
                    popup = self.driver.find_element(
                        By.CSS_SELECTOR,
                        "#onesignal-slidedown-dialog .primary.slidedown-button",
                    )
                    popup.click()
                except Exception:
                    ()
                log.info("start")
                try:
                    selectors = [
                        "div#cat-relevant.sub-cat-section .et_pb_row.cat-section.column-list-items a"
                    ]
                    additional_links = ["url"]
                    expected_link_count = 21

                    log.info("Verifying links for multiple selectors")
                    helper.verify_links(
                        selectors, additional_links, expected_link_count
                    )
                    log.info("All links verified successfully")
                except NoSuchElementException and TimeoutException:
                    self.driver.close()
                for handle in self.driver.window_handles:
                    if handle != main_window:
                        self.driver.switch_to.window(handle)
                        self.driver.close()

                # Switch back to the main window
                self.driver.switch_to.window(main_window)
