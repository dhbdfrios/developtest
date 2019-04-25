from base.base_action import BaseAction
import base
class DiscoverPage(BaseAction):

    def __init__(self,driver):
        BaseAction.__init__(self,driver)

    #点击搜索框
    def click_search_edit(self):
        self.click_element(base.discover_page_edit_search)

        