from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("https://www.physiciansweekly.com/podcast/")
driver.maximize_window()
window_size = driver.get_window_size()

try:
    popup = driver.find_element(By.CSS_SELECTOR, "#onesignal-popover-container")

    popup.click()
except Exception:
    ()

elements = driver.find_elements(
    By.CSS_SELECTOR,
    ".et_pb_section div[class*=et_pb_row_]",
)


fetched_css_properties = []

for element in elements:

    d = [
        "width",
        "padding",
        "margin",
        "font-weight",
        "max-width",
    ]
    for i in d:
        fetched_css_properties.append(element.value_of_css_property(i))


print(set(fetched_css_properties))
print(window_size)
