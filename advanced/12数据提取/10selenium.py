from selenium import webdriver
# driver = webdriver.PhantomJS('c:../pantomjs.exe')
# driver = webdriver.Chrome()
# 屏幕最大化
driver.maximize_window()
# 发送请求
driver.get('http://www.baidu.com')
# 页面截屏
driver.save_screenshot('./baidu.png')

# 元素定位
driver.find_element_by_id('kw').send_keys('python')
driver.find_element_by_id('su').click()

# 获取cookie
driver.get_cookies()

# 退出当前页
driver.close()
# 退出浏览器
driver.quit()