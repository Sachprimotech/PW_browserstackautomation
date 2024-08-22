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


class Testone(BaseClass):
    @pytest.mark.run(order=22)
    @pytest.mark.dependency(depends=["test_cartoonfunct"])
    def test_Cartoonarticlepage(self):
        wait = WebDriverWait(self.driver, 20)
        name = self.driver.name

        log = self.getLogger()
        log.info(name)
        helper = SeleniumHelper(self.driver)
        cartoonlinks = []
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
            self.driver.get("https://www.physiciansweekly.com/category/cartoons/")
            try:
                popup = self.driver.find_element(
                    By.CSS_SELECTOR,
                    "#onesignal-slidedown-dialog .primary.slidedown-button",
                )
                popup.click()
            except Exception:
                ()
            log.info("start")

            cartoonpages = By.CSS_SELECTOR, ".entry-title a"
            cartpages = wait.until(EC.presence_of_all_elements_located(cartoonpages))
            for pages in cartpages:
                Links = pages.get_attribute("href")
                cartoonlinks.append(Links)
            for lin in cartoonlinks:
                self.driver.execute_script("window.open(arguments[0])", lin)
            handles = self.driver.window_handles
            try:
                for window in handles:
                    self.driver.switch_to.window(window)

                    Ac = ActionChains(self.driver)

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
                            {
                                "elza",
                                "10px",
                                "rgba(1, 121, 217, 1)",
                                "30px",
                                "25px",
                                "700",
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
                            ".post-media-container",
                            {"1px solid rgb(191, 191, 191)", "282px"},
                            [
                                "height",
                                "border",
                            ],
                        ),
                        (
                            ".el-dbe-blog-extra.block_extended",
                            {"center", "flex"},
                            ["justify-content", "display"],
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
            except NoSuchElementException and TimeoutException:
                ()

        elif window_size["width"] > 767 and window_size["width"] < 981:

            log.info("start")

            self.driver.get("https://www.physiciansweekly.com/category/cartoons/")
            try:
                popup = self.driver.find_element(
                    By.CSS_SELECTOR,
                    "#onesignal-slidedown-dialog .primary.slidedown-button",
                )
                popup.click()
            except Exception:
                ()
            log.info("start")

            cartoonpages = By.CSS_SELECTOR, ".entry-title a"
            cartpages = wait.until(EC.presence_of_all_elements_located(cartoonpages))
            for pages in cartpages:
                Links = pages.get_attribute("href")
                cartoonlinks.append(Links)
            for lin in cartoonlinks:
                self.driver.execute_script("window.open(arguments[0])", lin)
            handles = self.driver.window_handles
            try:
                for window in handles:
                    self.driver.switch_to.window(window)

                    Ac = ActionChains(self.driver)

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
                            {
                                "elza",
                                "10px",
                                "rgba(1, 121, 217, 1)",
                                "30px",
                                "25px",
                                "700",
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
                            ".post-media-container",
                            {"1px solid rgb(191, 191, 191)", "282px"},
                            [
                                "height",
                                "border",
                            ],
                        ),
                        (
                            ".el-dbe-blog-extra.block_extended",
                            {"center", "flex"},
                            ["justify-content", "display"],
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
            except NoSuchElementException and TimeoutException:
                ()

        elif window_size["width"] <= 767:

            self.driver.get("https://www.physiciansweekly.com/category/cartoons/")
            try:
                popup = self.driver.find_element(
                    By.CSS_SELECTOR,
                    "#onesignal-slidedown-dialog .primary.slidedown-button",
                )
                popup.click()
            except Exception:
                ()
            log.info("start")

            cartoonpages = By.CSS_SELECTOR, ".entry-title a"
            cartpages = wait.until(EC.presence_of_all_elements_located(cartoonpages))
            for pages in cartpages:
                Links = pages.get_attribute("href")
                cartoonlinks.append(Links)
            for lin in cartoonlinks:
                self.driver.execute_script("window.open(arguments[0])", lin)
            handles = self.driver.window_handles
            try:
                for window in handles:
                    self.driver.switch_to.window(window)

                    Ac = ActionChains(self.driver)

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
                            {
                                "elza",
                                "10px",
                                "rgba(1, 121, 217, 1)",
                                "30px",
                                "25px",
                                "700",
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
                            ".post-media-container",
                            {"1px solid rgb(191, 191, 191)", "282px"},
                            [
                                "height",
                                "border",
                            ],
                        ),
                        (
                            ".el-dbe-blog-extra.block_extended",
                            {"center", "flex"},
                            ["justify-content", "display"],
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
            except NoSuchElementException and TimeoutException:
                ()
