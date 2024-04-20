from selenium import webdriver


driver = webdriver.Chrome()
driver.get("http://seleniumhq.org")

elem = driver.find_element_by_id('q')

print("element by id : ", elem)

driver.close()