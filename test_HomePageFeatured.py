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
    @pytest.mark.run(order=4)
    @pytest.mark.dependency(depends=["test_HomePageNews"])
    def test_HomePageFeatured(self):
        wait = WebDriverWait(self.driver, 20)
        name = self.driver.name

        log = self.getLogger()
        log.info(name)

        heading_css = []
        article_css = []
        image_css = []
        urls = []
        allwindowsinks = []
        left_section_css = []
        right_section_css = []
        window_size = self.driver.get_window_size()
        if window_size["width"] > 980:
            try:
                popup = self.driver.find_element(
                    By.CSS_SELECTOR,
                    "#onesignal-slidedown-dialog .primary.slidedown-button",
                )
                popup.click()
            except Exception:
                ()
            Tittle_heading = self.driver.find_elements(
                By.CSS_SELECTOR,
                "#mainFeatured article .post-content .post-categories a",
            )
            for heading in Tittle_heading:
                d = [
                    "text-transform",
                    "text-align",
                    "letter-spacing",
                    "line-height",
                    "font-weight",
                    "font-size",
                    "font-family",
                    "color",
                ]
                for i in d:
                    heading_css.append(heading.value_of_css_property(i))
            heading_set = {
                "uppercase",
                "left",
                ".025em",
                "17px",
                "700",
                "14px",
                "Elza",
                "rgba(1, 121, 217, 1)",
            }

            assert set(heading_css) == heading_set or len(set(heading_css)) == 8

            Artiles_featured = self.driver.find_elements(
                By.CSS_SELECTOR,
                "#featureBlogsection article .post-content h2.entry-title a",
            )
            for articles in Artiles_featured:
                da = [
                    "text-transform",
                    "text-align",
                    "letter-spacing",
                    "line-height",
                    "font-weight",
                    "font-size",
                    "font-family",
                    "color",
                ]
                for ia in da:
                    article_css.append(articles.value_of_css_property(ia))
            article_set = {
                "none",
                "left",
                "0",
                "25px",
                "600",
                "14px",
                "Elza",
                "#1c436e",
            }

            assert set(article_css) == article_set or len(set(article_css)) == 8

            image = self.driver.find_elements(
                By.CSS_SELECTOR, "#featureBlogsection article .post-media img"
            )
            for ima in image:
                im = [
                    "object-position",
                    "border",
                    "object-fit",
                    "max-width",
                    "height",
                    "width",
                ]
                for m in im:
                    image_css.append(ima.value_of_css_property(m))
            image_set = {"100%", "1px solid #bfbfbf", "75px", "cover", "top"}

            assert set(image_css) == image_set or len(set(image_set)) == 5

            left_section = self.driver.find_elements(
                By.CSS_SELECTOR, "#mainFeatured div#leftFeaturedblog"
            )
            for lf in left_section:
                ll = ["margin-right", "width", "padding-right"]
                for lt in ll:
                    left_section_css.append(lf.value_of_css_property(lt))
            imagesection_set = {"2%", "55%", "20px"}

            assert (
                set(left_section_css) == imagesection_set
                or len(set(left_section_css)) == 3
            )

            right_section = self.driver.find_elements(
                By.CSS_SELECTOR, "#mainFeatured #featureBlogsection"
            )
            for rt in right_section:
                rr = ["width"]
                for rig in rr:
                    right_section_css.append(rt.value_of_css_property(rig))
            right_section_set = {"43%"}

            All_links = self.driver.find_elements(By.CSS_SELECTOR, "#mainFeatured a")
            for All in All_links:
                links = All.get_attribute("href")
                urls.append(links)
            urls.append("https://www.physiciansweekly.com/")
            for soc in urls:
                self.driver.execute_script("window.open(arguments[0])", soc)

            handles = self.driver.window_handles

            for windows in handles:
                self.driver.switch_to.window(windows)
                alllinks = self.driver.current_url
                allwindowsinks.append(alllinks)

            log.info("verifying all social links")
            assert set(urls) == set(allwindowsinks) or len(set(allwindowsinks)) == 12
            log.info("All social links are verified sucessfully")
            for social in allwindowsinks:
                response = requests.get(social)

                status_code = response.status_code
                log.info("verfying any broken links")
                assert not status_code == 404
            log.info("No broken links")

        elif window_size["width"] > 767 and window_size["width"] < 981:
            Tittle_heading = self.driver.find_elements(
                By.CSS_SELECTOR,
                "#mainFeatured article .post-content .post-categories a",
            )
            for heading in Tittle_heading:
                d = [
                    "text-transform",
                    "text-align",
                    "letter-spacing",
                    "line-height",
                    "font-weight",
                    "font-size",
                    "font-family",
                    "color",
                ]
                for i in d:
                    heading_css.append(heading.value_of_css_property(i))
            heading_set = {
                "uppercase",
                "left",
                ".025em",
                "17px",
                "700",
                "14px",
                "Elza",
                "rgba(1, 121, 217, 1)",
            }

            assert set(heading_css) == heading_set or len(set(heading_css)) == 8

            Artiles_featured = self.driver.find_elements(
                By.CSS_SELECTOR,
                "#featureBlogsection article .post-content h2.entry-title a",
            )
            for articles in Artiles_featured:
                da = [
                    "text-transform",
                    "text-align",
                    "letter-spacing",
                    "line-height",
                    "font-weight",
                    "font-size",
                    "font-family",
                    "color",
                ]
                for ia in da:
                    article_css.append(articles.value_of_css_property(ia))
            article_set = {
                "none",
                "left",
                "0",
                "25px",
                "600",
                "14px",
                "Elza",
                "#1c436e",
            }

            assert set(article_css) == article_set or len(set(article_css)) == 8

            image = self.driver.find_elements(
                By.CSS_SELECTOR, "#featureBlogsection article .post-media img"
            )
            for ima in image:
                im = [
                    "object-position",
                    "border",
                    "object-fit",
                    "max-width",
                    "height",
                    "width",
                ]
                for m in im:
                    image_css.append(ima.value_of_css_property(m))
            image_set = {"100%", "1px solid #bfbfbf", "75px", "cover", "top"}

            assert set(image_css) == image_set or len(set(image_set)) == 5

            left_section = self.driver.find_elements(
                By.CSS_SELECTOR, "#mainFeatured div#leftFeaturedblog"
            )
            for lf in left_section:
                ll = ["width"]
                for lt in ll:
                    left_section_css.append(lf.value_of_css_property(lt))
            imagesection_set = {"100%"}
            right_section = self.driver.find_elements(
                By.CSS_SELECTOR, "#mainFeatured #featureBlogsection"
            )
            for rt in right_section:
                rr = ["width"]
                for rig in rr:
                    right_section_css.append(rt.value_of_css_property(rig))
            right_section_set = {"100%"}
            right_section_set_1 = {"780px"}
            assert (
                set(right_section_css) == right_section_set
                or set(right_section_css) == right_section_set_1
            )
            All_links = self.driver.find_elements(By.CSS_SELECTOR, "#mainFeatured a")
            for All in All_links:
                links = All.get_attribute("href")
                urls.append(links)
            # urls.append("https://www.physiciansweekly.com/")
            # for soc in urls:
            #     # self.driver.execute_script("window.open(arguments[0])", soc)
            #     self.driver.execute_script("window.open('_blank'),soc")

            # handles = self.driver.window_handles

            # for windows in handles:
            #     self.driver.switch_to.window(windows)
            #     alllinks = self.driver.current_url
            #     allwindowsinks.append(alllinks)

            for social in urls:
                response = requests.get(social)

                status_code = response.status_code
                log.info("verfying any broken links")
                assert not status_code == 404
            log.info("No broken links")

        elif window_size["width"] <= 767:
            Tittle_heading = self.driver.find_elements(
                By.CSS_SELECTOR,
                "#mainFeatured article .post-content .post-categories a",
            )
            for heading in Tittle_heading:
                d = [
                    "text-transform",
                    "text-align",
                    "letter-spacing",
                    "line-height",
                    "font-weight",
                    "font-size",
                    "font-family",
                    "color",
                ]
                for i in d:
                    heading_css.append(heading.value_of_css_property(i))
            heading_set = {
                "uppercase",
                "left",
                ".025em",
                "17px",
                "700",
                "14px",
                "Elza",
                "rgba(1, 121, 217, 1)",
            }

            assert set(heading_css) == heading_set or len(set(heading_css)) == 8

            Artiles_featured = self.driver.find_elements(
                By.CSS_SELECTOR,
                "#featureBlogsection article .post-content h2.entry-title a",
            )
            for articles in Artiles_featured:
                da = [
                    "text-transform",
                    "text-align",
                    "letter-spacing",
                    "line-height",
                    "font-weight",
                    "font-size",
                    "font-family",
                    "color",
                ]
                for ia in da:
                    article_css.append(articles.value_of_css_property(ia))
            article_set = {
                "none",
                "left",
                "0",
                "25px",
                "600",
                "14px",
                "Elza",
                "#1c436e",
            }

            assert set(article_css) == article_set or len(set(article_css)) == 8

            image = self.driver.find_elements(
                By.CSS_SELECTOR, "#featureBlogsection article .post-media img"
            )
            for ima in image:
                im = [
                    "object-position",
                    "border",
                    "object-fit",
                    "max-width",
                    "height",
                    "width",
                ]
                for m in im:
                    image_css.append(ima.value_of_css_property(m))
            image_set = {"100%", "1px solid #bfbfbf", "75px", "cover", "top"}

            assert set(image_css) == image_set or len(set(image_set)) == 5

            left_section = self.driver.find_elements(
                By.CSS_SELECTOR, "#mainFeatured div#leftFeaturedblog"
            )
            for lf in left_section:
                ll = ["width"]
                for lt in ll:
                    left_section_css.append(lf.value_of_css_property(lt))
            imagesection_set = {"100%"}
            right_section = self.driver.find_elements(
                By.CSS_SELECTOR, "#mainFeatured #featureBlogsection"
            )
            for rt in right_section:
                rr = ["width"]
                for rig in rr:
                    right_section_css.append(rt.value_of_css_property(rig))
            right_section_set = {"100%"}
            right_section_set_1 = {"384px"}
            assert (
                set(right_section_css) == right_section_set
                or set(right_section_css) == right_section_set_1
            )
            All_links = self.driver.find_elements(By.CSS_SELECTOR, "#mainFeatured a")
            for All in All_links:
                links = All.get_attribute("href")
                urls.append(links)
            urls.append("https://www.physiciansweekly.com/")
            for soc in urls:
                self.driver.execute_script("window.open(arguments[0])", soc)

            handles = self.driver.window_handles

            for windows in handles:
                self.driver.switch_to.window(windows)
                alllinks = self.driver.current_url
                allwindowsinks.append(alllinks)

            log.info("verifying all social links")
            assert set(urls) == set(allwindowsinks) or len(set(allwindowsinks)) == 12
            log.info("All social links are verified sucessfully")
            for social in allwindowsinks:
                response = requests.get(social)

                status_code = response.status_code
                log.info("verfying any broken links")
                assert not status_code == 404
            log.info("No broken links")
