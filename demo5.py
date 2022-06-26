# 页面下拉指定高度
js = 'document.documentElement.scrollTop=800;'
driver.execute_script(js)
alert = driver.switch_to.alert
# 查看alert中的文字

print(alert.text)
# 点击确定

alert.accept()
# 点击取消（如果有）

alert.dismiss()
# 获取窗口所有句柄
all_handles = driver.window_handles
# 获取当前窗口句柄
curr_window = driver.current_window_handle
# 遍历所有句柄
for k in all_handles:
    # 如果不是当前窗口句柄
    if k != curr_window:
        # 窗口句柄切换
        driver.switch_to.window(k)
iframe = driver.find_element_by_xpath()
# 切换到iframe

driver.switch_to.frame(iframe)
# ...页面操作代码...
# 跳出iframe

driver.switch_to.default_content()

