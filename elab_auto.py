import time 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
def getcode(q_no):
    driver = webdriver.Chrome()
    actions = ActionChains(driver)
    driver.get('https://60e1d7638f78504dd5d8354197730d85.github.io/');
    select = Select(driver.find_element_by_id('lab'))
    select.select_by_index(1) # dropdown option forlab
    driver.find_element_by_id("q_id").click()
    driver.find_element_by_id("q_id").send_keys(q_no);
    driver.find_element_by_id("submit_code").click()
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#output > ul > li:nth-child(1) > a")))
    element.click()
    driver.switch_to.window(driver.window_handles[1]) 
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "body>pre")))
    driver.close()
    return element.text

driver = webdriver.Chrome()
actions = ActionChains(driver)
driver.get('http://care.srmuniv.ac.in/rmpcsecpp/');
user = driver.find_element_by_name("username")
password = driver.find_element_by_name("password")
user.clear()
user.send_keys("RA1711003020466")
password.clear()
password.send_keys("Awesome123")
driver.find_element_by_id("button").click()
wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'div.card.choice.center.indigo.darken-1')))
driver.find_element_by_css_selector("div.card.choice.center.indigo.darken-1").click()
driver.refresh()
for i in range(0,99):
    driver.get("http://care.srmuniv.ac.in/rmpcsecpp/login/student/code/cpp/cpp.code.php?id=1&value="+str(i+1));
    element=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#codeEditor > div > div.CodeMirror-scroll')))
    WebDriverWait(driver, 5)
    element.click()
    q_no=driver.find_element_by_css_selector('body > div.main_div > div > div.col.s12.m12.l4.question_div > div > ul > li:nth-child(2) > b').text.strip('Q.')
    #driver.find_element_by_css_selector('.CodeMirror-sizer').click()
    ActionChains(driver).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform();
    driver.find_element_by_css_selector('.CodeMirror textarea').send_keys(getcode(q_no))
    driver.find_element_by_id("evaluateButton").click()
    WebDriverWait(driver, 5)
   
    #driver.find_element_by_id("printMsg").click()

driver.quit() 