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
    @pytest.mark.run(order=7)
    @pytest.mark.dependency(depends=["test_HomePagespotlightandpeer"])
    def test_HomePageBusinessOfMedicine(self):
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
                    ".lwp_post_carousel_image img",
                    {"186px", "cover", "186px"},
                    ["min-height", "object-fit", "max-height"],
                ),
                (
                    "#businessOfMedisection h4 a",
                    {"125%", "600", "Elza", "20px", "#152c6c"},
                    ["line-height" "font-weight" "font-family" "font-size" "color"],
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

            selectors = [
                "#businessOfMedisection h4 a",
                ".lwp_post_carousel_image  a",
            ]

            log.info("Verifying links for multiple selectors")
            helper.verify_linkscloud(selectors)
            log.info("All links verified successfully")

        elif window_size["width"] > 767 and window_size["width"] < 981:

            log.info("start")

            selectors_and_properties = [
                (
                    ".lwp_post_carousel_image img",
                    {"186px", "cover", "186px"},
                    ["min-height", "object-fit", "max-height"],
                ),
                (
                    "#businessOfMedisection h4 a",
                    {"125%", "600", "Elza", "20px", "#152c6c"},
                    ["line-height" "font-weight" "font-family" "font-size" "color"],
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

            selectors = [
                "#businessOfMedisection h4 a",
                ".lwp_post_carousel_image  a",
            ]

            log.info("Verifying links for multiple selectors")
            helper.verify_linkscloud(selectors)
            log.info("All links verified successfully")

        elif window_size["width"] <= 767:

            log.info("start")

            selectors_and_properties = [
                (
                    ".lwp_post_carousel_image img",
                    {"186px", "cover", "186px"},
                    ["min-height", "object-fit", "max-height"],
                ),
                (
                    "#businessOfMedisection h4 a",
                    {"125%", "600", "Elza", "20px", "#152c6c"},
                    ["line-height" "font-weight" "font-family" "font-size" "color"],
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

            # selectors = [
            #     "#businessOfMedisection section.lwp-slick-slider .slick-track .slick-slide h4 a",
            #     "#businessOfMedisection section.lwp-slick-slider .slick-track .slick-slide .lwp_post_carousel_image  a",
            # ]
            # additional_links = ["https://www.physiciansweekly.com/"]
            # expected_link_count = 13

            # log.info("Verifying links for multiple selectors")
            # helper.verify_links(selectors, additional_links, expected_link_count)
            # log.info("All links verified successfully")
