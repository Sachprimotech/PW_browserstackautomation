from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("https://www.physiciansweekly.com/")
driver.maximize_window()

try:
    popup = driver.find_element(By.CSS_SELECTOR, "#onesignal-popover-container")

    popup.click()
except Exception:
    ()

elements = driver.find_elements(
    By.CSS_SELECTOR, ".custom-slider #slider-container #slider .slide a img"
)


fetched_css_properties = []

for element in elements:

    d = ["border", "object-fit", "min-height", "max-height", "width"]
    for i in d:
        fetched_css_properties.append(element.value_of_css_property(i))


print(fetched_css_properties)
