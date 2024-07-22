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
    def test_Meetingsbriefprograme(self):
        wait = WebDriverWait(self.driver, 20)
        name = self.driver.name

        log = self.getLogger()
        log.info(name)
        helper = SeleniumHelper(self.driver)
        opened_links = []

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
            self.driver.get("https://www.physiciansweekly.com/meeting-coverage/")
            try:
                popup = self.driver.find_element(
                    By.CSS_SELECTOR,
                    "#onesignal-slidedown-dialog .primary.slidedown-button",
                )
                popup.click()
            except Exception:
                ()
            log.info("start")

            Ac = ActionChains(self.driver)
            if platform.system() == "Darwin":  # macOS
                key_to_hold = Keys.COMMAND
            else:  # Windows or other
                key_to_hold = Keys.CONTROL

            while True:
                try:
                    next = By.XPATH, "//a[@class='next page-numbers']"
                    nextbutton = wait.until(EC.presence_of_element_located(next))
                except Exception:
                    break
                if nextbutton:

                    readmore = (
                        By.CSS_SELECTOR,
                        "#doctor-voice-sec .et_pb_button_module_wrapper .et_pb_button",
                    )
                    readmorebutton = wait.until(
                        EC.presence_of_all_elements_located(readmore)
                    )
                    for button in readmorebutton:
                        Ac.key_down(key_to_hold).click(button).key_up(
                            key_to_hold
                        ).perform()
                    Ac.move_to_element(nextbutton).click().perform()
                else:
                    break
                readmore = (
                    By.CSS_SELECTOR,
                    "#doctor-voice-sec .et_pb_button_module_wrapper .et_pb_button",
                )
                readmorebutton = wait.until(
                    EC.presence_of_all_elements_located(readmore)
                )
                for button in readmorebutton:
                    Ac.key_down(key_to_hold).click(button).key_up(key_to_hold).perform()
            handles = self.driver.window_handles

            for window in handles:
                self.driver.switch_to.window(window)
                selectors_and_properties = [
                    (
                        "#et-boc .breadcrumb #crumbs",
                        {
                            "elza, sans-serif",
                            "rgba(55, 55, 55, 1)",
                            "20px",
                            "normal",
                            "24px",
                            "uppercase",
                            "700",
                        },
                        [
                            "text-transform",
                            "line-height",
                            "font-size",
                            "color",
                            "font-weight",
                            "font-style",
                            "font-family",
                        ],
                    )(
                        "#crumbs .current",
                        {".02em", "500"},
                        ["letter-spacing", "font-weight"],
                    ),
                    (".breadcrumb", {"10px 0"}, ["margin"]),
                    (
                        "h2",
                        {
                            "803.922px",
                            "22px",
                            "30px",
                            "620.094px",
                            "28.6px",
                            "elza, sans-serif",
                            "385.875px",
                            "normal",
                            "0px",
                            '"Open Sans"',
                            "Elza",
                            "36px",
                            "0px 0px 10px",
                            "rgba(0, 0, 0, 0.75)",
                            "600",
                            "rgba(21, 44, 108, 1)",
                            "block",
                            "auto",
                            "700",
                            "24px",
                        },
                        [
                            "padding",
                            "width",
                            "display",
                            "line-height",
                            "font-style",
                            "font-family",
                            "font-weight",
                            "font-size",
                            "color",
                        ],
                    ),
                ]

            log.info("click")

        elif window_size["width"] > 767 and window_size["width"] < 981:

            log.info("start")

            self.driver.get("https://www.physiciansweekly.com/meeting-coverage/")
            try:
                popup = self.driver.find_element(
                    By.CSS_SELECTOR,
                    "#onesignal-slidedown-dialog .primary.slidedown-button",
                )
                popup.click()
            except Exception:
                ()
            log.info("start")

            self.driver.get("https://www.physiciansweekly.com/meeting-coverage/")
            try:
                popup = self.driver.find_element(
                    By.CSS_SELECTOR,
                    "#onesignal-slidedown-dialog .primary.slidedown-button",
                )
                popup.click()
            except Exception:
                ()
            log.info("start")

            Ac = ActionChains(self.driver)

            tagslinks = (
                By.CSS_SELECTOR,
                "#wekly-news-container ul.meeting-coverage-list a",
            )
            tagsclicks = wait.until(EC.presence_of_all_elements_located(tagslinks))
            for tagclick in tagsclicks:
                Ac.move_to_element(tagclick).click().perform()

            while True:
                try:
                    next = By.XPATH, "//a[@class='next page-numbers']"
                    nextbutton = wait.until(EC.presence_of_element_located(next))
                except Exception:
                    break
                if nextbutton:

                    readmore = (
                        By.CSS_SELECTOR,
                        "#doctor-voice-sec .et_pb_button_module_wrapper .et_pb_button",
                    )
                    readmorebutton = wait.until(
                        EC.presence_of_all_elements_located(readmore)
                    )
                    for button in readmorebutton:
                        Ac.key_down(key_to_hold).click(button).key_up(
                            key_to_hold
                        ).perform()
                    Ac.move_to_element(nextbutton).click().perform()
                else:
                    break
                readmore = (
                    By.CSS_SELECTOR,
                    ".et_pb_button.et_pb_button_27.cat-view-all-button.et_pb_bg_layout_light",
                )
                readmorebutton = wait.until(
                    EC.presence_of_all_elements_located(readmore)
                )
                for button in readmorebutton:
                    Ac.key_down(key_to_hold).click(button).key_up(key_to_hold).perform()

            log.info("click")

        elif window_size["width"] <= 767:

            self.driver.get("https://www.physiciansweekly.com/meeting-coverage/")
            try:
                popup = self.driver.find_element(
                    By.CSS_SELECTOR,
                    "#onesignal-slidedown-dialog .primary.slidedown-button",
                )
                popup.click()
            except Exception:
                ()
            self.driver.get("https://www.physiciansweekly.com/meeting-coverage/")
            try:
                popup = self.driver.find_element(
                    By.CSS_SELECTOR,
                    "#onesignal-slidedown-dialog .primary.slidedown-button",
                )
                popup.click()
            except Exception:
                ()
            log.info("start")

            Ac = ActionChains(self.driver)
            if platform.system() == "Darwin":  # macOS
                key_to_hold = Keys.COMMAND
            else:  # Windows or other
                key_to_hold = Keys.CONTROL

            tagslinks = (
                By.CSS_SELECTOR,
                "#wekly-news-container ul.meeting-coverage-list a",
            )
            tagsclicks = wait.until(EC.presence_of_all_elements_located(tagslinks))
            for tagclick in tagsclicks:
                Ac.move_to_element(tagclick).click().perform()

            while True:
                try:
                    next = By.XPATH, "//a[@class='next page-numbers']"
                    nextbutton = wait.until(EC.presence_of_element_located(next))
                except Exception:
                    break
                if nextbutton:

                    readmore = (
                        By.CSS_SELECTOR,
                        "#doctor-voice-sec .et_pb_button_module_wrapper .et_pb_button",
                    )
                    readmorebutton = wait.until(
                        EC.presence_of_all_elements_located(readmore)
                    )
                    for button in readmorebutton:
                        Ac.key_down(key_to_hold).click(button).key_up(
                            key_to_hold
                        ).perform()
                    Ac.move_to_element(nextbutton).click().perform()
                else:
                    break
                readmore = (
                    By.CSS_SELECTOR,
                    ".et_pb_button.et_pb_button_27.cat-view-all-button.et_pb_bg_layout_light",
                )
                readmorebutton = wait.until(
                    EC.presence_of_all_elements_located(readmore)
                )
                for button in readmorebutton:
                    Ac.key_down(key_to_hold).click(button).key_up(key_to_hold).perform()

            log.info("click")
