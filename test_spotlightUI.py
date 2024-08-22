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
    @pytest.mark.run(order=43)
    @pytest.mark.dependency(depends=["test_Spotlightprogramelinks"])
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
            self.driver.get("https://www.physiciansweekly.com/deep-dives/spotlight/")
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

            readmore = (
                By.CSS_SELECTOR,
                ".spotlights-post-content p.read-more-link a",
            )
            readmorebutton = wait.until(EC.presence_of_all_elements_located(readmore))
            for button in readmorebutton:
                Ac.key_down(key_to_hold).click(button).key_up(key_to_hold).perform()

            handles = self.driver.window_handles
            log.info("start")

            for window in handles:
                self.driver.switch_to.window(window)
                try:
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
                        ),
                        (
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
                        (
                            "span.published",
                            {
                                "28px",
                                "uppercase",
                                "rgba(1, 121, 217, 1)",
                                "none",
                                "0px",
                                "elza",
                                "elza, sans-serif",
                                "500",
                                "14px",
                                "0.35px",
                                "700",
                                "normal",
                            },
                            [
                                "text-transform",
                                "letter-spacing",
                                "line-height",
                                "font-style",
                                "font-family",
                                "font-weight",
                                "font-size",
                                "color",
                                "margin",
                            ],
                        ),
                        (
                            "div#cat-relevant div#sub-cat-scnd-post p",
                            {
                                "385.875px",
                                "18px",
                                "0px 0px 4px",
                                "21px",
                                "rgba(21, 44, 108, 1)",
                                "normal",
                                "400",
                                "block",
                                "0px",
                                "elza",
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
                        (
                            "div#cat-relevant .et_pb_column.et_pb_column_2_3",
                            {"68.1875px", "803.922px"},
                            ["width", "margin-right"],
                        ),
                        (
                            "#sub-cat-scnd-post article",
                            {
                                "1px solid rgb(191, 191, 191)",
                                "45px",
                                "507px",
                                "486px",
                                "14px",
                                "12px",
                            },
                            [
                                "height",
                                "padding-bottom",
                                "margin-bottom",
                                "border-bottom",
                                "margin-right",
                            ],
                        ),
                        (
                            "#peer-to-peer-banner span.page-cat",
                            {
                                "10px",
                                "elza",
                                "700",
                                "flex",
                                "normal",
                                "flex-end",
                                "rgba(255, 255, 255, 1)",
                                "25px",
                            },
                            [
                                "margin-bottom",
                                "line-height",
                                "color",
                                "font-size",
                                "font-weight",
                                "font-family",
                                "align-items",
                                "display",
                            ],
                        ),
                        (
                            "#et-boc h1.is_archive",
                            {
                                "block",
                                "elza",
                                "700",
                                "60px",
                                "103px",
                                "rgba(255, 255, 255, 1)",
                            },
                            [
                                "line-height",
                                "color",
                                "font-size",
                                "font-weight",
                                "font-family",
                                "display",
                            ],
                        ),
                    ]
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
                except Exception:
                    log.info(" error")
                log.info("end")

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
            if platform.system() == "Darwin":  # macOS
                key_to_hold = Keys.COMMAND
            else:  # Windows or other
                key_to_hold = Keys.CONTROL

            readmore = (
                By.CSS_SELECTOR,
                ".spotlights-post-content p.read-more-link a",
            )
            readmorebutton = wait.until(EC.presence_of_all_elements_located(readmore))
            for button in readmorebutton:
                Ac.key_down(key_to_hold).click(button).key_up(key_to_hold).perform()

            handles = self.driver.window_handles
            log.info("start")

            for window in handles:
                self.driver.switch_to.window(window)
                try:
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
                        ),
                        (
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
                        (
                            "span.published",
                            {
                                "28px",
                                "uppercase",
                                "rgba(1, 121, 217, 1)",
                                "none",
                                "0px",
                                "elza",
                                "elza, sans-serif",
                                "500",
                                "14px",
                                "0.35px",
                                "700",
                                "normal",
                            },
                            [
                                "text-transform",
                                "letter-spacing",
                                "line-height",
                                "font-style",
                                "font-family",
                                "font-weight",
                                "font-size",
                                "color",
                                "margin",
                            ],
                        ),
                        (
                            "div#cat-relevant div#sub-cat-scnd-post p",
                            {
                                "385.875px",
                                "18px",
                                "0px 0px 4px",
                                "21px",
                                "rgba(21, 44, 108, 1)",
                                "normal",
                                "400",
                                "block",
                                "0px",
                                "elza",
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
                        (
                            "div#cat-relevant .et_pb_column.et_pb_column_2_3",
                            {"68.1875px", "803.922px"},
                            ["width", "margin-right"],
                        ),
                        (
                            "#sub-cat-scnd-post article",
                            {
                                "1px solid rgb(191, 191, 191)",
                                "45px",
                                "507px",
                                "486px",
                                "14px",
                                "12px",
                            },
                            [
                                "height",
                                "padding-bottom",
                                "margin-bottom",
                                "border-bottom",
                                "margin-right",
                            ],
                        ),
                        (
                            "#peer-to-peer-banner span.page-cat",
                            {
                                "10px",
                                "elza",
                                "700",
                                "flex",
                                "normal",
                                "flex-end",
                                "rgba(255, 255, 255, 1)",
                                "25px",
                            },
                            [
                                "margin-bottom",
                                "line-height",
                                "color",
                                "font-size",
                                "font-weight",
                                "font-family",
                                "align-items",
                                "display",
                            ],
                        ),
                        (
                            "#et-boc h1.is_archive",
                            {
                                "block",
                                "elza",
                                "700",
                                "60px",
                                "103px",
                                "rgba(255, 255, 255, 1)",
                            },
                            [
                                "line-height",
                                "color",
                                "font-size",
                                "font-weight",
                                "font-family",
                                "display",
                            ],
                        ),
                    ]
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
                except Exception:
                    log.info(" error")
                log.info("end")

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
            log.info("start")

            Ac = ActionChains(self.driver)
            if platform.system() == "Darwin":  # macOS
                key_to_hold = Keys.COMMAND
            else:  # Windows or other
                key_to_hold = Keys.CONTROL

            readmore = (
                By.CSS_SELECTOR,
                ".spotlights-post-content p.read-more-link a",
            )
            readmorebutton = wait.until(EC.presence_of_all_elements_located(readmore))
            for button in readmorebutton:
                Ac.key_down(key_to_hold).click(button).key_up(key_to_hold).perform()

            handles = self.driver.window_handles
            log.info("start")

            for window in handles:
                self.driver.switch_to.window(window)
                try:
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
                        ),
                        (
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
                        (
                            "span.published",
                            {
                                "28px",
                                "uppercase",
                                "rgba(1, 121, 217, 1)",
                                "none",
                                "0px",
                                "elza",
                                "elza, sans-serif",
                                "500",
                                "14px",
                                "0.35px",
                                "700",
                                "normal",
                            },
                            [
                                "text-transform",
                                "letter-spacing",
                                "line-height",
                                "font-style",
                                "font-family",
                                "font-weight",
                                "font-size",
                                "color",
                                "margin",
                            ],
                        ),
                        (
                            "div#cat-relevant div#sub-cat-scnd-post p",
                            {
                                "385.875px",
                                "18px",
                                "0px 0px 4px",
                                "21px",
                                "rgba(21, 44, 108, 1)",
                                "normal",
                                "400",
                                "block",
                                "0px",
                                "elza",
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
                        (
                            "div#cat-relevant .et_pb_column.et_pb_column_2_3",
                            {"68.1875px", "803.922px"},
                            ["width", "margin-right"],
                        ),
                        (
                            "#sub-cat-scnd-post article",
                            {
                                "1px solid rgb(191, 191, 191)",
                                "45px",
                                "507px",
                                "486px",
                                "14px",
                                "12px",
                            },
                            [
                                "height",
                                "padding-bottom",
                                "margin-bottom",
                                "border-bottom",
                                "margin-right",
                            ],
                        ),
                        (
                            "#peer-to-peer-banner span.page-cat",
                            {
                                "10px",
                                "elza",
                                "700",
                                "flex",
                                "normal",
                                "flex-end",
                                "rgba(255, 255, 255, 1)",
                                "25px",
                            },
                            [
                                "margin-bottom",
                                "line-height",
                                "color",
                                "font-size",
                                "font-weight",
                                "font-family",
                                "align-items",
                                "display",
                            ],
                        ),
                        (
                            "#et-boc h1.is_archive",
                            {
                                "block",
                                "elza",
                                "700",
                                "60px",
                                "103px",
                                "rgba(255, 255, 255, 1)",
                            },
                            [
                                "line-height",
                                "color",
                                "font-size",
                                "font-weight",
                                "font-family",
                                "display",
                            ],
                        ),
                    ]
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
                except Exception:
                    log.info(" error")
                log.info("end")
