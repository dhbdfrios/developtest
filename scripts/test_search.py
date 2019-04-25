import sys,os
sys.path.append(os.getcwd())
import pytest
from base.init_driver import init_driver
from page.article_page import ArticlePage
from page.discover_page import DiscoverPage
from page.home_page import HomePage
from base.read_yaml import read_yaml_data
import time


def get_test_search_data():
    data = read_yaml_data("search_data.yaml")
    keyword_list =  data.get("data")
    print(keyword_list)
    return keyword_list

class TestSearch:
    def setup_class(self):
        self.driver = init_driver()
        self.articlePage = ArticlePage(self.driver)
        self.discoverPage = DiscoverPage(self.driver)
        self.homePage = HomePage(self.driver)

    def test_discover(self):
        self.homePage.click_discover_btn()
        self.discoverPage.click_search_edit()
        self.articlePage.click_article()

    @pytest.mark.parametrize("keyword", get_test_search_data())
    def test_search_article_content(self,keyword):
        self.articlePage.search_article_content(keyword)


    def teardown_class(self):
        time.sleep(5)
        self.driver.quit()


