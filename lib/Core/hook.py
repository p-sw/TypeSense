from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome('assets\\driver.exe')
driver.get("http://s0urce.io")

window_xpath = '//*[@id="window-tool"]'
input_xpath = '//*[@id="tool-type-word"]'
word_xpath = '//*[@id="tool-type"]/img'


console = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, window_xpath)))
input_box = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, input_xpath)))
word_img = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, word_xpath)))
target_msg = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, 'targetmessage-input')))
target_msg_btn = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, 'targetmessage-button-send')))
