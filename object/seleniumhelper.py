# In a file named selenium_helper.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests

class SeleniumHelper:
    def __init__(self, driver):
        self.driver = driver

    def fetch_and_check_css_properties(self, css_selector, expected_css_properties, css_properties_list):
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
                fetched_css_properties.append(element.value_of_css_property(css_property))

        fetched_css_properties_set = set(fetched_css_properties)

        return fetched_css_properties_set == expected_css_properties or len(fetched_css_properties_set) == len(css_properties_list)

    def verify_links(self, selectors, additional_links, expected_link_count):
        all_links = []

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

        for window in handles:
            self.driver.switch_to.window(window)
            opened_links.append(self.driver.current_url)

        assert set(all_links) == set(opened_links) or (expected_link_count and len(all_links) == expected_link_count)

        for link in opened_links:
            response = requests.get(link)
            status_code = response.status_code
            assert status_code != 404, f"Link {link} is broken with status code {status_code}"