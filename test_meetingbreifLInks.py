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
    @pytest.mark.run(order=29)
    @pytest.mark.dependency(depends=["test_Bomrecentcoloumn"])
    def test_Meetingsbriefprogramelinks(self):
        wait = WebDriverWait(self.driver, 20)
        name = self.driver.name
        result_broken = []
        log = self.getLogger()
        log.info(name)
        helper = SeleniumHelper(self.driver)
        opened_links = [
            "https://www.physiciansweekly.com/meeting-coverage/asco-2024-multiple-myeloma/",
            "https://www.physiciansweekly.com/meeting-coverage/asco-2024-hepatocellular-carcinoma/",
            "https://www.physiciansweekly.com/meeting-coverage/asco-2024-ensclc/",
            "https://www.physiciansweekly.com/meeting-coverage/asco-2024-chronic-lymphocytic-leukemia/",
            "https://www.physiciansweekly.com/meeting-coverage/2024-aad-annual-meeting/",
            "https://www.physiciansweekly.com/meeting-coverage/actrims-forum-2024/",
            "https://www.physiciansweekly.com/meeting-coverage/crohns-colitis-congress-2024-crohns-disease-colitis/",
            "https://www.physiciansweekly.com/meeting-coverage/maui-derm-hawaii-2024-psoriasis/",
            "https://www.physiciansweekly.com/meeting-coverage/2024-winter-clinical-dermatology-conference-psoriasis/",
            "https://www.physiciansweekly.com/meeting-coverage/65th-ash-annual-meeting-leukemia-lymphoma/",
            "https://www.physiciansweekly.com/meeting-coverage/naclc-2023-nsclc/",
            "https://www.physiciansweekly.com/meeting-coverage/aan-2023-fall-conference-ms/",
            "https://www.physiciansweekly.com/meeting-coverage/aao-2023-retinal-vascular-disease/",
            "https://www.physiciansweekly.com/meeting-coverage/esmo-2023-ensclc/",
            "https://www.physiciansweekly.com/meeting-coverage/fall-clinical-dermatology-conference-psoriasis/",
            "https://www.physiciansweekly.com/meeting-coverage/conference-10/",
            "https://www.physiciansweekly.com/meeting-coverage/asrs-23-conference-oct/",
            "https://physiciansweekly.com/meeting-coverage/conference-14/",
            "https://www.physiciansweekly.com/meeting-coverage/conference-13/",
            "https://www.physiciansweekly.com/meeting-coverage/conference-may/",
            "https://www.physiciansweekly.com/meeting-coverage/conference-15/",
            "https://www.physiciansweekly.com/meeting-coverage/conference-11/",
            "https://www.physiciansweekly.com/clinical-report-addresses-management-of-sickle-cell-disease-in-children-teens/",
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
                    asyncio.run(SeleniumHelper.verify_links_async(self, selectors))
                    log.info("All links verified successfully")

                except Exception:
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
                    asyncio.run(SeleniumHelper.verify_links_async(self, selectors))
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
                    asyncio.run(SeleniumHelper.verify_links_async(self, selectors))
                    log.info("All links verified successfully")

                except Exception:
                    self.driver.close()
                for handle in self.driver.window_handles:
                    if handle != main_window:
                        self.driver.switch_to.window(handle)
                        self.driver.close()

                # Switch back to the main window
                self.driver.switch_to.window(main_window)
