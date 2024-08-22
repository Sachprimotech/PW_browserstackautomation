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
    @pytest.mark.run(order=36)
    @pytest.mark.dependency(depends=["test_peer_peerprogramelinks"])
    def test_prePodcastui(self):
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
            self.driver.get("https://www.physiciansweekly.com/podcast/")
            try:
                popup = self.driver.find_element(
                    By.CSS_SELECTOR,
                    "#onesignal-slidedown-dialog .primary.slidedown-button",
                )
                popup.click()
            except Exception:
                ()
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
                    ".et_pb_section div[class*=et_pb_row_]",
                    {
                        "40px 71.5px 0px",
                        "57px 0px 0px",
                        "7px 20px 43px",
                        "40px 51.5px 0px",
                        "0px 10px",
                        "0px 71.5px",
                        "55px 0px",
                        "65px 71.5px 40px",
                        "30px 20px 40px",
                        "1230px",
                        "30px 0px 0px",
                        "1280px",
                        "0px 51.5px",
                        "400",
                        "65px auto 40px",
                        "100%",
                        "20px 71.5px 0px",
                        "0px",
                    },
                    [
                        "width",
                        "padding",
                        "margin",
                        "font-weight",
                        "max-width",
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
                    ".category .et_pb_gutters3 .et_pb_column_2_3",
                    {"876.891px", "44.7969px", "65.5%", "838.391px", "3.5%", "0px"},
                    ["margin-right", "width"],
                ),
                (
                    "#in-this-section #cat-in-this .et-menu li a",
                    {
                        "normal",
                        "7px 10px 5px",
                        "rgba(21, 44, 108, 1)",
                        "rgba(1, 121, 217, 0.25) none repeat scroll 0% 0% / auto padding-box border-box",
                        "14px",
                        "uppercase",
                        "17px",
                        "600",
                        "rgb(223, 223, 223) none repeat scroll 0% 0% / auto padding-box border-box",
                        "Elza",
                    },
                    [
                        "padding",
                        "background",
                        "color",
                        "text-transform",
                        "line-height",
                        "font-size",
                        "font-weight",
                        "font-style",
                        "font-family",
                    ],
                ),
                (
                    ".author-sec-new .et_pb_blurb_description",
                    {"400", "rgba(1, 121, 217, 1)", "600", "16px"},
                    ["color", "font-size", "font-weight"],
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
                    ".category .et_pb_gutters3 .et_pb_column_2_3",
                    {"876.891px", "44.7969px", "65.5%", "838.391px", "3.5%", "0px"},
                    ["margin-right", "width"],
                ),
                (
                    "#in-this-section #cat-in-this .et-menu li a",
                    {
                        "normal",
                        "7px 10px 5px",
                        "rgba(21, 44, 108, 1)",
                        "rgba(1, 121, 217, 0.25) none repeat scroll 0% 0% / auto padding-box border-box",
                        "14px",
                        "uppercase",
                        "17px",
                        "600",
                        "rgb(223, 223, 223) none repeat scroll 0% 0% / auto padding-box border-box",
                        "Elza",
                    },
                    [
                        "padding",
                        "background",
                        "color",
                        "text-transform",
                        "line-height",
                        "font-size",
                        "font-weight",
                        "font-style",
                        "font-family",
                    ],
                ),
                (
                    ".author-sec-new .et_pb_blurb_description",
                    {"400", "rgba(1, 121, 217, 1)", "600", "16px"},
                    ["color", "font-size", "font-weight"],
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
