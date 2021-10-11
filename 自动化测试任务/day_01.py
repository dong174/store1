from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()

# driver.get(r"E:/python自动化测试/测试/练习的html/弹框的验证/dialogs.html")
# # driver.find_element_by_xpath("//*[@id='alert']").click()
# driver.find_element_by_xpath("//*[@id='confirm']").click()
# time.sleep(1)
# # driver.switch_to.alert.accept()
# driver.switch_to.alert.dismiss()
# time.sleep(1)
# driver.close()

####################################################################################

# driver.get(r"E:/python自动化测试/测试/练习的html/main.html")
# driver.find_element_by_xpath("//*[@id='input1']").send_keys("DWsama")
# time.sleep(1)
# driver.close()


###################################################################################
# driver.get(r"E:/python自动化测试/测试/练习的html/弹框的验证/dialogs.html")
# # driver.find_element_by_xpath("//*[@id='alert']").click()
# driver.find_element_by_xpath("//*[@id='confirm']").click()
# time.sleep(1)
# # driver.switch_to.alert.accept()
# driver.switch_to.alert.dismiss()
# time.sleep(1)
# driver.close()

#
######################################################################################
# driver.get(r"E:/python自动化测试/测试/练习的html/frame.html")
# driver.find_element_by_xpath("//*[@id='input1']").send_keys("DWsama")
# time.sleep(1)
# driver.close()


#####################################################################################

# driver.get(r"E:/python自动化测试/测试/练习的html/跳转页面/pop.html")
# driver.find_element_by_xpath("//*[@id='goo']").click()
# time.sleep(1)
# driver.close()

#
##################################################################################
#
driver.get(r"E:/python自动化测试/测试/练习的html/上传文件和下拉列表/autotest.html")
driver.maximize_window()
driver.find_element_by_xpath("//*[@id='accountID'  and  @name='account'  and  @type='text']").send_keys("DWsama")
driver.find_element_by_xpath("//*[@id='passwordID']").send_keys("admin")
driver.find_element_by_xpath("//*[@id='areaID']").send_keys("北京市")
time.sleep(1)
driver.find_element_by_xpath("//*[@id='sexID2']").click()
driver.find_element_by_xpath("//*[@value='spring']").click()
driver.find_element_by_xpath("//*[@value='Auterm']").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@name='file' and @type='file']").send_keys(r"E:\Media\Picture\壁纸\1.jpg")
time.sleep(2)
driver.close()

#=====================================================================================

# driver.get("http://www.jd.com")
# driver.find_element_by_xpath("//input[@clstag='h|keycount|head|search_c']").send_keys("电脑")
# driver.find_element_by_xpath("//button[@clstag='h|keycount|head|search_a']").click()
# time.sleep(4)
# # driver.get("https://search.jd.com/Search?keyword=电脑&enc=utf-8&wq=电脑&pvid=1b6b1be05549495a89ff62b7a94adeb0")
# driver.find_element_by_xpath("/html/body/div[5]/div[2]/div[2]/div[1]/div/div[2]/ul/li[1]/div/div[1]/a/img").click()
# time.sleep(4)
# driver.close()

#=====================================================================================
# driver.get("http://www.baidu.com")
# time.sleep(1)
# driver.find_element_by_xpath("//input[@id='kw']").send_keys("自动化测试")
# time.sleep(1)
# driver.find_element_by_xpath("//input[@id='su']").click()
# time.sleep(3)
# driver.close()
