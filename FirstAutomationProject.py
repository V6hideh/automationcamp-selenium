from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)


driver=webdriver.Chrome(options=chrome_options)
base_url = "https://play1.automationcamp.ir/"

# driver.get("https://www.google.com/")
# search_field = driver.find_element('name', 'q')
# search_field.send_keys("keep it simple stupid")
# search_field.send_keys(Keys.RETURN)

driver.get(f"{base_url}/forms.html")
driver.find_element('id', 'check_python').click()
check1 = driver.find_element('id', 'check_validate').text
assert check1 == 'PYTHON'
text1 = 'Hello automation world!'
driver.find_element('id', 'notes').send_keys(text1)
check2= driver.find_element('id', 'area notes validate').text
assert check2 == text1
driver.quit()

