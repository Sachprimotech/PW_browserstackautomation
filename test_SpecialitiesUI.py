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


# this file is pending for changes as speciality UI
class Testone(BaseClass):
    @pytest.mark.run(order=40)
    @pytest.mark.dependency(depends=["test_specialitysection"])
    def test_HomePagesspecialityUI(self):
        wait = WebDriverWait(self.driver, 20)
        name = self.driver.name

        log = self.getLogger()
        log.info(name)
        helper = SeleniumHelper(self.driver)
        AC = ActionChains(self.driver)
        All_specialities_urls = []
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
            All_specialities = (
                By.CSS_SELECTOR,
                "#specialties-columns nav.et-menu-nav .et-menu a",
            )

            specialities = wait.until(
                EC.presence_of_all_elements_located(All_specialities)
            )
            for specialty in specialities:
                href = specialty.get_attribute("href")
                All_specialities_urls.append(href)
            for urls in All_specialities_urls:
                self.driver.execute_script("window.open(arguments[0])", urls)
            wait.until(
                lambda d: d.execute_script("return document.readyState") == "complete"
            )
            time.sleep(20)

            handles = self.driver.window_handles

            for window in handles:

                self.driver.switch_to.window(window)

                log.info("start")
                try:

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
                            "#custom-main-sub-hdng .et_pb_text_inner",
                            {
                                "elza",
                                "24px",
                                "29px",
                                "#373737",
                                "400",
                            },
                            [
                                "font-family",
                                "line-height",
                                "font-size",
                                "font-family",
                                "font-weight",
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
                        (
                            "#main-sub-hdng",
                            {"20px"},
                            ["padding-left", "padding-right", "margin-bottom"],
                        ),
                        (
                            ".dg-post-thumb",
                            {"0% 0%", "relative", "0px", "auto"},
                            [
                                "position",
                                "top",
                                "bottom",
                                "background-size",
                                "background-position",
                            ],
                        ),
                        (
                            "h2",
                            {
                                "387.188px",
                                "16px 0px 10px",
                                "1230px",
                                "25px",
                                "0px",
                                "393.594px",
                                "600",
                                "22.5px",
                                "258.188px",
                                "elza",
                                "154.953px",
                                "607px",
                                "rgba(21, 44, 108, 1)",
                                "16px",
                                "28px",
                                "30px",
                                "1240px",
                                "normal",
                                '"Open Sans"',
                                "elza, sans-serif",
                                "0px 0px 10px",
                                "394.312px",
                                "36px",
                                "34px",
                                "block",
                                "232.094px",
                                "257.188px",
                                "319.906px",
                                "32px",
                                "620.094px",
                                "393.094px",
                                "22px",
                                "20px",
                                "377.188px",
                                "auto",
                                "38px",
                                "rgba(252, 176, 64, 1)",
                                "700",
                                "Elza",
                                "rgba(0, 0, 0, 0.75)",
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
                            ".category #breadcrumb-content .container .breadcrumb",
                            {"0 20px 20px"},
                            ["padding"],
                        ),
                    ]

                    log.info("medium")
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
                except Exception:
                    ()
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
                    "#custom-main-sub-hdng .et_pb_text_inner",
                    {
                        "elza",
                        "24px",
                        "29px",
                        "#373737",
                        "400",
                    },
                    [
                        "font-family",
                        "line-height",
                        "font-size",
                        "font-family",
                        "font-weight",
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
                (
                    "#main-sub-hdng",
                    {"20px"},
                    ["padding-left", "padding-right", "margin-bottom"],
                ),
                (
                    ".dg-post-thumb",
                    {"0% 0%", "relative", "0px", "auto"},
                    [
                        "position",
                        "top",
                        "bottom",
                        "background-size",
                        "background-position",
                    ],
                ),
                (
                    "h2",
                    {
                        "387.188px",
                        "16px 0px 10px",
                        "1230px",
                        "25px",
                        "0px",
                        "393.594px",
                        "600",
                        "22.5px",
                        "258.188px",
                        "elza",
                        "154.953px",
                        "607px",
                        "rgba(21, 44, 108, 1)",
                        "16px",
                        "28px",
                        "30px",
                        "1240px",
                        "normal",
                        '"Open Sans"',
                        "elza, sans-serif",
                        "0px 0px 10px",
                        "394.312px",
                        "36px",
                        "34px",
                        "block",
                        "232.094px",
                        "257.188px",
                        "319.906px",
                        "32px",
                        "620.094px",
                        "393.094px",
                        "22px",
                        "20px",
                        "377.188px",
                        "auto",
                        "38px",
                        "rgba(252, 176, 64, 1)",
                        "700",
                        "Elza",
                        "rgba(0, 0, 0, 0.75)",
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
                    ".category #breadcrumb-content .container .breadcrumb",
                    {"0 20px 20px"},
                    ["padding"],
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
                    "#custom-main-sub-hdng .et_pb_text_inner",
                    {
                        "elza",
                        "24px",
                        "29px",
                        "#373737",
                        "400",
                    },
                    [
                        "font-family",
                        "line-height",
                        "font-size",
                        "font-family",
                        "font-weight",
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
                (
                    "#main-sub-hdng",
                    {"20px"},
                    ["padding-left", "padding-right", "margin-bottom"],
                ),
                (
                    ".dg-post-thumb",
                    {"0% 0%", "relative", "0px", "auto"},
                    [
                        "position",
                        "top",
                        "bottom",
                        "background-size",
                        "background-position",
                    ],
                ),
                (
                    "h2",
                    {
                        "387.188px",
                        "16px 0px 10px",
                        "1230px",
                        "25px",
                        "0px",
                        "393.594px",
                        "600",
                        "22.5px",
                        "258.188px",
                        "elza",
                        "154.953px",
                        "607px",
                        "rgba(21, 44, 108, 1)",
                        "16px",
                        "28px",
                        "30px",
                        "1240px",
                        "normal",
                        '"Open Sans"',
                        "elza, sans-serif",
                        "0px 0px 10px",
                        "394.312px",
                        "36px",
                        "34px",
                        "block",
                        "232.094px",
                        "257.188px",
                        "319.906px",
                        "32px",
                        "620.094px",
                        "393.094px",
                        "22px",
                        "20px",
                        "377.188px",
                        "auto",
                        "38px",
                        "rgba(252, 176, 64, 1)",
                        "700",
                        "Elza",
                        "rgba(0, 0, 0, 0.75)",
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
                    ".category #breadcrumb-content .container .breadcrumb",
                    {"0 20px 20px"},
                    ["padding"],
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
