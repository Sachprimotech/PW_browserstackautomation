import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

import time




@pytest.fixture(scope="class")
def setup(request):
 
    
  
   
  driver = webdriver.Chrome() or webdriver.Edge() or webdriver.ChromiumEdge() or webdriver.Safari()
 
 
  driver.get("https://www.physiciansweekly.com/")
  driver.maximize_window()

  request.cls.driver = driver
  yield
  # driver.quit()

 
 