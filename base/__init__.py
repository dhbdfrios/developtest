from selenium.webdriver.common.by import By

#1 home_page页面
home_page_btn_discover = By.XPATH,"//*[contains(@text,'发现')]"

#2 discover_page
discover_page_edit_search = By.CLASS_NAME,"android.widget.TextView"

#3 article_page
article_page_btn_click_aricle = By.XPATH,"//*[contains(@text,'文章')]"
article_page_edit_keyword = By.ID,"io.manong.developerdaily:id/edt_keyword"
article_page_btn_action_search = By.ID,"io.manong.developerdaily:id/action_search"
