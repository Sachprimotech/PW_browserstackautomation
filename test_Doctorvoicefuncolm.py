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
import platform
import pytest
import asyncio


class Testone(BaseClass):
    @pytest.mark.run(order=12)
    @pytest.mark.dependency(depends=["test_doctorvoiceui"])
    def testcolmlinks(self):  # Time issue
        wait = WebDriverWait(self.driver, 20)
        name = self.driver.name
        result_broken = []
        log = self.getLogger()
        log.info(name)
        helper = SeleniumHelper(self.driver)
        opened_links = []
        self.driver.get("https://www.physiciansweekly.com/category/doctors-voice/")
        linkscolm = By.CSS_SELECTOR, ".view-all-btn-box .view-all-half a"
        colmlinks = wait.until(EC.presence_of_all_elements_located(linkscolm))
        for link in colmlinks:
            li = link.get_attribute("href")
            opened_links.append(li)

        # def verify_listlinks(
        #     selectors,
        #     additional_links,
        # ):
        #     all_links = []

        #     for selector in selectors:
        #         elements = self.driver.find_elements(By.CSS_SELECTOR, selector)
        #         links = [element.get_attribute("href") for element in elements]
        #         all_links.extend(links)

        #     if additional_links:
        #         all_links.extend(additional_links)

        # for link in all_links:
        #     self.driver.execute_script("window.open(arguments[0])", link)

        # handles = self.driver.window_handles
        # opened_links = []

        # for window in handles:
        #     self.driver.switch_to.window(window)
        #     opened_links.append(self.driver.current_url)

        # assert set(all_links) == set(opened_links) or (
        #     expected_link_count and len(all_links) == expected_link_count
        # )

        # for link in all_links:
        #     response = requests.get(link)
        #     status_code = response.status_code
        #     if status_code == 404:

        #         result_broken.append("fail")
        #         log.info(f"Link {link} is broken with status code {status_code}")

        #     elif status_code != 404:
        #         result_broken.append("pass")

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

                    log.info("Verifying links for multiple selectors")
                    selectors = [
                        ".doctor-voice-spcl-sec .et_pb_code_inner a"
                    ]  # Example CSS selectors
                    asyncio.run(SeleniumHelper.verify_links_async(self, selectors))
                    log.info("All links verified successfully")

                except Exception:
                    ()
            assert all(result == "pass" for result in result_broken)

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
                    log.info("Verifying links for multiple selectors")
                    selectors = [
                        ".doctor-voice-spcl-sec .et_pb_code_inner a"
                    ]  # Example CSS selectors
                    asyncio.run(SeleniumHelper.verify_links_async(self, selectors))
                    log.info("All links verified successfully")

                except Exception:
                    ()
            assert all(result == "pass" for result in result_broken)

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
                    log.info("Verifying links for multiple selectors")
                    selectors = [
                        ".doctor-voice-spcl-sec .et_pb_code_inner a"
                    ]  # Example CSS selectors
                    asyncio.run(SeleniumHelper.verify_links_async(self, selectors))
                    log.info("All links verified successfully")

                except Exception:
                    ()
            assert all(result == "pass" for result in result_broken)
