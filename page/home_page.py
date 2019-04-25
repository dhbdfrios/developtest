from base.base_action import BaseAction
import base


class HomePage(BaseAction):
    def __init__(self, driver):
        BaseAction.__init__(self, driver)

    #实现点击发现按钮
    def click_discover_btn(self):
        self.click_element(base.home_page_btn_discover)



