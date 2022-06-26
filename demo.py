from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://www.lanqiao.cn")

# webdriver 提供了一系列的元素定位方法，常用的有以下几种:
#     id
#     name
#     class name
#     tag name
#     link text
#     partial link text
#     xpath
#     css selector
# 分别对应 python webdriver 中的方法为：
#     find_element_by_id()
#     find_element_by_name()
#     find_element_by_class_name()
#     find_element_by_tag_name()
#     find_element_by_link_text()
#     find_element_by_partial_link_text()
#     find_element_by_xpath()
#     find_element_by_css_selector()
#使用方法：一般为先进行元素的定位，如果该元素可以点击如：超链接、文本框、带有超链接的图片等，则该元素可以进行点击操
# find_element_by_id().click()