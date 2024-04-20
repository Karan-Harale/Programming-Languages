from selenium import webdriver
driver= webdriver.Chrome()
driver.get("file:///C:/Users/Karan/OneDrive/Documents/Languages/Web%20developement/Tourist%20website/main.html")
login_form = driver.find_element_by_id('home')
print("My login form element is:")
print(login_form)
driver.close()
