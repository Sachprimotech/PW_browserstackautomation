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
    @pytest.mark.run(order=2)
    @pytest.mark.dependency(depends=["test_HomePage"])
    def test_HomePageslider(self):
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

            log.info("start")

            selectors_and_properties = [
                (
                    ".custom-slider #slider-container #slider .slide a img",
                    {
                        "cover",
                        "182px",
                        "182px",
                        "289px",
                        "1px solid rgb(191, 191, 191)",
                    },
                    ["border", "object-fit", "min-height", "max-height", "width"],
                ),
                (
                    "body.home .custom-slider .slide p",
                    {"10px", "#152c6c", "left", "0", "25px", "600", "20px", "Elza"},
                    [
                        "margin-top",
                        "color",
                        "text-align",
                        "letter-spacing",
                        "line-height",
                        "font-weight",
                        "font-size",
                        "font-family",
                    ],
                ),
                (
                    "body.home .custom-slider #slider-container .btn i",
                    {"41px", "41px"},
                    ("width", "height"),
                ),
                (
                    ".custom-slider #slider-container .btn i.fa-chevron-right",
                    {"30%", "8px"},
                    ["top", "right"],
                ),
                (
                    ".custom-slider #slider-container .btn i.fa-chevron-left",
                    {"30%", "13px"},
                    ["top", "left"],
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

            selectors = ["#home-meeting-brifs.et_pb_section  a"]
            additional_links = ["https://www.physiciansweekly.com/"]
            expected_link_count = 13

            log.info("Verifying links for multiple selectors")
            helper.verify_links(selectors, additional_links, expected_link_count)
            log.info("All links verified successfully")

        elif window_size["width"] > 767 and window_size["width"] < 981:

            log.info("start")

            selectors_and_properties = [
                (
                    ".custom-slider #slider-container #slider .slide a img",
                    {
                        "cover",
                        "182px",
                        "182px",
                        "289px",
                        "1px solid rgb(191, 191, 191)",
                    },
                    ["border", "object-fit", "min-height", "max-height", "width"],
                ),
                (
                    "body.home .custom-slider .slide p",
                    {"10px", "#152c6c", "left", "0", "25px", "600", "20px", "Elza"},
                    [
                        "margin-top",
                        "color",
                        "text-align",
                        "letter-spacing",
                        "line-height",
                        "font-weight",
                        "font-size",
                        "font-family",
                    ],
                ),
                (
                    "body.home .custom-slider #slider-container .btn i",
                    {"41px", "41px"},
                    ("width", "height"),
                ),
                (
                    ".custom-slider #slider-container .btn i.fa-chevron-right",
                    {"30%", "8px"},
                    ["top", "right"],
                ),
                (
                    ".custom-slider #slider-container .btn i.fa-chevron-left",
                    {"30%", "13px"},
                    ["top", "left"],
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

            selectors = ["#home-meeting-brifs.et_pb_section  a"]
            additional_links = ["https://www.physiciansweekly.com/"]
            expected_link_count = 13

            log.info("Verifying links for multiple selectors")
            helper.verify_links(selectors, additional_links, expected_link_count)
            log.info("All links verified successfully")

        elif window_size["width"] <= 767:

            log.info("start")

            selectors_and_properties = [
                (
                    ".custom-slider #slider-container #slider .slide a img",
                    {
                        "cover",
                        "182px",
                        "182px",
                        "289px",
                        "1px solid rgb(191, 191, 191)",
                    },
                    ["border", "object-fit", "min-height", "max-height", "width"],
                ),
                (
                    "body.home .custom-slider .slide p",
                    {"10px", "#152c6c", "left", "0", "25px", "600", "20px", "Elza"},
                    [
                        "margin-top",
                        "color",
                        "text-align",
                        "letter-spacing",
                        "line-height",
                        "font-weight",
                        "font-size",
                        "font-family",
                    ],
                ),
                (
                    "body.home .custom-slider #slider-container .btn i",
                    {"41px", "41px"},
                    ("width", "height"),
                ),
                (
                    ".custom-slider #slider-container .btn i.fa-chevron-right",
                    {"30%", "8px"},
                    ["top", "right"],
                ),
                (
                    ".custom-slider #slider-container .btn i.fa-chevron-left",
                    {"30%", "13px"},
                    ["top", "left"],
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
                ), f"CSS properties do not match the expected values for selector {css_selector,}"

            log.info("end")

            selectors = ["#home-meeting-brifs.et_pb_section  a"]
            additional_links = ["https://www.physiciansweekly.com/"]
            expected_link_count = 13

            log.info("Verifying links for multiple selectors")
            helper.verify_links(selectors, additional_links, expected_link_count)
            log.info("All links verified successfully")
