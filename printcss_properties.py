from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("https://www.physiciansweekly.com/specialties/")
driver.maximize_window()

try:
    popup = driver.find_element(By.CSS_SELECTOR, "#onesignal-popover-container")

    popup.click()
except Exception:
    ()

elements = driver.find_elements(By.CSS_SELECTOR, "h1.is_archive")


fetched_css_properties = []

for element in elements:

    d = [
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
    ]
    for i in d:
        fetched_css_properties.append(element.value_of_css_property(i))


print(set(fetched_css_properties))
