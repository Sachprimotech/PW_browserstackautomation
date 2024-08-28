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
    @pytest.mark.run(order=9)
    @pytest.mark.dependency(depends=["test_header"])
    def test_menubar(self):
        wait = WebDriverWait(self.driver, 20)
        name = self.driver.name

        log = self.getLogger()
        log.info(name)
        menu_links = []
        Css_values = []
        megamenu_cssvalues = []
        Css_linksvalues = []
        menubar_links = []
        all_windowslinks = []
        helper = SeleniumHelper(self.driver)
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
            menu_bar = self.driver.find_element(By.XPATH, "//div[@id='top-nv-section']")
            assert menu_bar.is_displayed
            menu_barlinks = self.driver.find_elements(
                By.XPATH, "//div[@class='mega-menu-wrap']/ul/li/a"
            )
            for links in menu_barlinks:
                lnks = links.get_attribute("href")
                menu_links.append(lnks)

            megamenu = self.driver.find_element(By.CSS_SELECTOR, "#new-mega-menu")
            f = ["margin-top", "margin-bottom"]
            for i in f:
                megamenu_cssvalues.append(megamenu.value_of_css_property(i))
            assert megamenu_cssvalues == ["-12px", "-12px"]

            menu_barcs = By.CSS_SELECTOR, "ul.mega-menu li"
            mnu_barcss = wait.until(EC.presence_of_all_elements_located(menu_barcs))
            for css in mnu_barcss:
                if css != None:
                    fsd = ["padding"]
                    for it in fsd:
                        Css_values.append(css.value_of_css_property(it))

            myset = {"0px 10px", "0px 25px", "10px 15px", "6px 15px", "8px 0px"}
            assert len(set(Css_values)) == 5 or set(Css_values) == myset

            sss = print(Css_values)
            log.info(sss)
            log.info("end")
            menu_links = By.CSS_SELECTOR, "ul.mega-menu a"
            mnu_links = wait.until(EC.presence_of_all_elements_located(menu_links))
            for mecss in mnu_links:
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
            linkset = {"0.8px", "16px", "500", "700", "elza", "rgba(255, 255, 255, 1)"}
            assert len(set(Css_linksvalues)) == 6 or set(Css_linksvalues) == linkset
            selectors = [
                "a.mega-menu-link",
            ]

            log.info("Verifying links for multiple selectors")
            helper.verify_linkscloud(selectors)
            log.info("All links verified successfully")

            # menu_lilinks = By.CSS_SELECTOR, "a.mega-menu-link"
            # mnu_lilinks = wait.until(EC.presence_of_all_elements_located(menu_lilinks))

            # for linkis in mnu_lilinks:
            #     if linkis != None:
            #         htags = linkis.get_attribute("href")
            #         log.info("href")

            #         menubar_links.append(htags)
            # for soc in menubar_links:
            #     self.driver.execute_script("window.open(arguments[0])", soc)

            # handles = self.driver.window_handles

            # for windows in handles:
            #     self.driver.switch_to.window(windows)
            #     alllinks = self.driver.current_url
            #     all_windowslinks.append(alllinks)

            # log.info("verifying all social links")
            # assert (
            #     set(menubar_links) == set(all_windowslinks) or len(menubar_links) == 34
            # )
            # log.info("All social links are verified sucessfully")
            # for social in all_windowslinks:
            #     response = requests.get(social)

            #     status_code = response.status_code
            #     log.info("verfying any broken links")
            #     assert not status_code == 404
            #     log.info("No broken links")

        else:
            pass
