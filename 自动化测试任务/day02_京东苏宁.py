from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.maximize_window()

# driver.get("http://www.jd.com")
# driver.find_element_by_xpath("//input[@clstag='h|keycount|head|search_c']").send_keys("thinkpad t14")
# driver.find_element_by_xpath("//button[@clstag='h|keycount|head|search_a']").click()
# time.sleep(3)
# driver.find_element_by_xpath("//*[@id='J_goodsList']/ul/li[5]/div/div[1]/a/img").click()
# time.sleep(3)
#
# data = driver.window_handles
# driver.switch_to.window(data[1])
#
# driver.find_element_by_xpath("//*[@id='InitCartUrl']").click()
# driver.find_element_by_xpath("//*[@id='kbCoagent']/ul/li[1]/a").click()
# time.sleep(3)
# driver.find_element_by_xpath("/html/body/div[1]/div[4]/div[8]/div/a/span[4]").click()
# driver.quit()
# ================================================================================================================
driver.get("https://www.suning.com/")
driver.find_element_by_xpath("//*[@id='searchKeywords']").send_keys("thinkpad e14")
driver.find_element_by_xpath("//*[@id='searchSubmit']").click()
time.sleep(5)
driver.find_element_by_xpath("//*[@id='ssdsn_search_pro_baoguang-1-0-1_1_01:0010327863_12290347000']/img").click()
data = driver.window_handles
driver.switch_to.window(data[1])
driver.find_element_by_xpath("//*[@id='addCart']").click()
driver.find_element_by_xpath("/html/body/div[38]/div/div[2]/div/div[1]/a").click()
driver.quit()















