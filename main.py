from selenium import webdriver

driver = webdriver.Firefox(executable_path=r'D:\geckodriver.exe')
driver.get('https://facebook.com')

UserName_xpath = '//*[@id="email"]'

User_Name = driver.find_element_by_xpath(UserName_xpath)
User_Name.send_keys() #fill username

Password_xpath = '//*[@id="pass"]'

Password = driver.find_element_by_xpath(Password_xpath)
Password.send_keys() #fill password

Login_xpath = '//*[@id="u_0_b"]'

Login = driver.find_element_by_xpath(Login_xpath)
Login.click()


#driver.close()
