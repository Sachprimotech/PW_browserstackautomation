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



class Testone(BaseClass):
    def test_HomePageFeatured(self):
        wait=WebDriverWait(self.driver,20)
        name = self.driver.name
        
        log = self.getLogger()
        log.info(name)

        heading_css=[]
        article_css=[]
        image_css=[]
        window_size =self.driver.get_window_size()
        if window_size['width']> 767:
            popup=self.driver.find_element(By.CSS_SELECTOR,"#onesignal-slidedown-dialog .primary.slidedown-button")
            popup.click()

            Tittle_heading=self.driver.find_elements(By.CSS_SELECTOR,"#mainFeatured article .post-content .post-categories a")
            for heading in Tittle_heading:
             d=['text-transform','text-align','letter-spacing','line-height','font-weight','font-size','font-family','color']
             for i in d:
               heading_css.append(heading.value_of_css_property(i))
            heading_set={'uppercase','left','.025em','17px','700','14px','Elza','rgba(1, 121, 217, 1)'}   

            assert set(heading_css) == heading_set or len(set(heading_css))==8

            Artiles_featured=self.driver.find_elements(By.CSS_SELECTOR,"#featureBlogsection article .post-content h2.entry-title a")
            for articles in Artiles_featured:
             da=['text-transform','text-align','letter-spacing','line-height','font-weight','font-size','font-family','color']
             for ia in da:
               article_css.append(articles.value_of_css_property(ia))
            article_set={'none','left','0','25px','600','14px','Elza','#1c436e'}   

            assert set(article_css) == article_set or len(set(article_css))==8

            image=self.driver.find_elements(By.CSS_SELECTOR,"#featureBlogsection article .post-media img")
            for articles in Artiles_featured:
             im=['object-position','border','object-fit','max-width','height','width']
             for m in im:
               image_css.append(articles.value_of_css_property(m))
            image_set={'100%', '1px solid #bfbfbf', '75px', 'cover', 'top'}   

            assert set(image_css) == image_set or len(set(image_set))==5
            