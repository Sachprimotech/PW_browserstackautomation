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
import asyncio


class Testone(BaseClass):
    @pytest.mark.run(order=41)
    @pytest.mark.dependency(depends=["test_HomePagesspecialityUI"])
    def test_spotlightlandingpage(self):
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
            tagslinks = (
                By.CSS_SELECTOR,
                "#wekly-news-container ul.meeting-coverage-list li",
            )
            tagsclicks = wait.until(EC.presence_of_all_elements_located(tagslinks))
            for tagclick in tagsclicks:
                Ac.move_to_element(tagclick).click().perform()
                time.sleep(2)

            selectors_and_properties = [
                (
                    "#et-boc .breadcrumb #crumbs",  # present
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
                    "#crumbs .current",  # present
                    {".02em", "500"},
                    ["letter-spacing", "font-weight"],
                ),
                (".breadcrumb", {"10px 0"}, ["margin"]),
                (
                    "h1.is_archive",  # present
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
                    "h2",  # present
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
                    "h3",
                    {"elza", "10px", "rgba(1, 121, 217, 1)", "30px", "25px", "700"},
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
                    ".cat-meeting-coverage-section .post-data p",
                    {
                        "0px",
                        "32px",
                        "block",
                        "elza, sans-serif",
                        "28px",
                        "rgba(55, 55, 55, 1)",
                        "20px",
                        "0px 0px 32px",
                        "400",
                        "20px 0px 0px",
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
                    ".spotlights-post-media img",
                    {"600px", "1px solid rgb(191, 191, 191)", "cover", "340px"},
                    [
                        "width",
                        "max-height",
                        "min-height",
                        "height",
                        "object-fit",
                        "border",
                    ],
                ),
                (
                    "#wekly-news-container ul.meeting-coverage-list li a",
                    {
                        "elza",
                        "24px",
                        "rgba(21, 44, 108, 1)",
                        "600",
                        "normal",
                        "0px",
                        "none solid rgb(21, 44, 108)",
                        "20px",
                    },
                    [
                        "color",
                        "font-size",
                        "font-weight",
                        "padding",
                        "font-family",
                        "line-height",
                        "text-decoration",
                        "font-style",
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

            selectors = [".spotlights-post-content p.read-more-link a"]
            asyncio.run(SeleniumHelper.verify_links_async(self, selectors))
            log.info("All links verified successfully")

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
            tagslinks = (
                By.CSS_SELECTOR,
                "#wekly-news-container ul.meeting-coverage-list li a",
            )
            tagsclicks = wait.until(EC.presence_of_all_elements_located(tagslinks))
            for tagclick in tagsclicks:
                Ac.move_to_element(tagclick).click().perform()

            selectors_and_properties = [
                (
                    "#et-boc .breadcrumb #crumbs",  # present
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
                    "#crumbs .current",  # present
                    {".02em", "500"},
                    ["letter-spacing", "font-weight"],
                ),
                (".breadcrumb", {"10px 0"}, ["margin"]),
                (
                    "h1.is_archive",  # present
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
                    "h2",  # present
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
                    "h3",
                    {"elza", "10px", "rgba(1, 121, 217, 1)", "30px", "25px", "700"},
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
                    ".cat-meeting-coverage-section .post-data p",
                    {
                        "0px",
                        "32px",
                        "block",
                        "elza, sans-serif",
                        "28px",
                        "rgba(55, 55, 55, 1)",
                        "20px",
                        "0px 0px 32px",
                        "400",
                        "20px 0px 0px",
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
                    ".spotlights-post-media img",
                    {"600px", "1px solid rgb(191, 191, 191)", "cover", "340px"},
                    [
                        "width",
                        "max-height",
                        "min-height",
                        "height",
                        "object-fit",
                        "border",
                    ],
                ),
                (
                    "#wekly-news-container ul.meeting-coverage-list li a",
                    {
                        "elza",
                        "24px",
                        "rgba(21, 44, 108, 1)",
                        "600",
                        "normal",
                        "0px",
                        "none solid rgb(21, 44, 108)",
                        "20px",
                    },
                    [
                        "color",
                        "font-size",
                        "font-weight",
                        "padding",
                        "font-family",
                        "line-height",
                        "text-decoration",
                        "font-style",
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
            selectors = [".spotlights-post-content p.read-more-link a"]
            asyncio.run(SeleniumHelper.verify_links_async(self, selectors))
            log.info("All links verified successfully")

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

            tagslinks = (
                By.CSS_SELECTOR,
                "#wekly-news-container ul.meeting-coverage-list li a",
            )
            tagsclicks = wait.until(EC.presence_of_all_elements_located(tagslinks))
            for tagclick in tagsclicks:
                Ac.move_to_element(tagclick).click().perform()

            selectors_and_properties = [
                (
                    "#et-boc .breadcrumb #crumbs",  # present
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
                    "#crumbs .current",  # present
                    {".02em", "500"},
                    ["letter-spacing", "font-weight"],
                ),
                (".breadcrumb", {"10px 0"}, ["margin"]),
                (
                    "h1.is_archive",  # present
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
                    "h2",  # present
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
                    "h3",
                    {"elza", "10px", "rgba(1, 121, 217, 1)", "30px", "25px", "700"},
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
                    ".cat-meeting-coverage-section .post-data p",
                    {
                        "0px",
                        "32px",
                        "block",
                        "elza, sans-serif",
                        "28px",
                        "rgba(55, 55, 55, 1)",
                        "20px",
                        "0px 0px 32px",
                        "400",
                        "20px 0px 0px",
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
                    ".spotlights-post-media img",
                    {"600px", "1px solid rgb(191, 191, 191)", "cover", "340px"},
                    [
                        "width",
                        "max-height",
                        "min-height",
                        "height",
                        "object-fit",
                        "border",
                    ],
                ),
                (
                    "#wekly-news-container ul.meeting-coverage-list li a",
                    {
                        "elza",
                        "24px",
                        "rgba(21, 44, 108, 1)",
                        "600",
                        "normal",
                        "0px",
                        "none solid rgb(21, 44, 108)",
                        "20px",
                    },
                    [
                        "color",
                        "font-size",
                        "font-weight",
                        "padding",
                        "font-family",
                        "line-height",
                        "text-decoration",
                        "font-style",
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
            selectors = [".spotlights-post-content p.read-more-link a"]
            asyncio.run(SeleniumHelper.verify_links_async(self, selectors))
            log.info("All links verified successfully")
