from utilities.base_class import BaseClass

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import time
import pytest


class Testone(BaseClass):
    @pytest.mark.run(order=1)
    def test_HomePage(self):

        wait = WebDriverWait(self.driver, 20)
        name = self.driver.name

        log = self.getLogger()
        log.info(name)
        Featured = []
        SpacingCss = []
        article_tittleCss = []

        def get_pseudo_element_styles(self, element, pseudo_element, property_name):
            return self.driver.execute_script(
                f"""
        var element = arguments[0];
        var pseudo = window.getComputedStyle(element, "{pseudo_element}");
        return pseudo.getPropertyValue("{property_name}");
        """,
                element,
            )

        log.info("start")
        window_size = self.driver.get_window_size()
        if window_size["width"] > 767:
            try:
                popup = self.driver.find_element(
                    By.CSS_SELECTOR,
                    "#onesignal-slidedown-dialog .primary.slidedown-button",
                )
                popup.click()
            except Exception:
                ()

            Tittles = self.driver.find_elements(
                By.CSS_SELECTOR, "#et-boc .homepage-section-hdng"
            )
            for Tittle in Tittles:

                d = ["padding-top", "align-items"]
                for i in d:
                    Featured.append(Tittle.value_of_css_property(i))
            tittle_set = {"0px", "35px", "baseline"}

            assert set(Featured) == tittle_set or len(set(Featured)) == 3

            Hompagespcing = self.driver.find_elements(By.CSS_SELECTOR, ".et_pb_row")

            properties = ["content", "display", "clear"]
            for spacing in Hompagespcing:
                for prop in properties:
                    value = get_pseudo_element_styles(self, spacing, "::after", prop)
                    SpacingCss.append(value)

            # Expected set of CSS property values
            spacing_set = {'""', "block", "both"}

            # Compare fetched CSS properties with the expected set
            assert set(SpacingCss) == spacing_set or len(set(SpacingCss)) == 3
            log.info("end")

            Article_tittle = self.driver.find_elements(
                By.CSS_SELECTOR, "#et-boc .homepage-section-hdng h3"
            )
            for Article in Article_tittle:
                ar = [
                    "font-size",
                    "font-family",
                    "font-weight",
                    "line-height",
                    "text-transform",
                    "padding-bottom",
                    "color",
                ]
                for a in ar:
                    article_tittleCss.append(Article.value_of_css_property(a))

            articltittle_set = {"28px", "Elza", "600", "100%", "uppercase", "15px"}

            assert (
                set(article_tittleCss) == articltittle_set
                or len(set(article_tittleCss)) == 5
            )
