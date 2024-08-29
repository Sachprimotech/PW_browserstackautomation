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
    @pytest.mark.run(order=38)
    @pytest.mark.dependency(depends=["test_Podcastui"])
    def test_Specialities(self):
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
            self.driver.get("https://www.physiciansweekly.com/specialties/")

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
                    "#specialties-columns nav.et-menu-nav .et-menu li",
                    {
                        "404.688px",
                        "inline-block",
                        "1px solid rgb(191, 191, 191)",
                        "0px 0px 12px",
                    },
                    [
                        "display",
                        "margin",
                        "padding",
                        "border-bottom",
                        "width",
                    ],
                ),
                (
                    "#menu-specialties-1 li",
                    {
                        "inline-block",
                        "0px 0px 12px",
                        "404.688px",
                        "1px solid rgb(191, 191, 191)",
                    },
                    [
                        "display",
                        "margin",
                        "padding",
                        "border-bottom",
                        "width",
                    ],
                ),
                (
                    "#menu-specialties-1 li a",
                    {
                        "126.234px",
                        "206.359px",
                        "49.25px",
                        "elza",
                        "117.281px",
                        "152.188px",
                        "93.0312px",
                        "rgba(21, 44, 108, 1)",
                        "91.2812px",
                        "168.234px",
                        "150.875px",
                        "169.734px",
                        "122.125px",
                        "table-cell",
                        "25px",
                        "38px",
                        "143.109px",
                        "252.578px",
                        "normal",
                        "213.359px",
                        "97.0312px",
                        "120.609px",
                        "152.328px",
                        "275.438px",
                        "0px",
                        "179.453px",
                        "135.953px",
                        "600",
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
                    "h1.is_archive",
                    {
                        "700",
                        "60px",
                        "rgba(21, 44, 108, 1)",
                        "normal",
                        "0.5px",
                        "elza",
                        "0px 0px 20px",
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

            log.info("end")

            selectors = ["#menu-specialties-1 li a"]
            asyncio.run(SeleniumHelper.verify_links_async(self, selectors))
            log.info("All links verified successfully")

        elif window_size["width"] > 767 and window_size["width"] < 981:

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
                    "#specialties-columns nav.et-menu-nav .et-menu li",
                    {
                        "404.688px",
                        "inline-block",
                        "1px solid rgb(191, 191, 191)",
                        "0px 0px 12px",
                    },
                    [
                        "display",
                        "margin",
                        "padding",
                        "border-bottom",
                        "width",
                    ],
                ),
                (
                    "#menu-specialties-1 li",
                    {
                        "inline-block",
                        "0px 0px 12px",
                        "404.688px",
                        "1px solid rgb(191, 191, 191)",
                    },
                    [
                        "display",
                        "margin",
                        "padding",
                        "border-bottom",
                        "width",
                    ],
                ),
                (
                    "#menu-specialties-1 li a",
                    {
                        "126.234px",
                        "206.359px",
                        "49.25px",
                        "elza",
                        "117.281px",
                        "152.188px",
                        "93.0312px",
                        "rgba(21, 44, 108, 1)",
                        "91.2812px",
                        "168.234px",
                        "150.875px",
                        "169.734px",
                        "122.125px",
                        "table-cell",
                        "25px",
                        "38px",
                        "143.109px",
                        "252.578px",
                        "normal",
                        "213.359px",
                        "97.0312px",
                        "120.609px",
                        "152.328px",
                        "275.438px",
                        "0px",
                        "179.453px",
                        "135.953px",
                        "600",
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
                    "h1.is_archive",
                    {
                        "700",
                        "60px",
                        "rgba(21, 44, 108, 1)",
                        "normal",
                        "0.5px",
                        "elza",
                        "0px 0px 20px",
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

            log.info("end")

            selectors = ["#menu-specialties-1 li a"]
            asyncio.run(SeleniumHelper.verify_links_async(self, selectors))
            log.info("All links verified successfully")

        elif window_size["width"] <= 767:

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
                    "#specialties-columns nav.et-menu-nav .et-menu li",
                    {
                        "404.688px",
                        "inline-block",
                        "1px solid rgb(191, 191, 191)",
                        "0px 0px 12px",
                    },
                    [
                        "display",
                        "margin",
                        "padding",
                        "border-bottom",
                        "width",
                    ],
                ),
                (
                    "#menu-specialties-1 li",
                    {
                        "inline-block",
                        "0px 0px 12px",
                        "404.688px",
                        "1px solid rgb(191, 191, 191)",
                    },
                    [
                        "display",
                        "margin",
                        "padding",
                        "border-bottom",
                        "width",
                    ],
                ),
                (
                    "#menu-specialties-1 li a",
                    {
                        "126.234px",
                        "206.359px",
                        "49.25px",
                        "elza",
                        "117.281px",
                        "152.188px",
                        "93.0312px",
                        "rgba(21, 44, 108, 1)",
                        "91.2812px",
                        "168.234px",
                        "150.875px",
                        "169.734px",
                        "122.125px",
                        "table-cell",
                        "25px",
                        "38px",
                        "143.109px",
                        "252.578px",
                        "normal",
                        "213.359px",
                        "97.0312px",
                        "120.609px",
                        "152.328px",
                        "275.438px",
                        "0px",
                        "179.453px",
                        "135.953px",
                        "600",
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
                    "h1.is_archive",
                    {
                        "700",
                        "60px",
                        "rgba(21, 44, 108, 1)",
                        "normal",
                        "0.5px",
                        "elza",
                        "0px 0px 20px",
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

            log.info("end")

            selectors = ["#menu-specialties-1 li a"]
            asyncio.run(SeleniumHelper.verify_links_async(self, selectors))
            log.info("All links verified successfully")
