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
    @pytest.mark.run(order=8)
    @pytest.mark.dependency(depends=["test_HomePageBusinessOfMedicine"])
    def test_header(self):
        social_link = []
        iconCss = []
        Cssvalue = []
        allsociallinks = []
        wait = WebDriverWait(self.driver, 20)
        name = self.driver.name

        log = self.getLogger()
        log.info(name)

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

            log.info("start")
            form = self.driver.find_element(By.XPATH, "//div[@class='social-box']/a")

            formLink = form.get_attribute("href")
            formtarge = form.get_attribute("target")

            assert formtarge == "_blank"
            social_link.append(formLink)
            social_lnk = self.driver.find_elements(
                By.XPATH, "//div[@class='social-box']/ul/li/a"
            )
            for social in social_lnk:
                soc_link = social.get_attribute("href")
                soc_target = social.get_attribute("target")
                social_link.append(soc_link)
                assert soc_target == "_blank"
            subscribe = self.driver.find_element(
                By.XPATH, "//div[@id='header-row-cstm']/div[3]/div"
            )
            assert subscribe.is_displayed
            social_lnkcss = self.driver.find_elements(
                By.XPATH, "//div[@class='social-box']/ul/li"
            )
            for socil in social_lnkcss:
                socil.is_displayed
                d = ["height", "color", "line-height"]
                for i in d:
                    iconCss.append(socil.value_of_css_property(i))
            sd = ["font-size", "font-weight", "font-family", "color", "line-height"]
            for ii in sd:
                Cssvalue.append(subscribe.value_of_css_property(ii))
            form_css = self.driver.find_element(By.XPATH, "//div[@class='social-box']")
            fsd = ["font-size", "font-weight", "font-family", "color", "line-height"]
            for it in fsd:
                Cssvalue.append(form_css.value_of_css_property(it))
            sss = print(iconCss)
            log.info(sss)
            css = print(Cssvalue)
            log.info(css)
            assert (
                Cssvalue
                == [
                    "14px",
                    "400",
                    "Elza",
                    "rgba(0, 0, 0, 0.5)",
                    "23.8px",
                    "14px",
                    "400",
                    "elza",
                    "rgba(148, 148, 148, 1)",
                    "23.8px",
                ]
                or len(set(Cssvalue)) == 7
            )
            assert len(set(iconCss)) == 3
            for soc in social_link:
                self.driver.execute_script("window.open(arguments[0])", soc)

            handles = self.driver.window_handles

            for windows in handles:
                self.driver.switch_to.window(windows)
                alllinks = self.driver.current_url
                allsociallinks.append(alllinks)

            log.info("verifying all social links")
            assert set(social_link) == set(allsociallinks) or len(social_link) == 4
            log.info("All social links are verified sucessfully")
            for social in allsociallinks:
                response = requests.get(social)

                status_code = response.status_code
                log.info("verfying any broken links")
                assert not status_code == 404
                log.info("No broken links")

        elif window_size["width"] <= 767:
            pass
