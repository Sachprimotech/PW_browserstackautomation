from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("https://www.physiciansweekly.com/category/allergy-immunology/")
driver.maximize_window()

try:
    popup = driver.find_element(By.CSS_SELECTOR, "#onesignal-popover-container")

    popup.click()
except Exception:
    ()

elements = driver.find_elements(By.CSS_SELECTOR, ".et_pb_button")


fetched_css_properties = []

for element in elements:

    d = [
        "color",
        "font-size",
        "font-weight",
        "padding",
        "font-family",
        "line-height",
        "text-decoration",
    ]
    for i in d:
        fetched_css_properties.append(element.value_of_css_property(i))


print(set(fetched_css_properties))
