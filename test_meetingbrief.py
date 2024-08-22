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


class Testone(BaseClass):
    @pytest.mark.run(order=30)
    @pytest.mark.dependency(depends=["test_Meetingsbriefprogramelinks"])
    def test_Meetingsbrief(self):
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
            while True:
                try:
                    next = By.XPATH, "//a[@class='next page-numbers']"
                    nextbutton = wait.until(EC.presence_of_element_located(next))
                except Exception:
                    break
                if nextbutton:

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
                            "div#et-boc div#doctor-voice-sec .cat-section article",
                            {"32.4%", "1px solid rgb(191, 191, 191)", "15px"},
                            ["padding-bottom", "width", "border-bottom"],
                        ),
                        (
                            ".meeting_brief_new_navigation",
                            {"0px 20px", "0px 76.5px"},
                            ["margin", "padding"],
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
                    Ac.move_to_element(nextbutton).click().perform()
                else:
                    break

            log.info("no-element")
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
                    "div#et-boc div#doctor-voice-sec .cat-section article",
                    {"32.4%", "1px solid rgb(191, 191, 191)", "15px"},
                    ["padding-bottom", "width", "border-bottom"],
                ),
                (
                    ".meeting_brief_new_navigation",
                    {"0px 20px", "0px 76.5px"},
                    ["margin", "padding"],
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

            Ac = ActionChains(self.driver)
            while True:
                try:
                    next = By.XPATH, "//a[@class='next page-numbers']"
                    nextbutton = wait.until(EC.presence_of_element_located(next))
                except Exception:
                    break
                if nextbutton:

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
                            "div#et-boc div#doctor-voice-sec .cat-section article",
                            {"32.4%", "1px solid rgb(191, 191, 191)", "15px"},
                            ["padding-bottom", "width", "border-bottom"],
                        ),
                        (
                            ".meeting_brief_new_navigation",
                            {"0px 20px", "0px 76.5px"},
                            ["margin", "padding"],
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
                    Ac.move_to_element(nextbutton).click().perform()
                else:
                    break

            log.info("no-element")
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
                    "div#et-boc div#doctor-voice-sec .cat-section article",
                    {"32.4%", "1px solid rgb(191, 191, 191)", "15px"},
                    ["padding-bottom", "width", "border-bottom"],
                ),
                (
                    ".meeting_brief_new_navigation",
                    {"0px 20px", "0px 76.5px"},
                    ["margin", "padding"],
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
            while True:
                try:
                    next = By.XPATH, "//a[@class='next page-numbers']"
                    nextbutton = wait.until(EC.presence_of_element_located(next))
                except Exception:
                    break
                if nextbutton:

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
                            "div#et-boc div#doctor-voice-sec .cat-section article",
                            {"32.4%", "1px solid rgb(191, 191, 191)", "15px"},
                            ["padding-bottom", "width", "border-bottom"],
                        ),
                        (
                            ".meeting_brief_new_navigation",
                            {"0px 20px", "0px 76.5px"},
                            ["margin", "padding"],
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
                    Ac.move_to_element(nextbutton).click().perform()
                else:
                    break

            log.info("no-element")
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
                    "div#et-boc div#doctor-voice-sec .cat-section article",
                    {"32.4%", "1px solid rgb(191, 191, 191)", "15px"},
                    ["padding-bottom", "width", "border-bottom"],
                ),
                (
                    ".meeting_brief_new_navigation",
                    {"0px 20px", "0px 76.5px"},
                    ["margin", "padding"],
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
