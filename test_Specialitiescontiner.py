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
import pytest


# this file is pending for changes as speciality UI
class Testone(BaseClass):
    @pytest.mark.run(order=39)
    @pytest.mark.dependency(depends=["test_Specialities"])
    def test_specialitysection(self):
        wait = WebDriverWait(self.driver, 20)
        name = self.driver.name

        log = self.getLogger()
        log.info(name)
        helper = SeleniumHelper(self.driver)
        AC = ActionChains(self.driver)
        All_specialities_urls = []
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
            self.driver.get("https://www.physiciansweekly.com/specialties/")
            All_specialities = (
                By.CSS_SELECTOR,
                "#specialties-columns nav.et-menu-nav .et-menu a",
            )

            specialities = wait.until(
                EC.presence_of_all_elements_located(All_specialities)
            )
            for specialty in specialities:
                href = specialty.get_attribute("href")
                All_specialities_urls.append(href)
            for urls in All_specialities_urls:
                self.driver.execute_script("window.open(arguments[0])", urls)
            wait.until(
                lambda d: d.execute_script("return document.readyState") == "complete"
            )
            time.sleep(20)

            handles = self.driver.window_handles

            for window in handles:

                self.driver.switch_to.window(window)

                log.info("start")
                try:

                    selectors_and_properties = [
                        (
                            "#cat-relevant.et_pb_section .wekly-news-container",
                            {"20px"},
                            ["padding"],
                        ),
                        (
                            ".category .wekly-news-container .el-dbe-blog-extra.block_extended article",
                            {"20px", "1px solid #bfbfbf"},
                            ["padding-bottom", "border-bottom"],
                        ),
                        (
                            "button.et_pb_button",
                            {
                                "600",
                                "rgba(25, 35, 62, 1)",
                                "23.8px",
                                "none solid rgb(25, 35, 62)",
                                "6px 20px",
                                "700",
                                "0px 5px 0px 0px",
                                "14px",
                                "Elza",
                                "none solid rgb(21, 44, 108)",
                                "6px 20px 6px 0px",
                                "18px",
                                "30.6px",
                                "elza",
                                "rgba(21, 44, 108, 1)",
                            },
                            [
                                "color",
                                "font-size",
                                "font-weight",
                                "padding",
                                "font-family",
                                "line-height",
                                "text-decoration",
                            ],
                        ),
                    ]

                    log.info("medium")
                    for (
                        css_selector,
                        expected_css_properties,
                        css_properties_list,
                    ) in selectors_and_properties:
                        result = helper.fetch_and_check_css_properties(
                            css_selector, expected_css_properties, css_properties_list
                        )
                    assert (
                        result
                    ), f"CSS properties do not match the expected values for selector {css_selector}"
                    log.info("end")
                except Exception:
                    ()
        elif window_size["width"] > 767 and window_size["width"] < 981:

            log.info("start")

            self.driver.get("https://www.physiciansweekly.com/specialties/")
            All_specialities = (
                By.CSS_SELECTOR,
                "#specialties-columns nav.et-menu-nav .et-menu a",
            )

            specialities = wait.until(
                EC.presence_of_all_elements_located(All_specialities)
            )
            for specialty in specialities:
                href = specialty.get_attribute("href")
                All_specialities_urls.append(href)
            for urls in All_specialities_urls:
                self.driver.execute_script("window.open(arguments[0])", urls)
            wait.until(
                lambda d: d.execute_script("return document.readyState") == "complete"
            )
            time.sleep(20)

            handles = self.driver.window_handles

            for window in handles:

                self.driver.switch_to.window(window)

                log.info("start")
                try:

                    selectors_and_properties = [
                        (
                            "#cat-relevant.et_pb_section .wekly-news-container",
                            {"20px"},
                            ["padding"],
                        ),
                        (
                            ".category .wekly-news-container .el-dbe-blog-extra.block_extended article",
                            {"20px", "1px solid #bfbfbf"},
                            ["padding-bottom", "border-bottom"],
                        ),
                        (
                            "button.et_pb_button",
                            {
                                "600",
                                "rgba(25, 35, 62, 1)",
                                "23.8px",
                                "none solid rgb(25, 35, 62)",
                                "6px 20px",
                                "700",
                                "0px 5px 0px 0px",
                                "14px",
                                "Elza",
                                "none solid rgb(21, 44, 108)",
                                "6px 20px 6px 0px",
                                "18px",
                                "30.6px",
                                "elza",
                                "rgba(21, 44, 108, 1)",
                            },
                            [
                                "color",
                                "font-size",
                                "font-weight",
                                "padding",
                                "font-family",
                                "line-height",
                                "text-decoration",
                            ],
                        ),
                    ]

                    log.info("medium")
                    for (
                        css_selector,
                        expected_css_properties,
                        css_properties_list,
                    ) in selectors_and_properties:
                        result = helper.fetch_and_check_css_properties(
                            css_selector, expected_css_properties, css_properties_list
                        )
                    assert (
                        result
                    ), f"CSS properties do not match the expected values for selector {css_selector}"
                    log.info("end")
                except Exception:
                    ()

        elif window_size["width"] <= 767:

            log.info("start")

            self.driver.get("https://www.physiciansweekly.com/specialties/")
            All_specialities = (
                By.CSS_SELECTOR,
                "#specialties-columns nav.et-menu-nav .et-menu a",
            )

            specialities = wait.until(
                EC.presence_of_all_elements_located(All_specialities)
            )
            for specialty in specialities:
                href = specialty.get_attribute("href")
                All_specialities_urls.append(href)
            for urls in All_specialities_urls:
                self.driver.execute_script("window.open(arguments[0])", urls)
            wait.until(
                lambda d: d.execute_script("return document.readyState") == "complete"
            )
            time.sleep(20)

            handles = self.driver.window_handles

            for window in handles:

                self.driver.switch_to.window(window)

                log.info("start")
                try:

                    selectors_and_properties = [
                        (
                            "#cat-relevant.et_pb_section .wekly-news-container",
                            {"20px"},
                            ["padding"],
                        ),
                        (
                            ".category .wekly-news-container .el-dbe-blog-extra.block_extended article",
                            {"20px", "1px solid #bfbfbf"},
                            ["padding-bottom", "border-bottom"],
                        ),
                        (
                            "button.et_pb_button",
                            {
                                "600",
                                "rgba(25, 35, 62, 1)",
                                "23.8px",
                                "none solid rgb(25, 35, 62)",
                                "6px 20px",
                                "700",
                                "0px 5px 0px 0px",
                                "14px",
                                "Elza",
                                "none solid rgb(21, 44, 108)",
                                "6px 20px 6px 0px",
                                "18px",
                                "30.6px",
                                "elza",
                                "rgba(21, 44, 108, 1)",
                            },
                            [
                                "color",
                                "font-size",
                                "font-weight",
                                "padding",
                                "font-family",
                                "line-height",
                                "text-decoration",
                            ],
                        ),
                    ]

                    log.info("medium")
                    for (
                        css_selector,
                        expected_css_properties,
                        css_properties_list,
                    ) in selectors_and_properties:
                        result = helper.fetch_and_check_css_properties(
                            css_selector, expected_css_properties, css_properties_list
                        )
                    assert (
                        result
                    ), f"CSS properties do not match the expected values for selector {css_selector}"
                    log.info("end")
                except Exception:
                    ()
