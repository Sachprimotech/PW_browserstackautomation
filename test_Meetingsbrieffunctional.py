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


class Testone(BaseClass):
    @pytest.mark.run(order=32)
    @pytest.mark.dependency(depends=["test_Meetingsbriefprograme"])
    def test_Meetingsbrieffunct(self):
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
                    "#doctor-voice-sec .et_pb_button_module_wrapper .et_pb_button",
                )
                readmorebutton = wait.until(
                    EC.presence_of_all_elements_located(readmore)
                )
                for button in readmorebutton:
                    Ac.key_down(key_to_hold).click(button).key_up(key_to_hold).perform()

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
                    "#doctor-voice-sec .et_pb_button_module_wrapper .et_pb_button",
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
                    "#doctor-voice-sec .et_pb_button_module_wrapper .et_pb_button",
                )
                readmorebutton = wait.until(
                    EC.presence_of_all_elements_located(readmore)
                )
                for button in readmorebutton:
                    Ac.key_down(key_to_hold).click(button).key_up(key_to_hold).perform()

            log.info("click")
