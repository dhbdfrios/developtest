from base.base_action import BaseAction
import base
class ArticlePage(BaseAction):
    def __init__(self,driver):
        BaseAction.__init__(self,driver)

    #实现点击文章 tab
    def click_article(self):
        self.click_element(base.article_page_btn_click_aricle)
    #实现搜索文章的内容
    def search_article_content(self,keyword):
        self.input_edit_content(base.article_page_edit_keyword,keyword)
        self.click_element(base.article_page_btn_action_search)

