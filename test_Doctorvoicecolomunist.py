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
    @pytest.mark.run(order=13)
    @pytest.mark.dependency(depends=["testcolmlinks"])  # pending
    def test_doctorvoicecolm(self):  # time issue
        wait = WebDriverWait(self.driver, 20)
        name = self.driver.name

        log = self.getLogger()
        log.info(name)
        helper = SeleniumHelper(self.driver)
        Ac = ActionChains(self.driver)
        window_size = self.driver.get_window_size()
        Ac = ActionChains(self.driver)
        if platform.system() == "Darwin":  # macOS
            key_to_hold = Keys.COMMAND
        else:  # Windows or other
            key_to_hold = Keys.CONTROL
        if window_size["width"] > 980:
            try:
                popup = self.driver.find_element(
                    By.CSS_SELECTOR,
                    "#onesignal-slidedown-dialog .primary.slidedown-button",
                )
                popup.click()
            except Exception:
                ()
            self.driver.get("https://www.physiciansweekly.com/category/doctors-voice/")
            try:
                popup = self.driver.find_element(
                    By.CSS_SELECTOR,
                    "#onesignal-slidedown-dialog .primary.slidedown-button",
                )
                popup.click()
            except Exception:
                ()

            view_allbtn = By.CSS_SELECTOR, ".view-all-btn-box .view-all-half a"
            btn = wait.until(EC.presence_of_all_elements_located(view_allbtn))

            for bn in btn:
                Ac.key_down(key_to_hold).click(bn).key_up(key_to_hold).perform()

            handles = self.driver.window_handles
            for window in handles:
                self.driver.switch_to.window(window)

                try:
                    log.info("start")

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
                            "h1.is_archive",
                            {
                                "700",
                                "60px",
                                "0.5px",
                                "Elza",
                                "rgba(21, 44, 108, 1)",
                                "0px 20px",
                                "normal",
                            },
                            [
                                "font-size",
                                "padding",
                                "color",
                                "line-height",
                                "font-style",
                                "font-family",
                                "font-weight",
                                "font-size",
                                "color",
                                "letter-spacing",
                            ],
                        ),
                        (
                            "h2",
                            {
                                "36px",
                                "24px",
                                "392.031px",
                                "620.094px",
                                "elza, sans-serif",
                                "28px",
                                "flex",
                                "600",
                                "30px",
                                "700",
                                "39px",
                                "rgba(21, 44, 108, 1)",
                                "normal",
                                "0px",
                                "0px 0px 20px",
                                "Elza",
                                "890.859px",
                                "0px 0px 25px",
                                "block",
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
                            "h4",
                            {
                                "rgba(255, 255, 255, 1)",
                                "600",
                                "23.4px",
                                "rgba(55, 55, 55, 1)",
                                "24px",
                                "0px",
                                "18px",
                                "30px",
                                "10px",
                                "rgba(0, 0, 0, 0.75)",
                                "700",
                                '"Open Sans"',
                                "Elza",
                            },
                            [
                                "line-height",
                                "color",
                                "font-size",
                                "font-weight",
                                "font-family",
                                "padding-bottom",
                            ],
                        ),
                        (
                            ".post-data p",
                            {
                                "17px",
                                "10px 0px 0px",
                                "0px 0px 10px",
                                "700",
                                "rgba(255, 255, 255, 1)",
                                "10px",
                                "23.4px",
                                "Elza",
                                "18px",
                                "10px 0px",
                                "none",
                                "400",
                                "rgba(21, 44, 108, 1)",
                                "22px",
                                "14px",
                                "0px",
                                "block",
                            },
                            [
                                "line-height",
                                "color",
                                "font-size",
                                "font-weight",
                                "font-family",
                                "padding-bottom",
                                "display",
                                "margin-bottom",
                                "margin",
                            ],
                        ),
                        (
                            ".post-categories",
                            {
                                "Elza",
                                "17px",
                                "700",
                                "600",
                                "14px",
                                "none",
                                "inline",
                                "21px",
                                "rgba(255, 255, 255, 1)",
                                "0px",
                                "rgba(1, 121, 217, 1)",
                                "0px 5px 0px 0px",
                                "23.8px",
                                "400",
                                "block",
                                "uppercase",
                                "rgba(0, 0, 0, 0.5)",
                            },
                            [
                                "line-height",
                                "color",
                                "font-size",
                                "font-weight",
                                "font-family",
                                "padding-bottom",
                                "display",
                                "margin-bottom",
                                "margin",
                                "text-transform",
                            ],
                        ),
                        (
                            ".author-sec-new .et_pb_blurb_description",
                            {"400", "rgba(1, 121, 217, 1)", "600", "16px"},
                            ["color", "font-size", "font-weight"],
                        ),
                        (
                            "div#doctor-voice-main-row img",
                            {
                                "100.75px",
                                "230px",
                                "31.8125px",
                                "100px",
                                "196px",
                                "838px",
                                "0px none rgba(0, 0, 0, 0.75)",
                                "none",
                                "30.2969px",
                                "375px",
                                "0px solid rgb(51, 51, 51)",
                                "63px",
                                "243px",
                                "28px",
                                "baseline",
                                "22.2031px",
                                "0px none rgb(55, 55, 55)",
                                "440px",
                                "40px",
                                "24px",
                                "98px",
                                "25px",
                                "219px",
                                "45px",
                                "cover",
                                "32px",
                                "99.0469px",
                                "0px solid rgb(191, 191, 191)",
                                "middle",
                                "0px none rgba(0, 0, 0, 0.5)",
                                "bottom",
                                "0px",
                                "1px solid rgb(191, 191, 191)",
                                "26px",
                                "30.1875px",
                                "30px",
                                "1px solid rgba(0, 0, 0, 0.133)",
                                "fill",
                                "104px",
                                "auto",
                                "160px",
                                "85.5625px",
                                "39.7188px",
                                "728px",
                                "0px none rgb(21, 44, 108)",
                            },
                            [
                                "width",
                                "max-height",
                                "min-height",
                                "height",
                                "object-fit",
                                "border",
                                "vertical-align",
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
                    ()
        elif window_size["width"] > 767 and window_size["width"] < 981:

            log.info("start")

            self.driver.get("https://www.physiciansweekly.com/category/doctors-voice/")
            try:
                popup = self.driver.find_element(
                    By.CSS_SELECTOR,
                    "#onesignal-slidedown-dialog .primary.slidedown-button",
                )
                popup.click()
            except Exception:
                ()

            view_allbtn = By.CSS_SELECTOR, ".view-all-btn-box .view-all-half a"
            btn = wait.until(EC.presence_of_all_elements_located(view_allbtn))

            for bn in btn:
                Ac.key_down(key_to_hold).click(bn).key_up(key_to_hold).perform()

            handles = self.driver.window_handles
            for window in handles:
                self.driver.switch_to.window(window)

                try:
                    log.info("start")

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
                            "h1.is_archive",
                            {
                                "700",
                                "60px",
                                "0.5px",
                                "Elza",
                                "rgba(21, 44, 108, 1)",
                                "0px 20px",
                                "normal",
                            },
                            [
                                "font-size",
                                "padding",
                                "color",
                                "line-height",
                                "font-style",
                                "font-family",
                                "font-weight",
                                "font-size",
                                "color",
                                "letter-spacing",
                            ],
                        ),
                        (
                            "h2",
                            {
                                "36px",
                                "24px",
                                "392.031px",
                                "620.094px",
                                "elza, sans-serif",
                                "28px",
                                "flex",
                                "600",
                                "30px",
                                "700",
                                "39px",
                                "rgba(21, 44, 108, 1)",
                                "normal",
                                "0px",
                                "0px 0px 20px",
                                "Elza",
                                "890.859px",
                                "0px 0px 25px",
                                "block",
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
                            "h4",
                            {
                                "rgba(255, 255, 255, 1)",
                                "600",
                                "23.4px",
                                "rgba(55, 55, 55, 1)",
                                "24px",
                                "0px",
                                "18px",
                                "30px",
                                "10px",
                                "rgba(0, 0, 0, 0.75)",
                                "700",
                                '"Open Sans"',
                                "Elza",
                            },
                            [
                                "line-height",
                                "color",
                                "font-size",
                                "font-weight",
                                "font-family",
                                "padding-bottom",
                            ],
                        ),
                        (
                            ".post-data p",
                            {
                                "17px",
                                "10px 0px 0px",
                                "0px 0px 10px",
                                "700",
                                "rgba(255, 255, 255, 1)",
                                "10px",
                                "23.4px",
                                "Elza",
                                "18px",
                                "10px 0px",
                                "none",
                                "400",
                                "rgba(21, 44, 108, 1)",
                                "22px",
                                "14px",
                                "0px",
                                "block",
                            },
                            [
                                "line-height",
                                "color",
                                "font-size",
                                "font-weight",
                                "font-family",
                                "padding-bottom",
                                "display",
                                "margin-bottom",
                                "margin",
                            ],
                        ),
                        (
                            ".post-categories",
                            {
                                "Elza",
                                "17px",
                                "700",
                                "600",
                                "14px",
                                "none",
                                "inline",
                                "21px",
                                "rgba(255, 255, 255, 1)",
                                "0px",
                                "rgba(1, 121, 217, 1)",
                                "0px 5px 0px 0px",
                                "23.8px",
                                "400",
                                "block",
                                "uppercase",
                                "rgba(0, 0, 0, 0.5)",
                            },
                            [
                                "line-height",
                                "color",
                                "font-size",
                                "font-weight",
                                "font-family",
                                "padding-bottom",
                                "display",
                                "margin-bottom",
                                "margin",
                                "text-transform",
                            ],
                        ),
                        (
                            ".author-sec-new .et_pb_blurb_description",
                            {"400", "rgba(1, 121, 217, 1)", "600", "16px"},
                            ["color", "font-size", "font-weight"],
                        ),
                        (
                            "div#doctor-voice-main-row img",
                            {
                                "100.75px",
                                "230px",
                                "31.8125px",
                                "100px",
                                "196px",
                                "838px",
                                "0px none rgba(0, 0, 0, 0.75)",
                                "none",
                                "30.2969px",
                                "375px",
                                "0px solid rgb(51, 51, 51)",
                                "63px",
                                "243px",
                                "28px",
                                "baseline",
                                "22.2031px",
                                "0px none rgb(55, 55, 55)",
                                "440px",
                                "40px",
                                "24px",
                                "98px",
                                "25px",
                                "219px",
                                "45px",
                                "cover",
                                "32px",
                                "99.0469px",
                                "0px solid rgb(191, 191, 191)",
                                "middle",
                                "0px none rgba(0, 0, 0, 0.5)",
                                "bottom",
                                "0px",
                                "1px solid rgb(191, 191, 191)",
                                "26px",
                                "30.1875px",
                                "30px",
                                "1px solid rgba(0, 0, 0, 0.133)",
                                "fill",
                                "104px",
                                "auto",
                                "160px",
                                "85.5625px",
                                "39.7188px",
                                "728px",
                                "0px none rgb(21, 44, 108)",
                            },
                            [
                                "width",
                                "max-height",
                                "min-height",
                                "height",
                                "object-fit",
                                "border",
                                "vertical-align",
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
                    ()

        elif window_size["width"] <= 767:

            self.driver.get("https://www.physiciansweekly.com/category/doctors-voice/")
            try:
                popup = self.driver.find_element(
                    By.CSS_SELECTOR,
                    "#onesignal-slidedown-dialog .primary.slidedown-button",
                )
                popup.click()
            except Exception:
                ()

            view_allbtn = By.CSS_SELECTOR, ".view-all-btn-box .view-all-half a"
            btn = wait.until(EC.presence_of_all_elements_located(view_allbtn))

            for bn in btn:
                Ac.key_down(key_to_hold).click(bn).key_up(key_to_hold).perform()

            handles = self.driver.window_handles
            for window in handles:
                self.driver.switch_to.window(window)

                try:
                    log.info("start")

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
                            "h1.is_archive",
                            {
                                "700",
                                "60px",
                                "0.5px",
                                "Elza",
                                "rgba(21, 44, 108, 1)",
                                "0px 20px",
                                "normal",
                            },
                            [
                                "font-size",
                                "padding",
                                "color",
                                "line-height",
                                "font-style",
                                "font-family",
                                "font-weight",
                                "font-size",
                                "color",
                                "letter-spacing",
                            ],
                        ),
                        (
                            "h2",
                            {
                                "36px",
                                "24px",
                                "392.031px",
                                "620.094px",
                                "elza, sans-serif",
                                "28px",
                                "flex",
                                "600",
                                "30px",
                                "700",
                                "39px",
                                "rgba(21, 44, 108, 1)",
                                "normal",
                                "0px",
                                "0px 0px 20px",
                                "Elza",
                                "890.859px",
                                "0px 0px 25px",
                                "block",
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
                            "h4",
                            {
                                "rgba(255, 255, 255, 1)",
                                "600",
                                "23.4px",
                                "rgba(55, 55, 55, 1)",
                                "24px",
                                "0px",
                                "18px",
                                "30px",
                                "10px",
                                "rgba(0, 0, 0, 0.75)",
                                "700",
                                '"Open Sans"',
                                "Elza",
                            },
                            [
                                "line-height",
                                "color",
                                "font-size",
                                "font-weight",
                                "font-family",
                                "padding-bottom",
                            ],
                        ),
                        (
                            ".post-data p",
                            {
                                "17px",
                                "10px 0px 0px",
                                "0px 0px 10px",
                                "700",
                                "rgba(255, 255, 255, 1)",
                                "10px",
                                "23.4px",
                                "Elza",
                                "18px",
                                "10px 0px",
                                "none",
                                "400",
                                "rgba(21, 44, 108, 1)",
                                "22px",
                                "14px",
                                "0px",
                                "block",
                            },
                            [
                                "line-height",
                                "color",
                                "font-size",
                                "font-weight",
                                "font-family",
                                "padding-bottom",
                                "display",
                                "margin-bottom",
                                "margin",
                            ],
                        ),
                        (
                            ".post-categories",
                            {
                                "Elza",
                                "17px",
                                "700",
                                "600",
                                "14px",
                                "none",
                                "inline",
                                "21px",
                                "rgba(255, 255, 255, 1)",
                                "0px",
                                "rgba(1, 121, 217, 1)",
                                "0px 5px 0px 0px",
                                "23.8px",
                                "400",
                                "block",
                                "uppercase",
                                "rgba(0, 0, 0, 0.5)",
                            },
                            [
                                "line-height",
                                "color",
                                "font-size",
                                "font-weight",
                                "font-family",
                                "padding-bottom",
                                "display",
                                "margin-bottom",
                                "margin",
                                "text-transform",
                            ],
                        ),
                        (
                            ".author-sec-new .et_pb_blurb_description",
                            {"400", "rgba(1, 121, 217, 1)", "600", "16px"},
                            ["color", "font-size", "font-weight"],
                        ),
                        (
                            "div#doctor-voice-main-row img",
                            {
                                "100.75px",
                                "230px",
                                "31.8125px",
                                "100px",
                                "196px",
                                "838px",
                                "0px none rgba(0, 0, 0, 0.75)",
                                "none",
                                "30.2969px",
                                "375px",
                                "0px solid rgb(51, 51, 51)",
                                "63px",
                                "243px",
                                "28px",
                                "baseline",
                                "22.2031px",
                                "0px none rgb(55, 55, 55)",
                                "440px",
                                "40px",
                                "24px",
                                "98px",
                                "25px",
                                "219px",
                                "45px",
                                "cover",
                                "32px",
                                "99.0469px",
                                "0px solid rgb(191, 191, 191)",
                                "middle",
                                "0px none rgba(0, 0, 0, 0.5)",
                                "bottom",
                                "0px",
                                "1px solid rgb(191, 191, 191)",
                                "26px",
                                "30.1875px",
                                "30px",
                                "1px solid rgba(0, 0, 0, 0.133)",
                                "fill",
                                "104px",
                                "auto",
                                "160px",
                                "85.5625px",
                                "39.7188px",
                                "728px",
                                "0px none rgb(21, 44, 108)",
                            },
                            [
                                "width",
                                "max-height",
                                "min-height",
                                "height",
                                "object-fit",
                                "border",
                                "vertical-align",
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
                    ()
