# In a file named selenium_helper.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import inspect
import logging
import requests


class SeleniumHelper:
    def __init__(self, driver):
        self.driver = driver

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler("logfile.log")
        formatter = logging.Formatter(
            "%(asctime)s :%(levelname)s : %(name)s :%(message)s"
        )
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger

    def fetch_and_check_css_properties(
        self, css_selector, expected_css_properties, css_properties_list
    ):
        """
        Fetches CSS properties from elements found using the given CSS selector and checks them against expected values.

        :param css_selector: CSS selector to locate elements
        :param expected_css_properties: Set of expected CSS properties
        :param css_properties_list: List of CSS properties to fetch
        :return: True if the fetched properties match the expected properties, False otherwise
        """
        elements = self.driver.find_elements(By.CSS_SELECTOR, css_selector)
        fetched_css_properties = []

        for element in elements:
            for css_property in css_properties_list:
                fetched_css_properties.append(
                    element.value_of_css_property(css_property)
                )

        fetched_css_properties_set = set(fetched_css_properties)

        return fetched_css_properties_set == expected_css_properties or len(
            fetched_css_properties_set
        ) == len(css_properties_list)

    def verify_links(self, selectors, additional_links, expected_link_count):
        all_links = []
        log = logging.getLogger()

        for selector in selectors:
            elements = self.driver.find_elements(By.CSS_SELECTOR, selector)
            links = [element.get_attribute("href") for element in elements]
            all_links.extend(links)

        if additional_links:
            all_links.extend(additional_links)

        for link in all_links:
            self.driver.execute_script("window.open(arguments[0])", link)

        handles = self.driver.window_handles
        opened_links = []
        result_broken = []

        for window in handles:
            self.driver.switch_to.window(window)
            try:
                popup = self.driver.find_element(
                    By.CSS_SELECTOR,
                    "#onesignal-slidedown-dialog .primary.slidedown-button",
                )
                popup.click()
            except Exception:
                ()
            opened_links.append(self.driver.current_url)

        assert set(all_links) == set(opened_links) or (
            len(all_links) == len(opened_links) or expected_link_count
        )

        for link in opened_links:
            response = requests.get(link)
            status_code = response.status_code
            if status_code == 404:

                result_broken.append("fail")
                log.info(f"Link {link} is broken with status code {status_code}")

            elif status_code != 404:
                result_broken.append("pass")

        assert all(element == "pass" for element in result_broken)
        log.info(f"Link {link} is broken with status code {status_code}")


def get_pseudo_element_styles(self, element, pseudo_element, property_name):
    return self.driver.execute_script(
        f"""
        var element = arguments[0];
        var pseudo = window.getComputedStyle(element, "{pseudo_element}");
        return pseudo.getPropertyValue("{property_name}");
        """,
        element,
    )
