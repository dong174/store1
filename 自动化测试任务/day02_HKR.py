from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("http://localhost:8080\HKR")
# ============注册==========================================================================
# driver.find_element_by_xpath("/html/body/div/div/div[1]/div[2]/a[1]").click()
# driver.find_element_by_xpath("//*[@id='loginname']").send_keys("DW")
# driver.find_element_by_xpath("//*[@id='msform']/fieldset[1]/input[2]").send_keys("董伟")
# driver.find_element_by_xpath("//*[@id='pwd']").send_keys("123456")
# driver.find_element_by_xpath("//*[@id='msform']/fieldset[1]/input[4]").send_keys("123456")
# driver.find_element_by_xpath("//*[@id='msform']/fieldset[1]/input[5]").click()
# driver.find_element_by_xpath("//*[@id='valid_age']").send_keys("20")
# time.sleep(2)
# driver.find_element_by_xpath("//*[@id='msform']/fieldset[2]/input[3]").click()
# driver.find_element_by_xpath("//*[@id='reg_mail']").send_keys("dong174110@163.com")
# driver.find_element_by_xpath("//*[@id='reg_phone']").send_keys("15565368149")
# driver.find_element_by_xpath("//*[@id='msform']/fieldset[3]/textarea").send_keys("北京")
# time.sleep(2)
# driver.find_element_by_xpath("//*[@id='btn_reg']").click()
# driver.quit()
# ============注册==========================================================================

# driver.find_element_by_xpath("//*[@id='loginname']").send_keys("DW")
# driver.find_element_by_xpath("//*[@id='password']").send_keys("123456")
# driver.find_element_by_xpath("//*[@id='submit']").click()
# time.sleep(2)
# ============修改头像==========================================================================
# driver.find_element_by_xpath("//*[@id='img']").click()
# time.sleep(2)
# driver.find_element_by_xpath("//*[@id='ul_pic']/li[6]/img").click()
# =========================================================================================

# ============提交评价========================================================================
# #driver.find_element_by_xpath("//*[@id='form_table']/tbody/tr[2]/td[2]").send_keys("9 (上晚自习)")
# driver.find_element_by_xpath("//*[@id='form_table']/tbody/tr[7]/td[3]/div/label[2]/div").click()
# driver.find_element_by_xpath("//*[@id='form_table']/tbody/tr[11]/td[2]/div/label[2]/div").click()
# driver.find_element_by_xpath("//*[@id='textarea']").send_keys("waesrdbfsdbvfdasddbfdwddbfds")
# time.sleep(2)
# driver.find_element_by_xpath("//*[@id='subtn']").click()


# ============查询同学==========================================================================
# driver.find_element_by_xpath("//*[@id='_easyui_tree_10']").click()

# ============修改信息==========================================================================
# driver.find_element_by_xpath("//*[@id='_easyui_tree_8']").click()
#
# ac = ActionChains(driver)
#
# age = driver.find_element_by_xpath("//*[@id='_easyui_textbox_input1']")
# ac.double_click(age).send_keys("26").perform()
# ac.release()
# driver.find_element_by_xpath("//*[@id='btn_modify']").click()
#
#
# driver.quit()

##############################################################################################
##############################################################################################
##############################################################################################

#======================教师===================================================================

driver.find_element_by_xpath("/html/body/div/div/div[1]/div[2]/a[2]").click()
driver.find_element_by_xpath("//*[@id='loginname']").send_keys("jason")
driver.find_element_by_xpath("//*[@id='password']").send_keys("admin")
driver.find_element_by_xpath("//*[@id='submit']").click()
time.sleep(1)

#======================教师管理================================================================
# driver.find_element_by_xpath("//*[@id='_easyui_tree_11']/span[4]/a").click()
# time.sleep(2)
# driver.find_element_by_xpath("//*[@id='sear_teaname']").send_keys("贾生")
# driver.find_element_by_xpath("//*[@id='search_user']/span/span[1]").click()
# time.sleep(1)
# driver.find_element_by_xpath("//*[@id='datagrid-row-r1-2-0']/td[9]/div/a").click()

#======================学生管理================================================================
# driver.find_element_by_xpath("//*[@id='_easyui_tree_12']/span[4]/a").click()
# time.sleep(2)
# driver.find_element_by_xpath("//*[@id='J-stu']").send_keys("董伟")
# driver.find_element_by_xpath("//*[@id='J-phone']").send_keys("15565368149")
# driver.find_element_by_xpath("//*[@id='stu_panel']/div/div/div[1]/table/tbody/tr/td[4]/a/span/span[1]").click()
# time.sleep(3)
# driver.find_element_by_xpath("//*[@id='datagrid-row-r1-2-0']/td[11]/div/a").click()

#======================课程管理================================================================
driver.find_element_by_xpath("//*[@id='_easyui_tree_13']").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='course_panel']/div/div/div[1]/table/tbody/tr/td/a/span/span[1]").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='course_form_add']/table/tbody/tr[1]/td[2]/input").send_keys("数据库")
driver.find_element_by_xpath("//*[@id='course_form_add']/table/tbody/tr[2]/td[2]/textarea").send_keys("非常好用！！")
time.sleep(2)
driver.find_element_by_xpath("//*[@class='l-btn l-btn-small']").click()

driver.close()
# driver.find_element_by_xpath("/html/body/div[9]/div[3]/a[2]/span/span[1]").click()













