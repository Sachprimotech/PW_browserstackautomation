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
    @pytest.mark.run(order=3)
    @pytest.mark.dependency(depends=["test_HomePageslider"])
    def test_HomePageNews(self):
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
                    "#newsSection .et_pb_with_border",
                    {"0px none rgba(0, 0, 0, 0.5)", "8.4375px", "0px", "25.5938px"},
                    ["margin-right", "padding-right", "border"],
                ),
                # (
                #     "#newsSection .newsFeaturedblog .swiper-pagination.swiper-pagination-clickable.swiper-pagination-bullets",
                #     {"0 50px", "-56px"},
                #     ["padding", "top"],
                # ),
                (
                    ".et_pb_blog_extras_21 .et_pb_post.et_pb_post_extra .entry-title a",
                    {"700", "#FFFFFF", "39px", "Elza"},
                    ["font-weight", "font-size", "color", "font-family"],
                ),
                (
                    "#newsSection .newRightblogsec article .post-content h2.entry-title a",
                    {"left", "23px", "500", "18px", "Elza"},
                    [
                        "text-align",
                        "line-height",
                        "font-weight",
                        "font-size",
                        "font-family",
                    ],
                ),
                (
                    "#newsSection .newRightblogsec article .post-content p.post-meta",
                    {
                        "0",
                        "block",
                        "#0179d9",
                        "left",
                        "0.025em",
                        "500",
                        "14px",
                        "Elza",
                        "18px",
                    },
                    [
                        "margin",
                        "display",
                        "color",
                        "text-align",
                        "line-height",
                        "font-weight",
                        "font-size",
                        "font-family",
                        "letter-spacing",
                    ],
                ),
                (
                    ".et_pb_section_15",
                    {"0px", "20px", "0px", "20px"},
                    ["padding-top", "padding-right", "padding-bottom", "padding-left"],
                ),
                (
                    "p.post-meta",
                    {
                        "12px",
                        "uppercase",
                        "14px",
                        "400",
                        "18px",
                        "none",
                        "0px",
                        "28px",
                        "22px",
                        "block",
                        "left",
                        "normal",
                        "rgba(255, 255, 255, 1)",
                        "Elza",
                        "500",
                        "rgba(1, 121, 217, 1)",
                        "rgba(21, 44, 108, 1)",
                        "20.4px",
                        "0px 0px 6px",
                        "0.35px",
                    },
                    [
                        "margin",
                        "display",
                        "color",
                        "text-align",
                        "line-height",
                        "font-weight",
                        "font-size",
                        "font-family",
                        "letter-spacing",
                        "text-transform",
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

            selectors = [".et_pb_section_15 a"]
            additional_links = ["https://www.physiciansweekly.com/"]
            expected_link_count = 13

            log.info("Verifying links for multiple selectors")
            helper.verify_links(selectors, additional_links, expected_link_count)
            log.info("All links verified successfully")

        elif window_size["width"] > 767 and window_size["width"] < 981:

            log.info("start")

            selectors_and_properties = [
                (
                    "#newsSection .et_pb_with_border",
                    {"0px none rgba(0, 0, 0, 0.5)", "0px"},
                    ["margin-right", "padding-right", "border"],
                ),
                # (
                #     "#newsSection .newsFeaturedblog .swiper-pagination.swiper-pagination-clickable.swiper-pagination-bullets",
                #     {"0 50px", "-56px"},
                #     ["padding", "top"],
                # ),
                (
                    ".et_pb_blog_extras_21 .et_pb_post.et_pb_post_extra .entry-title a",
                    {"700", "#FFFFFF", "39px", "Elza"},
                    ["font-weight", "font-size", "color", "font-family"],
                ),
                (
                    "#newsSection .newRightblogsec article .post-content h2.entry-title a",
                    {"left", "23px", "500", "18px", "Elza"},
                    [
                        "text-align",
                        "line-height",
                        "font-weight",
                        "font-size",
                        "font-family",
                    ],
                ),
                (
                    "#newsSection .newRightblogsec article .post-content p.post-meta",
                    {
                        "0",
                        "block",
                        "#0179d9",
                        "left",
                        "0.025em",
                        "500",
                        "14px",
                        "Elza",
                        "18px",
                    },
                    [
                        "margin",
                        "display",
                        "color",
                        "text-align",
                        "line-height",
                        "font-weight",
                        "font-size",
                        "font-family",
                        "letter-spacing",
                    ],
                ),
                (
                    ".et_pb_section_15",
                    {"0px", "20px", "0px", "20px"},
                    ["padding-top", "padding-right", "padding-bottom", "padding-left"],
                ),
                (
                    "p.post-meta",
                    {
                        "12px",
                        "uppercase",
                        "14px",
                        "400",
                        "18px",
                        "none",
                        "0px",
                        "28px",
                        "22px",
                        "block",
                        "left",
                        "normal",
                        "rgba(255, 255, 255, 1)",
                        "Elza",
                        "500",
                        "rgba(1, 121, 217, 1)",
                        "rgba(21, 44, 108, 1)",
                        "20.4px",
                        "0px 0px 6px",
                        "0.35px",
                    },
                    [
                        "margin",
                        "display",
                        "color",
                        "text-align",
                        "line-height",
                        "font-weight",
                        "font-size",
                        "font-family",
                        "letter-spacing",
                        "text-transform",
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

            selectors = [".et_pb_section_15 a"]
            additional_links = ["https://www.physiciansweekly.com/"]
            expected_link_count = 13

            log.info("Verifying links for multiple selectors")
            helper.verify_links(selectors, additional_links, expected_link_count)
            log.info("All links verified successfully")

        elif window_size["width"] <= 767:

            log.info("start")

            selectors_and_properties = [
                (
                    "#newsSection .et_pb_with_border",
                    {"0px none rgba(0, 0, 0, 0.5)", "0px"},
                    ["margin-right", "padding-right", "border"],
                ),
                # (
                #     "#newsSection .newsFeaturedblog .swiper-pagination.swiper-pagination-clickable.swiper-pagination-bullets",
                #     {"0 50px", "-56px"},
                #     ["padding", "top"],
                # ),
                (
                    ".et_pb_blog_extras_21 .et_pb_post.et_pb_post_extra .entry-title a",
                    {"700", "#FFFFFF", "39px", "Elza"},
                    ["font-weight", "font-size", "color", "font-family"],
                ),
                (
                    "#newsSection .newRightblogsec article .post-content h2.entry-title a",
                    {"left", "23px", "500", "18px", "Elza"},
                    [
                        "text-align",
                        "line-height",
                        "font-weight",
                        "font-size",
                        "font-family",
                    ],
                ),
                (
                    "#newsSection .newRightblogsec article .post-content p.post-meta",
                    {
                        "0",
                        "block",
                        "#0179d9",
                        "left",
                        "0.025em",
                        "500",
                        "14px",
                        "Elza",
                        "18px",
                    },
                    [
                        "margin",
                        "display",
                        "color",
                        "text-align",
                        "line-height",
                        "font-weight",
                        "font-size",
                        "font-family",
                        "letter-spacing",
                    ],
                ),
                (
                    ".et_pb_section_15",
                    {"0px", "20px", "0px", "20px"},
                    ["padding-top", "padding-right", "padding-bottom", "padding-left"],
                ),
                (
                    "p.post-meta",
                    {
                        "12px",
                        "uppercase",
                        "14px",
                        "400",
                        "18px",
                        "none",
                        "0px",
                        "28px",
                        "22px",
                        "block",
                        "left",
                        "normal",
                        "rgba(255, 255, 255, 1)",
                        "Elza",
                        "500",
                        "rgba(1, 121, 217, 1)",
                        "rgba(21, 44, 108, 1)",
                        "20.4px",
                        "0px 0px 6px",
                        "0.35px",
                    },
                    [
                        "margin",
                        "display",
                        "color",
                        "text-align",
                        "line-height",
                        "font-weight",
                        "font-size",
                        "font-family",
                        "letter-spacing",
                        "text-transform",
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

            selectors = [".et_pb_section_15 a"]
            additional_links = ["https://www.physiciansweekly.com/"]
            expected_link_count = 13

            log.info("Verifying links for multiple selectors")
            helper.verify_links(selectors, additional_links, expected_link_count)
            log.info("All links verified successfully")
