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


class Testone(BaseClass):
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

        def verify_listlinks(selectors, additional_links, expected_link_count):
            all_links = []

            for selector in selectors:
                elements = self.driver.find_elements(By.CSS_SELECTOR, selector)
                links = [element.get_attribute("href") for element in elements]
                all_links.extend(links)

            if additional_links:
                all_links.extend(additional_links)

            for link in all_links:
                self.driver.execute_script("window.open(arguments[0])", link)

            handles = self.driver.window_handles
            opened_links = []

            for window in handles:
                self.driver.switch_to.window(window)
                opened_links.append(self.driver.current_url)

            assert set(all_links) == set(opened_links) or (
                expected_link_count and len(all_links) == expected_link_count
            )

            for link in opened_links:
                response = requests.get(link)
                status_code = response.status_code
                if status_code == 404:

                    result_broken.append("fail")
                    log.info(f"Link {link} is broken with status code {status_code}")

                elif status_code != 404:
                    result_broken.append("pass")

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
                    expected_link_count = 21

                    log.info("Verifying links for multiple selectors")
                    verify_listlinks(selectors, additional_links, expected_link_count)
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
                    additional_links = ["url"]
                    expected_link_count = 21

                    log.info("Verifying links for multiple selectors")
                    verify_listlinks(selectors, additional_links, expected_link_count)
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
                    verify_listlinks(selectors, additional_links, expected_link_count)
                    log.info("All links verified successfully")

                except Exception:
                    self.driver.close()
                for handle in self.driver.window_handles:
                    if handle != main_window:
                        self.driver.switch_to.window(handle)
                        self.driver.close()

                # Switch back to the main window
                self.driver.switch_to.window(main_window)
