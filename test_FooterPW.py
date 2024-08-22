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
    @pytest.mark.run(order=10)
    @pytest.mark.dependency(depends=["test_menubar"])
    def test_footer(self):
        wait = WebDriverWait(self.driver, 20)
        name = self.driver.name

        log = self.getLogger()
        log.info(name)
        footer_linksvalues = []
        Css_values = []
        Footer_cssvalues = []
        Css_linksvalues = []
        menubar_links = []
        all_windowslinks = []
        log.info("start")
        window_size = self.driver.get_window_size()
        if window_size["width"] > 767:
            try:
                popup = self.driver.find_element(
                    By.CSS_SELECTOR, "#onesignal-popover-container"
                )
                popup.click()
            except Exception:
                ()
            footer_links = self.driver.find_elements(
                By.CSS_SELECTOR, ".ft-custom-menu a"
            )

            for links in footer_links:
                lnks = links.get_attribute("href")
                footer_linksvalues.append(lnks)

            Footer_css = self.driver.find_element(
                By.CSS_SELECTOR, "#ft-first-row.et_pb_row"
            )
            f = ["padding-top", "padding-right", "padding-bottom", "padding-left"]
            for i in f:
                Footer_cssvalues.append(Footer_css.value_of_css_property(i))
            assert set(Footer_cssvalues) == {"30px", "20px", "40px", "20px"}

            Tittle = By.CSS_SELECTOR, ".ft-sec-hdng"
            footer_tittlecss = wait.until(EC.presence_of_all_elements_located(Tittle))
            for css in footer_tittlecss:
                if css != None:
                    fsd = ["font-family", "font-weight", "color", "font-size"]
                    for it in fsd:
                        Css_values.append(css.value_of_css_property(it))

            myset = {"elza", "700", "#dbbe46", "18px"}
            assert len(set(Css_values)) == 4 or set(Css_values) == myset

            sss = print(Css_values)
            log.info(sss)
            log.info("end")
            footers_links = By.CSS_SELECTOR, ".ft-custom-menu a"
            ftu_links = wait.until(EC.presence_of_all_elements_located(footers_links))
            for mecss in ftu_links:
                if mecss != None:
                    mfd = [
                        "font-size",
                        "font-weight",
                        "font-family",
                        "color",
                        "letter-spacing",
                    ]
                    for me in mfd:
                        Css_linksvalues.append(mecss.value_of_css_property(me))
            linkset = {"0.48px", "16px", "400", "elza", "rgba(255, 255, 255, 1)"}
            assert len(set(Css_linksvalues)) == 5 or set(Css_linksvalues) == linkset
            footer_linksvalues.append("https://www.physiciansweekly.com/")

            for soc in footer_linksvalues:
                self.driver.execute_script("window.open(arguments[0])", soc)

            handles = self.driver.window_handles

            for windows in handles:
                self.driver.switch_to.window(windows)
                alllinks = self.driver.current_url
                all_windowslinks.append(alllinks)

            log.info("verifying all social links")
            assert (
                set(footer_linksvalues) == set(all_windowslinks)
                or len(footer_linksvalues) == 14
            )
            log.info("All social links are verified sucessfully")
            for social in all_windowslinks:
                response = requests.get(social)

                status_code = response.status_code
                log.info("verfying any broken links")
                assert not status_code == 404
                log.info("No broken links")

        elif window_size["width"] <= 767:

            try:
                popup = self.driver.find_element(
                    By.CSS_SELECTOR, "#onesignal-popover-container"
                )
                popup.click()
            except Exception:
                ()
            footer_links = self.driver.find_elements(
                By.CSS_SELECTOR, ".ft-custom-menu a"
            )

            for links in footer_links:
                lnks = links.get_attribute("href")
                footer_linksvalues.append(lnks)

            Footer_css = self.driver.find_element(
                By.CSS_SELECTOR, "#ft-first-row.et_pb_row"
            )
            f = ["padding-top", "padding-right", "padding-bottom", "padding-left"]
            for i in f:
                Footer_cssvalues.append(Footer_css.value_of_css_property(i))
            assert set(Footer_cssvalues) == {"30px", "20px", "0px"}

            Tittle = By.CSS_SELECTOR, ".ft-sec-hdng"
            footer_tittlecss = wait.until(EC.presence_of_all_elements_located(Tittle))
            for css in footer_tittlecss:
                if css != None:
                    fsd = ["font-family", "font-weight", "color", "font-size"]
                    for it in fsd:
                        Css_values.append(css.value_of_css_property(it))

            myset = {"elza", "700", "#dbbe46", "18px"}
            assert len(set(Css_values)) == 4 or set(Css_values) == myset

            sss = print(Css_values)
            log.info(sss)
            log.info("end")
            footers_links = By.CSS_SELECTOR, ".ft-custom-menu a"
            ftu_links = wait.until(EC.presence_of_all_elements_located(footers_links))
            for mecss in ftu_links:
                if mecss != None:
                    mfd = [
                        "font-size",
                        "font-weight",
                        "font-family",
                        "color",
                        "letter-spacing",
                    ]
                    for me in mfd:
                        Css_linksvalues.append(mecss.value_of_css_property(me))
            linkset = {"0.48px", "16px", "400", "elza", "rgba(255, 255, 255, 1)"}
            assert len(set(Css_linksvalues)) == 5 or set(Css_linksvalues) == linkset
            footer_linksvalues.append("https://www.physiciansweekly.com/")

            for soc in footer_linksvalues:
                self.driver.execute_script("window.open(arguments[0])", soc)

            handles = self.driver.window_handles

            for windows in handles:
                self.driver.switch_to.window(windows)
                alllinks = self.driver.current_url
                all_windowslinks.append(alllinks)

            log.info("verifying all social links")
            assert (
                set(footer_linksvalues) == set(all_windowslinks)
                or len(footer_linksvalues) == 14
            )
            log.info("All social links are verified sucessfully")
            for social in all_windowslinks:
                response = requests.get(social)

                status_code = response.status_code
                log.info("verfying any broken links")
                assert not status_code == 404
                log.info("No broken links")
