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


class Testone(BaseClass):
    def test_HomePageDoctorvoice(self):
        wait = WebDriverWait(self.driver, 20)
        name = self.driver.name

        log = self.getLogger()
        log.info(name)
        helper = SeleniumHelper(self.driver)

        window_size = self.driver.get_window_size()
        if window_size["width"] > 980:
            popup = self.driver.find_element(
                By.CSS_SELECTOR, "#onesignal-slidedown-dialog .primary.slidedown-button"
            )
            popup.click()

            log.info("start")

            selectors_and_properties = [
                (
                    "#doctorVoicesection div#doctorVoiceFeatureblog",
                    {"3%", "55%", "1px solid #bfbfbf", "40px"},
                    ["margin-right", "width", "border-right", "padding-right"],
                ),
                (
                    ".post-categories",
                    {"5px", "uppercase", "#0179d9", "18px", "600", "14px", "Elza"},
                    [
                        "margin-bottom",
                        "text-transform",
                        "color",
                        "line-height",
                        "font-weight",
                        "font-size",
                        "font-family",
                    ],
                ),
                (
                    "#doctorVoicesection div#doctorVoiceFeatureblog .featuredDoctorpost article .post-media",
                    {"100%", "100%"},
                    ["height", "width"],
                ),
                (
                    "#doctorVoicesection div#doctorVioceblogsec article a img",
                    {"cover", "183px", "100%"},
                    ["object-fit", "height"],
                ),
                (
                    "#doctorVoicesection div#doctorVioceblogsec article a img",
                    {"cover", "height", "100%"},
                    ["object-fit", "height", "max-width"],
                ),
                (
                    "#doctorVoicesection div#doctorVioceblogsec article .post-content h2.entry-title a",
                    {"none", "#152c6c", "30px", "600", "24px", "Elza"},
                    [
                        "text-transform",
                        "color",
                        "line-height",
                        "font-weight",
                        "font-size",
                        "font-family",
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

            selectors = ["#doctorVoicesection a"]
            additional_links = ["https://www.physiciansweekly.com/"]
            expected_link_count = 13

            log.info("Verifying links for multiple selectors")
            helper.verify_links(selectors, additional_links, expected_link_count)
            log.info("All links verified successfully")

        elif window_size["width"] > 767 and window_size["width"] < 981:

            log.info("start")

            selectors_and_properties = [
                (
                    "#doctorVoicesection div#doctorVoiceFeatureblog",
                    {"3%", "55%", "1px solid #bfbfbf", "40px"},
                    ["margin-right", "width", "border-right", "padding-right"],
                ),
                (
                    ".post-categories",
                    {
                        "uppercase",
                        "left",
                        ".025em",
                        "17px",
                        "700",
                        "14px",
                        "Elza",
                        "rgba(1, 121, 217, 1)",
                    },
                    [
                        "text-transform",
                        "text-align",
                        "letter-spacing",
                        "line-height",
                        "font-weight",
                        "font-size",
                        "font-family",
                        "color",
                    ],
                ),
                (
                    "#doctorVoicesection div#doctorVioceblogsec article a img",
                    {"cover", "height", "100%"},
                    ["object-fit", "height", "max-width"],
                ),
                (
                    "#doctorVoicesection div#doctorVioceblogsec article .post-content h2.entry-title a",
                    {"none", "#152c6c", "30px", "600", "24px", "Elza"},
                    [
                        "text-transform",
                        "color",
                        "line-height",
                        "font-weight",
                        "font-size",
                        "font-family",
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

            selectors = [
                "#Editorpickssec .editorBlog h2.entry-title a",
                ".et_pb_post_extra .post-categories",
                "#Editorpickssec .editorBlog .post-media a",
            ]
            additional_links = ["https://www.physiciansweekly.com/"]
            expected_link_count = 13

            log.info("Verifying links for multiple selectors")
            helper.verify_links(selectors, additional_links, expected_link_count)
            log.info("All links verified successfully")

        elif window_size["width"] <= 767:

            log.info("start")

            selectors_and_properties = [
                (
                    "#doctorVoicesection div#doctorVoiceFeatureblog",
                    {"3%", "55%", "1px solid #bfbfbf", "40px"},
                    ["margin-right", "width", "border-right", "padding-right"],
                ),
                (
                    ".post-categories",
                    {"5px", "uppercase", "#0179d9", "18px", "600", "14px", "Elza"},
                    [
                        "margin-bottom",
                        "text-transform",
                        "color",
                        "line-height",
                        "font-weight",
                        "font-size",
                        "font-family",
                    ],
                ),
                (
                    "#doctorVoicesection div#doctorVoiceFeatureblog .featuredDoctorpost article .post-media",
                    {"100%", "100%"},
                    ["height", "width"],
                ),
                (
                    "#doctorVoicesection div#doctorVioceblogsec article a img",
                    {"cover", "183px", "100%"},
                    ["object-fit", "height"],
                ),
                (
                    "#doctorVoicesection div#doctorVioceblogsec article a img",
                    {"cover", "height", "100%"},
                    ["object-fit", "height", "max-width"],
                ),
                (
                    "#doctorVoicesection div#doctorVioceblogsec article .post-content h2.entry-title a",
                    {"none", "#152c6c", "30px", "600", "24px", "Elza"},
                    [
                        "text-transform",
                        "color",
                        "line-height",
                        "font-weight",
                        "font-size",
                        "font-family",
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

            selectors = ["#doctorVoicesection a"]
            additional_links = ["https://www.physiciansweekly.com/"]
            expected_link_count = 8

            log.info("Verifying links for multiple selectors")
            helper.verify_links(selectors, additional_links, expected_link_count)
            log.info("All links verified successfully")
